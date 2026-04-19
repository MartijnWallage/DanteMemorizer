import re
import unicodedata
from flask import Flask, render_template, session, request, jsonify

from data.canto1 import VOCABULARY, LINES, SENTENCES

app = Flask(__name__)
app.secret_key = "la-selva-oscura-key"

# ─── Data expansion ───────────────────────────────────────────────────────────

def _expand_sentence(s):
    """Fill in derived fields from a minimal {italian, literal} sentence entry."""
    if "word_order" in s and "translation" in s:
        return s
    s = dict(s)
    italian_lines = [l for l in s["italian"].split("\n") if l.strip()]
    literal_lines = s.get("literal", [""] * len(italian_lines))
    start_line = s["lines"][0]
    if "word_order" not in s:
        s["word_order"] = [
            {
                "line": start_line + i,
                "tokens": line.split(),
                "translation": literal_lines[i] if i < len(literal_lines) else "",
                "hint": "",
            }
            for i, line in enumerate(italian_lines)
        ]
    if "translation" not in s:
        s["translation"] = {
            "lines": s["lines"],
            "prompt": "\n".join(literal_lines),
            "italian": s["italian"],
            "note": "",
        }
    s.setdefault("vocab_ids", [])
    return s

SENTENCES = [_expand_sentence(s) for s in SENTENCES]

# ─── Helpers ──────────────────────────────────────────────────────────────────

def normalise(text):
    """Strip punctuation and accents, lowercase — for loose comparison."""
    text = text.lower()
    text = unicodedata.normalize("NFD", text)
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    text = re.sub(r"[^\w\s]", "", text)
    return text.split()


def token_match(answer_tokens, correct_tokens):
    """Return list of (user_tok, correct_tok, ok) for each position."""
    results = []
    for i, ct in enumerate(correct_tokens):
        ut = answer_tokens[i] if i < len(answer_tokens) else ""
        results.append({
            "user": ut,
            "correct": ct,
            "ok": normalise(ut) == normalise(ct),
        })
    return results


def compare_translation(student_text, correct_text):
    """Compare student Italian against Dante's text line by line.

    Returns status 'correct' (0 errors), 'pass' (≤15% errors), or
    'retry' (>15% errors), plus per-line token results for display.
    Each token result carries the correct raw word and an ok flag.
    """
    student_lines = [l.strip() for l in student_text.strip().split('\n')]
    correct_lines = [l.strip() for l in correct_text.strip().split('\n')]

    total_c = 0
    total_wrong = 0
    line_results = []

    for i, correct_line in enumerate(correct_lines):
        student_line = student_lines[i] if i < len(student_lines) else ""
        s_norm = normalise(student_line)
        s_raw  = student_line.split()   # raw tokens for inline markup display
        c_raw  = correct_line.split()

        # Build (raw_word, normalised_word_or_None) pairs, skipping punct-only
        c_pairs = []
        for w in c_raw:
            n = normalise(w)
            c_pairs.append((w, n[0] if n else None))

        tokens = []
        s_idx = 0
        for c_raw_w, c_norm_w in c_pairs:
            if c_norm_w is None:
                # Pure punctuation — always ok, don't consume a student token
                tokens.append({"correct": c_raw_w, "student": None, "ok": True})
                continue
            s_raw_w  = s_raw[s_idx]  if s_idx < len(s_raw)  else None
            s_norm_w = s_norm[s_idx] if s_idx < len(s_norm) else ""
            tokens.append({"correct": c_raw_w, "student": s_raw_w,
                           "ok": s_norm_w == c_norm_w})
            s_idx += 1

        c_count = sum(1 for _, n in c_pairs if n is not None)
        wrong = sum(1 for t in tokens if not t["ok"])
        # Penalise surplus student words
        wrong += max(0, len(s_norm) - c_count)

        total_c += c_count
        total_wrong += wrong
        line_results.append({"tokens": tokens, "ok": wrong == 0})

    error_ratio = total_wrong / max(total_c, 1)
    if error_ratio == 0:
        status = "correct"
    elif error_ratio <= 0.15:
        status = "pass"
    else:
        status = "retry"

    return {"status": status, "line_results": line_results}


# ─── Routes ──────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    learn_phases = session.get("learn_phase", {})
    sentence_statuses = []
    for i, s in enumerate(SENTENCES):
        phase = learn_phases.get(s["id"], "vocab")
        if phase == "done":
            status = "done"
        elif i == 0 or learn_phases.get(SENTENCES[i - 1]["id"], "vocab") == "done":
            status = "active"
        else:
            status = "locked"
        sentence_statuses.append({
            "lines": s["lines"],
            "phase": phase,
            "status": status,
        })
    sentences_done = sum(1 for ss in sentence_statuses if ss["status"] == "done")
    return render_template(
        "index.html",
        sentence_statuses=sentence_statuses,
        sentences_done=sentences_done,
        sentences_total=len(SENTENCES),
    )


@app.route("/about")
def about():
    return render_template(
        "about.html",
   )


@app.route("/text")
def full_text():
    return render_template(
        "text.html",
        lines=LINES,
   )

# ─── Learn flow ──────────────────────────────────────────────────────────────

def _vocab_map():
    needed = {vid for s in SENTENCES for vid in s["vocab_ids"]}
    return {w["id"]: w for w in VOCABULARY if w["id"] in needed}


@app.route("/learn")
def learn():
    mastery = session.get("word_mastery", {})
    raw     = session.get("learn_phase", {})
    phases  = {s["id"]: raw.get(s["id"], "vocab") for s in SENTENCES}
    return render_template(
        "learn.html",
        sentences=SENTENCES,
        vocab_map=_vocab_map(),
        mastery=mastery,
        phases=phases,
    )


@app.route("/api/learn/vocab/result", methods=["POST"])
def api_learn_vocab_result():
    data    = request.get_json()
    word_id = data.get("word_id")
    result  = data.get("result")   # 'new' | 'knew' | 'forgot'

    mastery = session.get("word_mastery", {})
    current = mastery.get(word_id, 0)

    if result == "new":
        mastery[word_id] = 1          # first viewing counts as one pass
    elif result == "knew":
        mastery[word_id] = min(current + 1, 3)
    # 'forgot': no change

    session["word_mastery"] = mastery
    return jsonify({"mastery": mastery.get(word_id, 0)})


@app.route("/api/learn/phase/advance", methods=["POST"])
def api_learn_phase_advance():
    data       = request.get_json()
    sent_id    = data.get("sentence_id")
    from_phase = data.get("from_phase")

    order  = ["vocab", "word_order", "translation", "done"]
    phases = session.get("learn_phase", {})
    current = phases.get(sent_id, "vocab")

    if current == from_phase and from_phase in order:
        idx = order.index(from_phase)
        if idx + 1 < len(order):
            phases[sent_id] = order[idx + 1]

    session["learn_phase"] = phases
    return jsonify({"phase": phases.get(sent_id, "vocab")})


@app.route("/api/learn/word-order/check", methods=["POST"])
def api_learn_word_order_check():
    data      = request.get_json()
    sent_id   = data.get("sentence_id")
    answer    = data.get("answer", [])
    line_idx  = data.get("line_index", 0)

    sentence = next((s for s in SENTENCES if s["id"] == sent_id), None)
    if not sentence:
        return jsonify({"error": "not found"}), 404

    wo_list = sentence["word_order"]
    if line_idx < 0 or line_idx >= len(wo_list):
        return jsonify({"error": "invalid line_index"}), 400

    wo          = wo_list[line_idx]
    results     = token_match(answer, wo["tokens"])
    all_correct = all(r["ok"] for r in results) and len(answer) == len(wo["tokens"])
    is_last     = line_idx == len(wo_list) - 1

    phase_advanced = False
    if all_correct and is_last:
        phases = session.get("learn_phase", {})
        if phases.get(sent_id, "vocab") == "word_order":
            phases[sent_id] = "translation"
            session["learn_phase"] = phases
            phase_advanced = True

    return jsonify({
        "correct":        all_correct,
        "results":        results,
        "translation":    wo["translation"],
        "hint":           wo["hint"],
        "is_last":        is_last,
        "phase_advanced": phase_advanced,
    })


@app.route("/api/learn/translation/submit", methods=["POST"])
def api_learn_translation_submit():
    data    = request.get_json()
    sent_id = data.get("sentence_id")
    answer  = data.get("answer", "")

    sentence = next((s for s in SENTENCES if s["id"] == sent_id), None)
    if not sentence:
        return jsonify({"error": "not found"}), 404

    tr     = sentence["translation"]
    result = compare_translation(answer, tr["italian"])
    status = result["status"]
    response = {"status": status, "line_results": result["line_results"]}

    if status == "correct":
        phases = session.get("learn_phase", {})
        if phases.get(sent_id, "vocab") == "translation":
            phases[sent_id] = "done"
            session["learn_phase"] = phases
        response["note"] = tr["note"]
    elif status == "pass":
        response["note"] = tr["note"]   # show note even on pass (for reference)
    elif status == "retry":
        wrong = sum(1 for lr in result["line_results"] if not lr["ok"])
        total = len(result["line_results"])
        s = "s" if wrong != 1 else ""
        v = "have" if wrong != 1 else "has"
        response["hint"] = f"{wrong} of {total} line{s} {v} errors — try again."

    return jsonify(response)


@app.route("/api/reset", methods=["POST"])
def api_reset():
    session.clear()
    return jsonify({"ok": True})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
