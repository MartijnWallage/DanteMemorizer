import re
import unicodedata
from flask import Flask, render_template, session, request, jsonify

from data.canto1 import VOCABULARY, WORD_ORDER, TRANSLATION, LINES, SENTENCES

app = Flask(__name__)
app.secret_key = "la-selva-oscura-key"

# ─── Unlock thresholds ────────────────────────────────────────────────────────

VOCAB_THRESHOLD = 10        # words marked known to unlock word-order
WORD_ORDER_THRESHOLD = 5    # exercises done to unlock translation


# ─── Helpers ──────────────────────────────────────────────────────────────────

def get_progress():
    return {
        "vocab_known": session.get("vocab_known", []),
        "word_order_done": session.get("word_order_done", []),
        "translation_done": session.get("translation_done", []),
    }


def word_order_unlocked(p):
    return len(p["vocab_known"]) >= VOCAB_THRESHOLD


def translation_unlocked(p):
    return len(p["word_order_done"]) >= WORD_ORDER_THRESHOLD


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


@app.route("/flashcards")
def flashcards():
    p = get_progress()
    return render_template(
        "flashcards.html",
        vocab=VOCABULARY,
        known=p["vocab_known"],
        progress=p,
        word_order_unlocked=word_order_unlocked(p),
        translation_unlocked=translation_unlocked(p),
        vocab_threshold=VOCAB_THRESHOLD,
    )


@app.route("/word-order")
def word_order():
    p = get_progress()
    if not word_order_unlocked(p):
        return render_template("locked.html",
                               reason=f"Learn {VOCAB_THRESHOLD} vocabulary words first.",
                               back_url="/flashcards")
    return render_template(
        "word_order.html",
        exercises=WORD_ORDER,
        done=p["word_order_done"],
        progress=p,
        word_order_unlocked=True,
        translation_unlocked=translation_unlocked(p),
        word_order_threshold=WORD_ORDER_THRESHOLD,
    )


@app.route("/translation")
def translation():
    p = get_progress()
    if not translation_unlocked(p):
        return render_template("locked.html",
                               reason=f"Complete {WORD_ORDER_THRESHOLD} word-order exercises first.",
                               back_url="/word-order")
    return render_template(
        "translation.html",
        exercises=TRANSLATION,
        done=p["translation_done"],
        progress=p,
        word_order_unlocked=True,
        translation_unlocked=True,
    )


@app.route("/about")
def about():
    p = get_progress()
    return render_template(
        "about.html",
        progress=p,
        word_order_unlocked=word_order_unlocked(p),
        translation_unlocked=translation_unlocked(p),
    )


@app.route("/text")
def full_text():
    p = get_progress()
    return render_template(
        "text.html",
        lines=LINES,
        progress=p,
        word_order_unlocked=word_order_unlocked(p),
        translation_unlocked=translation_unlocked(p),
    )


# ─── API ─────────────────────────────────────────────────────────────────────

@app.route("/api/vocab/mark", methods=["POST"])
def api_vocab_mark():
    data = request.get_json()
    word_id = data.get("id")
    known = data.get("known", True)

    vocab_known = session.get("vocab_known", [])
    if known and word_id not in vocab_known:
        vocab_known.append(word_id)
    elif not known and word_id in vocab_known:
        vocab_known.remove(word_id)

    session["vocab_known"] = vocab_known
    p = get_progress()
    return jsonify({
        "vocab_known": vocab_known,
        "word_order_unlocked": word_order_unlocked(p),
    })


@app.route("/api/word-order/check", methods=["POST"])
def api_word_order_check():
    data = request.get_json()
    ex_id = data.get("id")
    answer = data.get("answer", [])  # list of token strings in order

    exercise = next((e for e in WORD_ORDER if e["id"] == ex_id), None)
    if not exercise:
        return jsonify({"error": "not found"}), 404

    correct_tokens = exercise["tokens"]
    results = token_match(answer, correct_tokens)
    all_correct = all(r["ok"] for r in results) and len(answer) == len(correct_tokens)

    if all_correct:
        done = session.get("word_order_done", [])
        if ex_id not in done:
            done.append(ex_id)
        session["word_order_done"] = done

    p = get_progress()
    return jsonify({
        "correct": all_correct,
        "results": results,
        "translation": exercise["translation"],
        "hint": exercise["hint"],
        "translation_unlocked": translation_unlocked(p),
        "word_order_done": p["word_order_done"],
    })


@app.route("/api/translation/submit", methods=["POST"])
def api_translation_submit():
    data = request.get_json()
    ex_id = data.get("id")
    answer = data.get("answer", "")

    exercise = next((e for e in TRANSLATION if e["id"] == ex_id), None)
    if not exercise:
        return jsonify({"error": "not found"}), 404

    result = compare_translation(answer, exercise["italian"])
    status = result["status"]
    response = {"status": status, "line_results": result["line_results"]}

    if status == "correct":
        done = session.get("translation_done", [])
        if ex_id not in done:
            done.append(ex_id)
        session["translation_done"] = done
        response["note"] = exercise["note"]
        response["translation_done"] = done
    elif status == "retry":
        wrong_lines = sum(1 for lr in result["line_results"] if not lr["ok"])
        total_lines = len(result["line_results"])
        s = "s" if wrong_lines != 1 else ""
        v = "have" if wrong_lines != 1 else "has"
        response["hint"] = f"{wrong_lines} of {total_lines} line{s} {v} errors — try again."
    # pass: return line_results only; student must retype before advancing

    return jsonify(response)


# ─── Learn flow ──────────────────────────────────────────────────────────────

def _vocab_map():
    needed = {vid for s in SENTENCES for vid in s["vocab_ids"]}
    return {w["id"]: w for w in VOCABULARY if w["id"] in needed}


@app.route("/learn")
def learn():
    mastery = session.get("word_mastery", {})
    raw     = session.get("learn_phase", {})
    phases  = {s["id"]: raw.get(s["id"], "vocab") for s in SENTENCES}
    p = get_progress()
    return render_template(
        "learn.html",
        sentences=SENTENCES,
        vocab_map=_vocab_map(),
        mastery=mastery,
        phases=phases,
        word_order_unlocked=True,
        translation_unlocked=True,
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


@app.route("/api/progress")
def api_progress():
    p = get_progress()
    return jsonify({
        **p,
        "word_order_unlocked": word_order_unlocked(p),
        "translation_unlocked": translation_unlocked(p),
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
