"""
Inferno, Canto I — text, vocabulary, and exercises.

Italian text: standard critical edition (Petrocchi).
English translations follow Durling & Martinez (1996) and Hollander & Hollander (2000),
both highly literal scholarly translations.
"""

# ─── Full Italian text ────────────────────────────────────────────────────────

LINES = [
    (1,  "Nel mezzo del cammin di nostra vita"),
    (2,  "mi ritrovai per una selva oscura,"),
    (3,  "ché la diritta via era smarrita."),
    (4,  "Ahi quanto a dir qual era è cosa dura"),
    (5,  "esta selva selvaggia e aspra e forte"),
    (6,  "che nel pensier rinova la paura!"),
    (7,  "Tant'è amara che poco è più morte;"),
    (8,  "ma per trattar del ben ch'i' vi trovai,"),
    (9,  "dirò de l'altre cose ch'i' v'ho scorte."),
    (10, "Io non so ben ridir com'i' v'intrai,"),
    (11, "tant'era pien di sonno a quel punto"),
    (12, "che la verace via abbandonai."),
    (13, "Ma poi ch'i' fui al piè d'un colle giunto,"),
    (14, "là dove terminava quella valle"),
    (15, "che m'aveva di paura il cor compunto,"),
    (16, "guardai in alto e vidi le sue spalle"),
    (17, "vestite già de' raggi del pianeta"),
    (18, "che mena dritto altrui per ogni calle;"),
    (19, "Allor fu la paura un poco queta,"),
    (20, "che nel lago del cor m'era durata"),
    (21, "la notte ch'i' passai con tanta pieta."),
    (22, "E come quei che con lena affannata,"),
    (23, "uscito fuor del pelago a la riva,"),
    (24, "si volge a l'acqua perigliosa e guata,"),
    (25, "così l'animo mio, ch'ancor fuggiva,"),
    (26, "si volse a retro a rimirar lo passo"),
    (27, "che non lasciò già mai persona viva."),
    (28, "Poi ch'èi posato un poco il corpo lasso,"),
    (29, "ripresi via per la piaggia diserta,"),
    (30, "sì che 'l piè fermo sempre era 'l più basso."),
    (31, "Ed ecco, quasi al cominciar de l'erta,"),
    (32, "una lonza leggera e presta molto,"),
    (33, "che di pel macolato era coverta;"),
    (34, "e non mi si partia dinanzi al volto,"),
    (35, "anzi 'mpediva tanto il mio cammino,"),
    (36, "che fu per tornare più volte vòlto."),
    (37, "Temp'era dal principio del mattino,"),
    (38, "e 'l sol montava 'n sù con quelle stelle"),
    (39, "ch'eran con lui quando l'amor divino"),
    (40, "mosse di prima quelle cose belle;"),
    (41, "sì ch'a bene sperar m'era cagione"),
    (42, "di quella fiera a la gaìa pelle"),
    (43, "la stagion nova e l'ora del mattino;"),
    (44, "ma non sì che paura non mi desse"),
    (45, "la vista d'un leon che m'apparve poscia."),
    (46, "Questi parea che contra me venisse"),
    (47, "con la test'alta e con rabbiosa fame,"),
    (48, "sì che parea che l'aere ne tremesse;"),
    (49, "ed una lupa, che di tutte brame"),
    (50, "sembrava carca ne la sua magrezza,"),
    (51, "e molte genti fé già viver grame,"),
    (52, "questa mi porse tanto di gravezza"),
    (53, "con la paura ch'uscia di sua vista,"),
    (54, "che io perdei la speranza de l'altezza."),
    (55, "E qual è quei che volentieri acquista,"),
    (56, "e giugne 'l tempo che perder lo face,"),
    (57, "che 'n tutt'i suoi pensier piange e s'attrista;"),
    (58, "tal mi fece la bestia sanza pace,"),
    (59, "che, venendomi 'ncontro, a poco a poco"),
    (60, "mi ripigneva là dove 'l sol tace."),
    (61, "Mentre ch'i' rovinava in basso loco,"),
    (62, "dinanzi a li occhi mi si fu offerto"),
    (63, "chi per lungo silenzio parea fioco."),
    (64, "Quando vidi costui nel gran diserto,"),
    (65, "«Miserere di me» gridai a lui,"),
    (66, "«qual che tu sii, od ombra od omo vero!»"),
    (67, "Rispuosemi: «Non omo, omo già fui,"),
    (68, "e li parenti miei furon lombardi,"),
    (69, "mantoani per patrïa ambedui."),
    (70, "Nacqui sub Iulio, ancor che fosse tardi,"),
    (71, "e vissi a Roma sotto 'l buono Augusto"),
    (72, "nel tempo de li dèi falsi e bugiardi."),
    (73, "Poeta fui, e cantai di quel giusto"),
    (74, "figliuol d'Anchise che venne di Troia,"),
    (75, "poi che 'l superbo Ilïón fu combusto."),
    (76, "Ma tu perché ritorni a tanta noia?"),
    (77, "perché non sali il dilettoso monte"),
    (78, "che è principio e cagion di tutta gioia?»"),
    (79, "«Or se' tu quel Virgilio e quella fonte"),
    (80, "che spandi di parlar sì largo fiume?»"),
    (81, "rispuos'io lui con vergogna e fronte."),
    (82, "«O de li altri poeti onore e lume,"),
    (83, "vagliami 'l lungo studio e 'l grande amore"),
    (84, "che m'ha fatto cercar lo tuo volume."),
    (85, "Tu se' lo mio maestro e 'l mio autore,"),
    (86, "tu se' solo colui da cu' io tolsi"),
    (87, "lo bello stilo che m'ha fatto onore."),
    (88, "Vedi la bestia per cu' io mi volsi;"),
    (89, "aiutami da lei, famoso saggio,"),
    (90, "ch'ella mi fa tremar le vene e i polsi»."),
    (91, "«A te convien tenere altro viaggio»,"),
    (92, "rispuose poi che lagrimar mi vide,"),
    (93, "«se vuo' campar d'esto loco selvaggio;"),
    (94, "ché questa bestia, per la qual tu gride,"),
    (95, "non lascia altrui passar per la sua via,"),
    (96, "ma tanto 'mpedisce che l'uccide;"),
    (97, "e ha natura sì malvagia e ria,"),
    (98, "che mai non empie la bramosa voglia,"),
    (99, "e dopo 'l pasto ha più fame che pria."),
    (100, "Molti son li animai a cui s'ammoglia,"),
    (101, "e più saranno ancora, infin che 'l Veltro"),
    (102, "verrà, che la farà morir con doglia."),
    (103, "Questi non ciberà terra né peltro,"),
    (104, "ma sapïenza, amore e virtute,"),
    (105, "e sua nazion sarà tra feltro e feltro."),
    (106, "Di quella umile Italia fia salute"),
    (107, "per cui morì la vergine Camilla,"),
    (108, "Eurialo e Turno e Niso di ferute."),
    (109, "Questi la caccerà per ogne villa,"),
    (110, "fin che l'avrà rimessa ne lo 'nferno,"),
    (111, "là onde 'nvidia prima dipartilla."),
    (112, "Ond'io per lo tuo me' penso e discerno"),
    (113, "che tu mi segua, e io sarò tua guida,"),
    (114, "e trarrotti di qui per loco etterno;"),
    (115, "e udrai le disperate strida,"),
    (116, "vedrai li antichi spiriti dolenti,"),
    (117, "che la seconda morte ciascun grida;"),
    (118, "e vederai color che son contenti"),
    (119, "nel foco, perché speran di venire"),
    (120, "quando che sia a le beate genti;"),
    (121, "a le quai poi se tu vorrai salire,"),
    (122, "anima fia a ciò più di me degna;"),
    (123, "con lei ti lascerò in su la fine:"),
    (124, "ché quello 'mperador che là sù regna,"),
    (125, "perché fu' io ribello a la sua legge,"),
    (126, "non vuol che 'n sua città per me si vegna."),
    (127, "In tutte parti impera e quivi regge;"),
    (128, "quivi è la sua città e l'alto seggio:"),
    (129, "oh felice colui cu' ivi elegge!»."),
    (130, "E io a lui: «Poeta, io ti richieggio"),
    (131, "per quello Dio che tu non conoscesti,"),
    (132, "acciò ch'io fugga questo male e peggio,"),
    (133, "che tu mi meni là dov'or dicesti,"),
    (134, "sì ch'io vegga la porta di san Pietro"),
    (135, "e color che tu fai cotanto mesti»."),
    (136, "Allor si mosse, e io li tenni dietro."),
]

# ─── Vocabulary ───────────────────────────────────────────────────────────────

VOCABULARY = [
    {
        "id": "selva",
        "italian": "selva",
        "english": "wood, forest",
        "pos": "noun (f.)",
        "example_italian": "mi ritrovai per una selva oscura",
        "example_english": "I came to myself in a dark wood",
        "note": (
            "From Latin silva (wood, forest). Modern Italian keeps selva as a literary word; "
            "bosco is the everyday term. Related to English 'sylvan'."
        ),
    },
    {
        "id": "oscura",
        "italian": "oscura",
        "english": "dark, obscure",
        "pos": "adjective (f.)",
        "example_italian": "per una selva oscura",
        "example_english": "in a dark wood",
        "note": (
            "Feminine form of oscuro, agreeing with selva (f.). From Latin obscurus. "
            "Gives English 'obscure'. Unchanged in modern Italian."
        ),
    },
    {
        "id": "cammin",
        "italian": "cammin",
        "english": "journey, way",
        "pos": "noun (m.)",
        "example_italian": "nel mezzo del cammin di nostra vita",
        "example_english": "in the middle of the journey of our life",
        "note": (
            "Apocopated form of cammino (loss of final -o). Apocopation before a following word "
            "beginning with a consonant is common in medieval Italian poetry. "
            "From Late Latin camminus (road)."
        ),
    },
    {
        "id": "vita",
        "italian": "vita",
        "english": "life",
        "pos": "noun (f.)",
        "example_italian": "del cammin di nostra vita",
        "example_english": "of the journey of our life",
        "note": (
            "Directly from Latin vita (accusative of vita). Unchanged in modern Italian."
        ),
    },
    {
        "id": "mezzo",
        "italian": "mezzo",
        "english": "middle, midway",
        "pos": "noun/adjective (m.)",
        "example_italian": "nel mezzo del cammin",
        "example_english": "in the middle of the journey",
        "note": (
            "From Latin medius. Functions as noun (il mezzo = the middle) and adjective. "
            "Nel mezzo = in the middle. Survives in modern Italian and in English musical terms "
            "(mezzo-soprano, mezzo-forte)."
        ),
    },
    {
        "id": "via",
        "italian": "via",
        "english": "way, road",
        "pos": "noun (f.)",
        "example_italian": "ché la diritta via era smarrita",
        "example_english": "for the straight way was lost",
        "note": (
            "Directly from Latin via. Unchanged in modern Italian. "
            "Diritta via (straight way) is a key phrase in this canto; cf. also verace via (true way) at line 12."
        ),
    },
    {
        "id": "smarrita",
        "italian": "smarrita",
        "english": "lost, gone astray",
        "pos": "past participle (f.)",
        "example_italian": "la diritta via era smarrita",
        "example_english": "the straight way was lost",
        "note": (
            "Past participle of smarrire (to lose one's way). Feminine to agree with via (f.). "
            "Era smarrita is a pluperfect passive (had been lost). "
            "Smarrire is from Germanic *smirran (to smear, wipe away) via Old French esmarrir."
        ),
    },
    {
        "id": "diritta",
        "italian": "diritta",
        "english": "straight, right",
        "pos": "adjective (f.)",
        "example_italian": "la diritta via era smarrita",
        "example_english": "the straight way was lost",
        "note": (
            "Feminine of diritto. From Latin directus (past participle of dirigere, to direct). "
            "Gives English 'direct', 'direction'. Modern Italian: diritto/a."
        ),
    },
    {
        "id": "paura",
        "italian": "paura",
        "english": "fear",
        "pos": "noun (f.)",
        "example_italian": "che nel pensier rinova la paura",
        "example_english": "which in thought renews the fear",
        "note": (
            "From Latin pavor (dread) via Vulgar Latin *pavorea. "
            "Unchanged in modern Italian. One of the most repeated nouns in Canto I."
        ),
    },
    {
        "id": "morte",
        "italian": "morte",
        "english": "death",
        "pos": "noun (f.)",
        "example_italian": "tant'è amara che poco è più morte",
        "example_english": "so bitter is it, death is little more",
        "note": (
            "From Latin mors, mortis (f., 3rd declension). Unchanged in modern Italian. "
            "Related to English 'mortal', 'murder'."
        ),
    },
    {
        "id": "colle",
        "italian": "colle",
        "english": "hill",
        "pos": "noun (m.)",
        "example_italian": "al piè d'un colle giunto",
        "example_english": "arrived at the foot of a hill",
        "note": (
            "From Latin collis (m.). Unchanged in modern Italian as a literary word; "
            "collina (diminutive) is more common in speech."
        ),
    },
    {
        "id": "valle",
        "italian": "valle",
        "english": "valley",
        "pos": "noun (f.)",
        "example_italian": "là dove terminava quella valle",
        "example_english": "there where that valley ended",
        "note": (
            "From Latin vallis (f.). Unchanged in modern Italian."
        ),
    },
    {
        "id": "sole",
        "italian": "sole",
        "english": "sun",
        "pos": "noun (m.)",
        "example_italian": "e 'l sol montava 'n sù",
        "example_english": "and the sun was climbing",
        "note": (
            "From Latin sol, solis (m.). Modern Italian: sole. "
            "Appears as sol (apocopated) in the verse text."
        ),
    },
    {
        "id": "pianeta",
        "italian": "pianeta",
        "english": "planet",
        "pos": "noun (m.)",
        "example_italian": "vestite già de' raggi del pianeta",
        "example_english": "already clothed in the rays of the planet",
        "note": (
            "From Greek planetes (wanderer) via Latin planeta. "
            "In Ptolemaic cosmology the seven planets included the sun and moon. "
            "Here pianeta refers to the sun."
        ),
    },
    {
        "id": "notte",
        "italian": "notte",
        "english": "night",
        "pos": "noun (f.)",
        "example_italian": "la notte ch'i' passai con tanta pieta",
        "example_english": "the night that I passed with such great pity",
        "note": (
            "From Latin nox, noctis (f.). Unchanged in modern Italian."
        ),
    },
    {
        "id": "lago",
        "italian": "lago",
        "english": "lake",
        "pos": "noun (m.)",
        "example_italian": "che nel lago del cor m'era durata",
        "example_english": "that had lasted in the lake of my heart",
        "note": (
            "From Latin lacus (m.). Unchanged in modern Italian. "
            "Used here metaphorically: nel lago del cor (in the lake of the heart)."
        ),
    },
    {
        "id": "cor",
        "italian": "cor",
        "english": "heart",
        "pos": "noun (m.)",
        "example_italian": "di paura il cor compunto",
        "example_english": "my heart pierced with fear",
        "note": (
            "Apocopated form of core, the older Italian form of cuore. "
            "From Latin cor, cordis (n.). "
            "Related to English 'cordial', 'courage' (< Latin cor + agere)."
        ),
    },
    {
        "id": "pie",
        "italian": "piè",
        "english": "foot",
        "pos": "noun (m.)",
        "example_italian": "al piè d'un colle giunto",
        "example_english": "arrived at the foot of a hill",
        "note": (
            "Apocopated form of piede. From Latin pes, pedis (m.). "
            "Modern Italian: piede. The grave accent marks the open e in the apocopated form."
        ),
    },
    {
        "id": "lasso",
        "italian": "lasso",
        "english": "weary, tired",
        "pos": "adjective (m.)",
        "example_italian": "riposato un poco il corpo lasso",
        "example_english": "having rested a little the weary body",
        "note": (
            "From Latin laxus (loose, slack → exhausted). "
            "Archaic in modern Italian (stanco is the everyday word). "
            "Lasso → Old French las → English 'alas' (via hélas, 'ah, weary one')."
        ),
    },
    {
        "id": "lonza",
        "italian": "lonza",
        "english": "leopard",
        "pos": "noun (f.)",
        "example_italian": "una lonza leggera e presta molto",
        "example_english": "a leopard, light and very swift",
        "note": (
            "Uncertain etymology; possibly from Old French lonce (lynx) "
            "or ultimately from medieval Latin luncea. "
            "The exact species is debated; most commentators identify it as a leopard."
        ),
    },
    {
        "id": "leone",
        "italian": "leone",
        "english": "lion",
        "pos": "noun (m.)",
        "example_italian": "la vista d'un leon che m'apparve poscia",
        "example_english": "the sight of a lion that afterwards appeared to me",
        "note": (
            "From Latin leo, leonis (m.). Appears as leon (apocopated). "
            "Modern Italian: leone."
        ),
    },
    {
        "id": "lupa",
        "italian": "lupa",
        "english": "she-wolf",
        "pos": "noun (f.)",
        "example_italian": "ed una lupa, che di tutte brame",
        "example_english": "and a she-wolf, full of all hungers",
        "note": (
            "Feminine of lupo (wolf). From Latin lupa (she-wolf), "
            "feminine of lupus. Unchanged in modern Italian."
        ),
    },
    {
        "id": "fiera",
        "italian": "fiera",
        "english": "wild beast",
        "pos": "noun (f.)",
        "example_italian": "di quella fiera a la gaìa pelle",
        "example_english": "of that beast with the gay-coloured hide",
        "note": (
            "From Latin fera (wild animal, feminine of ferus, wild). "
            "Modern Italian fiera has two unrelated senses: 'wild beast' (literary) "
            "and 'fair, market' (from Latin feria)."
        ),
    },
    {
        "id": "ombra",
        "italian": "ombra",
        "english": "shade, shadow",
        "pos": "noun (f.)",
        "example_italian": "qual che tu sii, od ombra od omo vero",
        "example_english": "whatever you are, either shade or real man",
        "note": (
            "From Latin umbra (shadow). Unchanged in modern Italian. "
            "In Dante, ombra is the standard term for souls in the afterlife "
            "— they have form but not body."
        ),
    },
    {
        "id": "poeta",
        "italian": "poeta",
        "english": "poet",
        "pos": "noun (m.)",
        "example_italian": "Poeta fui, e cantai di quel giusto",
        "example_english": "A poet was I, and I sang of that just",
        "note": (
            "From Greek poietes via Latin poeta. Unchanged in modern Italian. "
            "Note the inverted word order: Poeta fui (a poet was I), "
            "placing the predicate noun first for emphasis."
        ),
    },
    {
        "id": "monte",
        "italian": "monte",
        "english": "mountain, hill",
        "pos": "noun (m.)",
        "example_italian": "perché non sali il dilettoso monte",
        "example_english": "why do you not climb the delightful mountain",
        "note": (
            "From Latin mons, montis (m.). Unchanged in modern Italian. "
            "Related to English 'mountain', 'mount', 'amount'."
        ),
    },
    {
        "id": "fonte",
        "italian": "fonte",
        "english": "source, spring",
        "pos": "noun (f.)",
        "example_italian": "quel Virgilio e quella fonte",
        "example_english": "that Virgil and that spring",
        "note": (
            "From Latin fons, fontis (f./m.). Modern Italian: fonte (source), fontana (fountain). "
            "Related to English 'font' and 'fountain' (via Old French fontaine)."
        ),
    },
    {
        "id": "maestro",
        "italian": "maestro",
        "english": "master, teacher",
        "pos": "noun (m.)",
        "example_italian": "Tu se' lo mio maestro e 'l mio autore",
        "example_english": "You are my master and my author",
        "note": (
            "From Latin magister. Unchanged in modern Italian and borrowed into English as 'maestro'. "
            "Se' is the contracted form of sei (2nd person singular of essere). "
            "'l is the elided definite article il."
        ),
    },
    {
        "id": "viaggio",
        "italian": "viaggio",
        "english": "journey, way",
        "pos": "noun (m.)",
        "example_italian": "A te convien tenere altro viaggio",
        "example_english": "You must needs take another way",
        "note": (
            "From Late Latin viaticum (provisions for a journey), related to via (road). "
            "Unchanged in modern Italian."
        ),
    },
    {
        "id": "guida",
        "italian": "guida",
        "english": "guide",
        "pos": "noun (f.)",
        "example_italian": "e io sarò tua guida",
        "example_english": "and I will be your guide",
        "note": (
            "From Old High German *wītan (to show the way), via the verb guidare. "
            "Unchanged in modern Italian. Borrowed into English as 'guide' (via Old French)."
        ),
    },

    # ─── Function words ───────────────────────────────────────────────────────

    # Articles
    {
        "id": "art_il",
        "italian": "il / lo / l'",
        "english": "the (m. sg.)",
        "pos": "definite article (m. sg.)",
        "example_italian": "il cor compunto",
        "example_english": "the heart pierced",
        "note": (
            "Three allomorphs: il before most consonants, lo before s+consonant or z, "
            "l' before vowels. Plural: i (from il), gli (from lo/l'). "
            "In Dante, li often stands where modern Italian uses i: "
            "a li occhi (line 62), li antichi spiriti (line 116)."
        ),
        "category": "function",
    },
    {
        "id": "art_la",
        "italian": "la / l'",
        "english": "the (f. sg.)",
        "pos": "definite article (f. sg.)",
        "example_italian": "la diritta via era smarrita",
        "example_english": "the straight way was lost",
        "note": (
            "Feminine singular: la before consonants, l' before vowels. "
            "Plural: le. So: la selva, la via, la paura, la notte — all feminine."
        ),
        "category": "function",
    },
    {
        "id": "art_li",
        "italian": "li",
        "english": "the (m. pl.)",
        "pos": "definite article (m. pl.)",
        "example_italian": "dinanzi a li occhi mi si fu offerto",
        "example_english": "before my eyes there was offered to me",
        "note": (
            "Medieval and poetic plural article for masculine nouns, equivalent to modern i "
            "(or gli before vowels/s+cons./z). Dante uses li throughout: "
            "li parenti miei (line 68), li antichi spiriti (line 116). "
            "Modern Italian: i parenti miei, gli antichi spiriti."
        ),
        "category": "function",
    },
    {
        "id": "art_le",
        "italian": "le",
        "english": "the (f. pl.)",
        "pos": "definite article (f. pl.)",
        "example_italian": "guardai in alto e vidi le sue spalle",
        "example_english": "I looked up and saw its shoulders",
        "note": (
            "Feminine plural article, identical in form to the singular la (before consonants). "
            "le spalle (the shoulders), le stelle (the stars), le vene e i polsi (line 90)."
        ),
        "category": "function",
    },

    # Contracted prepositions
    {
        "id": "del",
        "italian": "del",
        "english": "of the (m. sg.)",
        "pos": "contracted preposition (di + il)",
        "example_italian": "nel mezzo del cammin di nostra vita",
        "example_english": "in the middle of the journey of our life",
        "note": (
            "Contraction of di + il. Full paradigm: del (m.sg.), dello (s+cons./z), "
            "della (f.sg.), dell' (before vowels), dei (m.pl.), degli (m.pl. before s+cons./z/vowel), "
            "delle (f.pl.). In Dante de' often appears for dei: de' raggi (line 17)."
        ),
        "category": "function",
    },
    {
        "id": "nel",
        "italian": "nel",
        "english": "in the (m. sg.)",
        "pos": "contracted preposition (in + il)",
        "example_italian": "nel mezzo del cammin",
        "example_english": "in the middle of the journey",
        "note": (
            "Contraction of in + il. Full paradigm mirrors del: "
            "nel/nello/nella/nell'/nei/negli/nelle. "
            "Nel mezzo opens the poem; nel pensier (line 6), nel lago del cor (line 20)."
        ),
        "category": "function",
    },
    {
        "id": "al",
        "italian": "al",
        "english": "to the, at the (m. sg.)",
        "pos": "contracted preposition (a + il)",
        "example_italian": "al piè d'un colle giunto",
        "example_english": "arrived at the foot of a hill",
        "note": (
            "Contraction of a + il. Full paradigm: al/allo/alla/all'/ai/agli/alle. "
            "Expresses both location (at: al piè) and direction (to). "
            "Al cominciar de l'erta (line 31): at the beginning of the steep."
        ),
        "category": "function",
    },

    # Prepositions
    {
        "id": "prep_di",
        "italian": "di",
        "english": "of, from",
        "pos": "preposition",
        "example_italian": "nel mezzo del cammin di nostra vita",
        "example_english": "in the middle of the journey of our life",
        "note": (
            "From Latin de. The most frequent preposition in Italian. "
            "Core uses: possession/specification (cammin di nostra vita), "
            "origin (di Troia), partitive (di paura). "
            "Before a definite article contracts: di + il = del, di + la = della, etc. "
            "Reduced to d' before a vowel: d'un colle."
        ),
        "category": "function",
    },
    {
        "id": "prep_a",
        "italian": "a",
        "english": "to, at",
        "pos": "preposition",
        "example_italian": "«Miserere di me» gridai a lui",
        "example_english": "\"Have mercy on me,\" I cried out to him",
        "note": (
            "From Latin ad. Core uses: direction (venire a Roma), location (a Roma), "
            "indirect object (gridai a lui). "
            "Before the definite article contracts: a + il = al, a + la = alla, etc."
        ),
        "category": "function",
    },
    {
        "id": "prep_per",
        "italian": "per",
        "english": "through, for, by, in order to",
        "pos": "preposition",
        "example_italian": "mi ritrovai per una selva oscura",
        "example_english": "I came to myself in a dark wood",
        "note": (
            "From Latin per (through). Multiple uses in the same canto: "
            "spatial (per una selva = through/in a wood), "
            "causal (per paura = because of fear), "
            "purpose (per trattar = in order to treat, line 8). "
            "Does not contract with the article."
        ),
        "category": "function",
    },
    {
        "id": "prep_con",
        "italian": "con",
        "english": "with",
        "pos": "preposition",
        "example_italian": "la notte ch'i' passai con tanta pieta",
        "example_english": "the night that I passed with such great pity",
        "note": (
            "From Latin cum. Does not regularly contract with articles in Dante "
            "(modern col = con + il exists but is optional). "
            "Con la test'alta (line 47): with head held high."
        ),
        "category": "function",
    },
    {
        "id": "prep_da",
        "italian": "da",
        "english": "from, by",
        "pos": "preposition",
        "example_italian": "aiutami da lei, famoso saggio",
        "example_english": "help me against her, famous sage",
        "note": (
            "From Latin de + ab, merged in Vulgar Latin. Core uses: separation/origin (from), "
            "agent in passive constructions (by). Here da lei means 'from/against her'. "
            "Before articles: dal, dalla, dall', dai, dagli, dalle."
        ),
        "category": "function",
    },
    {
        "id": "prep_in",
        "italian": "in",
        "english": "in, into",
        "pos": "preposition",
        "example_italian": "guardai in alto e vidi le sue spalle",
        "example_english": "I looked up high and saw its shoulders",
        "note": (
            "From Latin in. Expresses location (in the forest) and direction (into). "
            "Before the definite article contracts: in + il = nel, in + la = nella, etc. "
            "In alto: up high (alto = high, used as an adverb here)."
        ),
        "category": "function",
    },

    # Conjunctions
    {
        "id": "conj_che",
        "italian": "che",
        "english": "that; which, who; than",
        "pos": "conjunction / relative pronoun",
        "example_italian": "che nel pensier rinova la paura",
        "example_english": "which in the very thought renews the fear",
        "note": (
            "The most versatile word in Italian, from Latin quod/qui/quia. "
            "As relative pronoun (which, who): che rinova = which renews. "
            "As subordinating conjunction (that): after verbs of saying, thinking, feeling. "
            "As comparative (than): più … che. "
            "Not to be confused with ché (grave accent), which is causal."
        ),
        "category": "function",
    },
    {
        "id": "conj_ché",
        "italian": "ché",
        "english": "because, for",
        "pos": "conjunction (causal)",
        "example_italian": "ché la diritta via era smarrita",
        "example_english": "for the straight way was lost",
        "note": (
            "Causal conjunction, from Latin quia. Always written with grave accent "
            "to distinguish it from che (relative/subordinating). "
            "Equivalent to perché or poiché in modern Italian. "
            "Appears three times in Canto I: lines 3, 15, 94."
        ),
        "category": "function",
    },
    {
        "id": "conj_e",
        "italian": "e / ed",
        "english": "and",
        "pos": "conjunction (copulative)",
        "example_italian": "guardai in alto e vidi le sue spalle",
        "example_english": "I looked up and saw its shoulders",
        "note": (
            "From Latin et. Ed is the form used before words beginning with e- "
            "(or sometimes other vowels) to avoid hiatus: ed ecco (line 31), ed una lupa (line 49). "
            "The alternation e/ed mirrors the o/od pattern."
        ),
        "category": "function",
    },
    {
        "id": "conj_ma",
        "italian": "ma",
        "english": "but",
        "pos": "conjunction (adversative)",
        "example_italian": "ma per trattar del ben ch'i' vi trovai",
        "example_english": "but in order to treat of the good that I found there",
        "note": (
            "From Latin magis (more, rather). Adversative conjunction, unchanged in modern Italian. "
            "Marks a pivot or contrast. In line 8 it turns from recalling the horror "
            "to speaking of the good Dante found in the journey."
        ),
        "category": "function",
    },
    {
        "id": "conj_o",
        "italian": "o / od",
        "english": "or",
        "pos": "conjunction (disjunctive)",
        "example_italian": "qual che tu sii, od ombra od omo vero",
        "example_english": "whatever you are, either shade or real man",
        "note": (
            "From Latin aut. Od is used before vowels to avoid hiatus: "
            "od ombra od omo (or shade or man). "
            "Same pattern as e/ed. Modern Italian keeps the same rule (optional)."
        ),
        "category": "function",
    },
    {
        "id": "conj_se",
        "italian": "se",
        "english": "if",
        "pos": "conjunction (conditional)",
        "example_italian": "se vuo' campar d'esto loco selvaggio",
        "example_english": "if you wish to escape this savage place",
        "note": (
            "From Latin si. Introduces conditional clauses. "
            "In real conditions the verb is indicative; in hypothetical ones, subjunctive. "
            "Not to be confused with the reflexive pronoun si (oneself)."
        ),
        "category": "function",
    },
    {
        "id": "conj_poi",
        "italian": "poi / poi che",
        "english": "then; after, since",
        "pos": "adverb / conjunction",
        "example_italian": "Ma poi ch'i' fui al piè d'un colle giunto",
        "example_english": "But when I had arrived at the foot of a hill",
        "note": (
            "From Latin post (after, behind). As adverb: then, afterwards. "
            "As conjunction poi che (after, since, once): poi ch'i' = poi che io. "
            "The ch' is che + elision before a vowel. "
            "Modern Italian: poi che → poiché (because, since)."
        ),
        "category": "function",
    },
    {
        "id": "conj_mentre",
        "italian": "mentre / mentre che",
        "english": "while",
        "pos": "conjunction (temporal)",
        "example_italian": "Mentre ch'i' rovinava in basso loco",
        "example_english": "While I was rushing down to a low place",
        "note": (
            "From Latin dum interim (meanwhile). Unchanged in modern Italian. "
            "Mentre che is the fuller medieval form (= mentre + che). "
            "Ch'i' = che io: 'while I'. The imperfect rovinava marks ongoing action."
        ),
        "category": "function",
    },
    {
        "id": "conj_quando",
        "italian": "quando",
        "english": "when",
        "pos": "conjunction / adverb (temporal)",
        "example_italian": "Quando vidi costui nel gran diserto",
        "example_english": "When I saw him in that great wasteland",
        "note": (
            "From Latin quando. Unchanged in modern Italian. "
            "As temporal conjunction it governs indicative (past fact) or subjunctive (hypothetical). "
            "Line 39: quando l'amor divino / mosse — when divine love first moved."
        ),
        "category": "function",
    },

    # Pronouns
    {
        "id": "pron_mi",
        "italian": "mi",
        "english": "me, to me; myself",
        "pos": "pronoun (1st pers. sg. unstressed clitic)",
        "example_italian": "mi ritrovai per una selva oscura",
        "example_english": "I came to myself in a dark wood",
        "note": (
            "Unstressed (clitic) pronoun, 1st person singular. Three functions: "
            "direct object (mi vide, he saw me), "
            "indirect object (mi disse, he said to me), "
            "reflexive (mi ritrovai, I found myself). "
            "Precedes the verb. Stressed/disjunctive form: me."
        ),
        "category": "function",
    },
    {
        "id": "pron_si",
        "italian": "si",
        "english": "oneself; each other",
        "pos": "pronoun (reflexive clitic, 3rd pers.)",
        "example_italian": "si volse a retro a rimirar lo passo",
        "example_english": "turned back to look again at the pass",
        "note": (
            "Reflexive clitic for 3rd person (sg. and pl.). "
            "Si volse: turned himself/itself. "
            "Also forms the passive/impersonal: mi si fu offerto (was offered to me, line 62). "
            "Not to be confused with sì (so, yes) or se (if)."
        ),
        "category": "function",
    },
    {
        "id": "pron_cui",
        "italian": "cui",
        "english": "whom, which, whose",
        "pos": "relative pronoun (invariable)",
        "example_italian": "tu se' solo colui da cu' io tolsi",
        "example_english": "you alone are the one from whom I took",
        "note": (
            "Invariable relative pronoun used after a preposition: "
            "da cui (from whom), a cui (to whom), di cui (of whom/whose). "
            "In the text cu' is cui with elision before a vowel (cu' io). "
            "Without a preposition, che is used instead (who, which)."
        ),
        "category": "function",
    },
    {
        "id": "pron_chi",
        "italian": "chi",
        "english": "who; whoever, he who",
        "pos": "relative / interrogative pronoun",
        "example_italian": "chi per lungo silenzio parea fioco",
        "example_english": "one who seemed faint from long silence",
        "note": (
            "Indefinite-relative pronoun: who, whoever, he who. Refers only to persons. "
            "For things or after an antecedent, che is used. "
            "Chi … parea: 'one who seemed'. "
            "Also interrogative: chi sei? (who are you?). Invariable."
        ),
        "category": "function",
    },
    {
        "id": "pron_costui",
        "italian": "costui",
        "english": "this one, he, that man",
        "pos": "demonstrative pronoun (m. sg.)",
        "example_italian": "Quando vidi costui nel gran diserto",
        "example_english": "When I saw him in that great wasteland",
        "note": (
            "Demonstrative pronoun for a person nearby or just mentioned, from Latin ecce + istui. "
            "Medieval Italian has a three-way system: questi (near), costui (at a middle distance), "
            "colui (far). Colui appears in line 129: colui cu' ivi elegge. "
            "Modern Italian collapses these into questo/quello."
        ),
        "category": "function",
    },

    # Adverbs
    {
        "id": "adv_non",
        "italian": "non",
        "english": "not",
        "pos": "adverb (negation)",
        "example_italian": "Io non so ben ridir com'i' v'intrai",
        "example_english": "I do not well know how to tell how I entered there",
        "note": (
            "From Latin non. Placed directly before the verb it negates. "
            "Medieval Italian uses expressive double negation: "
            "non lasciò già mai (line 27) = never ever left "
            "(già and mai both reinforce the negation)."
        ),
        "category": "function",
    },
    {
        "id": "adv_già",
        "italian": "già",
        "english": "already; once, ever",
        "pos": "adverb",
        "example_italian": "vestite già de' raggi del pianeta",
        "example_english": "already clothed in the rays of the planet",
        "note": (
            "From Latin iam. Three main uses in Canto I: "
            "1) already (line 17: vestite già = already clothed); "
            "2) once, formerly (line 67: omo già fui = man once I was); "
            "3) reinforcing negation (line 27: non lasciò già mai). "
            "Unchanged in modern Italian."
        ),
        "category": "function",
    },
    {
        "id": "adv_mai",
        "italian": "mai",
        "english": "never (with non); ever",
        "pos": "adverb",
        "example_italian": "che non lasciò già mai persona viva",
        "example_english": "that never yet left anyone alive",
        "note": (
            "From Latin magis (more) → ever, at any time. "
            "With non: never (non … mai). Without non: ever. "
            "Non lasciò già mai: triple reinforcement (non + già + mai) common in medieval Italian. "
            "Unchanged in modern Italian."
        ),
        "category": "function",
    },
    {
        "id": "adv_sì",
        "italian": "sì",
        "english": "so, thus; yes",
        "pos": "adverb",
        "example_italian": "sì che 'l piè fermo sempre era 'l più basso",
        "example_english": "so that the firm foot was always the lower",
        "note": (
            "From Latin sic (thus, in this way). Two main uses: "
            "1) degree/manner: sì che = so that, in such a way that; "
            "2) affirmation (yes) — the use that survives as the standard sì in modern Italian. "
            "Not to be confused with si (reflexive pronoun) or se (if)."
        ),
        "category": "function",
    },
    {
        "id": "adv_là",
        "italian": "là",
        "english": "there",
        "pos": "adverb (place)",
        "example_italian": "là dove terminava quella valle",
        "example_english": "there where that valley ended",
        "note": (
            "From Latin illac (from that direction). Accent distinguishes it from la (article). "
            "Là dove = there where, introduces a relative clause of place. "
            "Contrasts with qui/qua (here) and distinguishes more distant reference than lì."
        ),
        "category": "function",
    },

    # Interjections
    {
        "id": "interj_ahi",
        "italian": "ahi",
        "english": "ah!, alas!",
        "pos": "interjection",
        "example_italian": "Ahi quanto a dir qual era è cosa dura",
        "example_english": "Ah, how hard a thing it is to say",
        "note": (
            "Exclamation of pain or dismay, from Latin. Common in Dante throughout the Commedia. "
            "Often strengthened to ahimè (alas, to me). "
            "Quanto here is an exclamative adverb: 'how (greatly), how much'."
        ),
        "category": "function",
    },
    {
        "id": "interj_ecco",
        "italian": "ecco",
        "english": "behold!, here is/are, lo!",
        "pos": "presentative adverb",
        "example_italian": "Ed ecco, quasi al cominciar de l'erta",
        "example_english": "And behold, almost at the beginning of the steep",
        "note": (
            "From Latin ecce (look!, here!). Unchanged in modern Italian. "
            "Presentative: draws attention to something suddenly appearing. "
            "Ed ecco is a dramatic formula; it introduces the leopard as a sudden apparition."
        ),
        "category": "function",
    },

    # ─── Words from lines 1–9 not yet covered above ───────────────────────────

    # Verbs
    {
        "id": "essere",
        "italian": "essere",
        "english": "to be",
        "pos": "verb (essere — key forms)",
        "example_italian": "ché la diritta via era smarrita",
        "example_english": "for the straight way was lost",
        "note": (
            "The most important Italian verb. Key forms in lines 1–9: "
            "è (3rd sg. present: is), era (3rd sg. imperfect: was). "
            "Other forms in Canto I: fu (3rd sg. passato remoto: was, line 19), "
            "se' / sei (2nd sg. present: you are, line 85), fui (1st sg. p.r.: I was, line 67). "
            "Era smarrita = imperfect passive: 'was lost / had been lost'."
        ),
        "conjugations": {
            "present":        {"label": "Presente",        "forms": ["sono", "sei", "è",   "siamo",   "siete",   "sono"]},
            "imperfect":      {"label": "Imperfetto",      "forms": ["ero",  "eri", "era",  "eravamo", "eravate", "erano"]},
            "passato_remoto": {"label": "Passato remoto",  "forms": ["fui",  "fosti", "fu", "fummo",   "foste",   "furono"]},
            "future":         {"label": "Futuro",          "forms": ["sarò", "sarai", "sarà", "saremo", "sarete", "saranno"]},
        },
    },
    {
        "id": "ritrovai",
        "italian": "ritrovai",
        "english": "I found myself again; I came to myself",
        "pos": "verb (1st pers. sg. passato remoto of ritrovarsi)",
        "example_italian": "mi ritrovai per una selva oscura",
        "example_english": "I came to myself in a dark wood",
        "note": (
            "Passato remoto of ritrovarsi (reflexive: to find oneself again, to come to). "
            "Mi is the reflexive clitic (myself). Ri- adds the sense of 'back / again'. "
            "Trovarsi = to find oneself; ritrovarsi = to regain one's bearings."
        ),
        "conjugations": {
            "present":        {"label": "Presente (ritrovarsi)",       "forms": ["mi ritrovo", "ti ritrovi", "si ritrova", "ci ritroviamo", "vi ritrovate", "si ritrovano"]},
            "passato_remoto": {"label": "Passato remoto (ritrovarsi)", "forms": ["mi ritrovai", "ti ritrovasti", "si ritrovò", "ci ritrovammo", "vi ritrovaste", "si ritrovarono"]},
        },
    },
    {
        "id": "trovare",
        "italian": "trovare",
        "english": "to find",
        "pos": "verb (trovare)",
        "example_italian": "ma per trattar del ben ch'i' vi trovai",
        "example_english": "but in order to speak of the good that I found there",
        "note": (
            "From Latin *tropare (to compose, find) via Old Provençal trobar. "
            "Trovai is 1st person singular passato remoto (I found). "
            "Cf. ritrovai (line 2, reflexive: I found myself again). "
            "Related to English 'troubadour' (trovatore). Unchanged in modern Italian."
        ),
        "conjugations": {
            "present":        {"label": "Presente",       "forms": ["trovo", "trovi", "trova", "troviamo", "trovate", "trovano"]},
            "passato_remoto": {"label": "Passato remoto", "forms": ["trovai", "trovasti", "trovò", "trovammo", "trovaste", "trovarono"]},
        },
    },
    {
        "id": "dire",
        "italian": "dire",
        "english": "to say, to tell",
        "pos": "verb (dire)",
        "example_italian": "Ahi quanto a dir qual era è cosa dura",
        "example_english": "Ah, how hard a thing it is to tell what it was",
        "note": (
            "From Latin dicere. Irregular verb. "
            "Dir is the apocopated infinitive (used in verse for metre). "
            "Dirò (line 9) is 1st sg. future: I will tell. "
            "Io non so ben ridir (line 10): I do not well know how to re-tell. "
            "Related to English 'diction', 'dictate', 'indicate'."
        ),
        "conjugations": {
            "present": {"label": "Presente", "forms": ["dico", "dici", "dice", "diciamo", "dite", "dicono"]},
            "future":  {"label": "Futuro",   "forms": ["dirò", "dirai", "dirà", "diremo", "direte", "diranno"]},
        },
    },
    {
        "id": "rinova",
        "italian": "rinova",
        "english": "renews",
        "pos": "verb (3rd pers. sg. present of rinnovare)",
        "example_italian": "che nel pensier rinova la paura",
        "example_english": "which in the very thought renews the fear",
        "note": (
            "3rd person singular present of rinnovare (to renew). "
            "Ri- adds 'again': novare (to make new) → rinnovare. "
            "The subject is che referring back to the selva: "
            "the wood renews the fear even in thought, even in memory."
        ),
        "conjugations": {
            "present": {"label": "Presente (rinnovare)", "forms": ["rinnovo", "rinnovi", "rinnova", "rinnoviamo", "rinnovate", "rinnovano"]},
        },
    },
    {
        "id": "trattare",
        "italian": "trattare",
        "english": "to treat, to speak of, to deal with",
        "pos": "verb (trattare)",
        "example_italian": "ma per trattar del ben ch'i' vi trovai",
        "example_english": "but in order to speak of the good that I found there",
        "note": (
            "From Latin tractare (to handle, manage). "
            "Trattar is the apocopated infinitive. "
            "Per trattar = in order to speak of (per + infinitive = purpose). "
            "Unchanged in modern Italian."
        ),
        "conjugations": {
            "present": {"label": "Presente", "forms": ["tratto", "tratti", "tratta", "trattiamo", "trattate", "trattano"]},
        },
    },
    {
        "id": "avere",
        "italian": "avere",
        "english": "to have",
        "pos": "verb (avere — key forms)",
        "example_italian": "dirò de l'altre cose ch'i' v'ho scorte",
        "example_english": "I will tell of the other things that I have seen there",
        "note": (
            "From Latin habere. Key forms: ho (I have), hai (you have), ha (he/she has). "
            "V'ho = vi ho (I have there). Used as auxiliary to form compound tenses: "
            "v'ho scorte = I have (there) seen/made out (past participle scorte). "
            "Unchanged in modern Italian."
        ),
        "conjugations": {
            "present":        {"label": "Presente",       "forms": ["ho",   "hai",    "ha",   "abbiamo", "avete",   "hanno"]},
            "passato_remoto": {"label": "Passato remoto", "forms": ["ebbi", "avesti", "ebbe", "avemmo",  "aveste",  "ebbero"]},
        },
    },
    {
        "id": "scorgere",
        "italian": "scorgere",
        "english": "to perceive, to see, to make out",
        "pos": "verb (scorgere)",
        "example_italian": "dirò de l'altre cose ch'i' v'ho scorte",
        "example_english": "I will tell of the other things that I have seen there",
        "note": (
            "Scorte is the feminine plural past participle, agreeing with cose (f. pl.). "
            "Scorgere implies perceiving or discerning something, often at a distance. "
            "V'ho scorte = I have seen/made out there. Still used in modern Italian."
        ),
        "conjugations": {
            "present": {"label": "Presente", "forms": ["scorgo", "scorgi", "scorge", "scorgiamo", "scorgete", "scorgono"]},
            "past_participle": {"label": "Participio passato", "forms": ["scòrto", "scòrta", "scòrti", "scòrte"]},
        },
    },

    # Nouns
    {
        "id": "cosa",
        "italian": "cosa",
        "english": "thing",
        "pos": "noun (f.)",
        "example_italian": "quanto a dir qual era è cosa dura",
        "example_english": "how hard a thing it is to tell what it was",
        "note": (
            "From Latin causa (cause, reason → thing). Plural: cose. "
            "È cosa dura = it is a hard thing. "
            "In modern Italian cosa also means 'what' in questions (cosa fai? = what are you doing?). "
            "Unchanged in modern Italian."
        ),
    },
    {
        "id": "pensier",
        "italian": "pensiero",
        "english": "thought",
        "pos": "noun (m.)",
        "example_italian": "che nel pensier rinova la paura",
        "example_english": "which in the very thought renews the fear",
        "note": (
            "Apocopated form of pensiero (loss of final -o before a following consonant). "
            "From pensare (to think), from Latin pensare. "
            "Nel pensier = in (the very) thought, just by thinking of it. "
            "Pensieri (pl.) = thoughts; Dante uses it again at line 57."
        ),
    },
    {
        "id": "ben",
        "italian": "bene / ben",
        "english": "good; well",
        "pos": "noun (m.) / adverb",
        "example_italian": "ma per trattar del ben ch'i' vi trovai",
        "example_english": "but in order to speak of the good that I found there",
        "note": (
            "From Latin bonum (noun) and bene (adverb). "
            "As noun (il bene): the good, the benefit. Del ben = of the good. "
            "As adverb: well (io non so ben ridir, line 10: I do not well know how to tell). "
            "Ben (apocopated) used before consonants in verse."
        ),
    },

    # Adjectives
    {
        "id": "nostra",
        "italian": "nostro / nostra",
        "english": "our",
        "pos": "possessive adjective (1st pers. pl.)",
        "example_italian": "nel mezzo del cammin di nostra vita",
        "example_english": "in the middle of the journey of our life",
        "note": (
            "From Latin noster. Agrees with the noun it modifies: "
            "nostro (m. sg.), nostra (f. sg.), nostri (m. pl.), nostre (f. pl.). "
            "Nostra vita = our life (vita is feminine). "
            "In the opening line, nostra includes all humanity in Dante's journey. "
            "Unchanged in modern Italian."
        ),
    },
    {
        "id": "duro",
        "italian": "duro / dura",
        "english": "hard, difficult",
        "pos": "adjective",
        "example_italian": "quanto a dir qual era è cosa dura",
        "example_english": "how hard a thing it is to tell what it was",
        "note": (
            "From Latin durus (hard, tough). Dura (feminine) agrees with cosa (f.). "
            "Metaphorical: hard = difficult, heavy. "
            "Related to English 'durable', 'endure', 'duration'. Unchanged in modern Italian."
        ),
    },
    {
        "id": "esta",
        "italian": "esta / esto",
        "english": "this (archaic/poetic)",
        "pos": "demonstrative adjective (f. sg.)",
        "example_italian": "esta selva selvaggia e aspra e forte",
        "example_english": "this wood savage and harsh and fierce",
        "note": (
            "Archaic/poetic form of questa (this, feminine). From Latin ista. "
            "Dante prefers esta/esto in verse for metrical reasons. "
            "Modern Italian: questa selva. "
            "Esto loco selvaggio (line 93) = this savage place."
        ),
    },
    {
        "id": "selvaggio",
        "italian": "selvaggio / selvaggia",
        "english": "savage, wild",
        "pos": "adjective",
        "example_italian": "esta selva selvaggia e aspra e forte",
        "example_english": "this wood savage and harsh and fierce",
        "note": (
            "Derived from selva + -aggio, from Latin silvaticus (of the forest). "
            "Selvaggia (feminine) agrees with selva (f.). "
            "The line echoes the noun: selva selvaggia = wild wood (the adjective shares its root). "
            "Related to English 'savage' via Old French sauvage, from Latin silvaticus."
        ),
    },
    {
        "id": "aspro",
        "italian": "aspro / aspra",
        "english": "harsh, rough",
        "pos": "adjective",
        "example_italian": "esta selva selvaggia e aspra e forte",
        "example_english": "this wood savage and harsh and fierce",
        "note": (
            "From Latin asper (rough, harsh). Aspra (feminine) agrees with selva (f.). "
            "The three adjectives selvaggia, aspra, forte build up an overwhelming picture "
            "of the wood. Related to English 'asperity'. Unchanged in modern Italian."
        ),
    },
    {
        "id": "forte",
        "italian": "forte",
        "english": "fierce, strong; hard",
        "pos": "adjective / adverb",
        "example_italian": "esta selva selvaggia e aspra e forte",
        "example_english": "this wood savage and harsh and fierce",
        "note": (
            "From Latin fortis (strong, brave). The climax of the three-adjective description. "
            "As adjective: strong, fierce. As adverb: strongly, hard. "
            "Related to English 'force', 'fort', 'comfort'. Unchanged in modern Italian."
        ),
    },
    {
        "id": "amaro",
        "italian": "amaro / amara",
        "english": "bitter",
        "pos": "adjective",
        "example_italian": "Tant'è amara che poco è più morte",
        "example_english": "So bitter is it that death is scarcely more",
        "note": (
            "From Latin amarus (bitter). Amara (feminine) agrees with selva understood. "
            "Tant'è amara: so bitter is it. The predicate adjective follows è. "
            "Related to English 'amaretto', 'amaranth'. Unchanged in modern Italian."
        ),
    },
    {
        "id": "altro",
        "italian": "altro / altra",
        "english": "other, else; another",
        "pos": "adjective / pronoun",
        "example_italian": "dirò de l'altre cose ch'i' v'ho scorte",
        "example_english": "I will tell of the other things that I have seen there",
        "note": (
            "From Latin alter (the other of two). Altre is feminine plural, agreeing with cose. "
            "L'altre = le altre (elision of le before a vowel). De l'altre = of the others. "
            "Altro viaggio (line 91): another way. Unchanged in modern Italian."
        ),
    },

    # Adverbs and pronouns (function-word-like)
    {
        "id": "quanto",
        "italian": "quanto",
        "english": "how much; as much; how",
        "pos": "adverb / adjective / pronoun",
        "example_italian": "Ahi quanto a dir qual era è cosa dura",
        "example_english": "Ah, how hard a thing it is to tell what it was",
        "note": (
            "From Latin quantum. As exclamative adverb: how (much). "
            "Quanto è dura = how hard it is. "
            "As relative pronoun: as much as. As adjective it agrees in gender/number. "
            "Unchanged in modern Italian."
        ),
        "category": "function",
    },
    {
        "id": "qual",
        "italian": "quale / qual",
        "english": "which, what, as",
        "pos": "adjective / pronoun",
        "example_italian": "Ahi quanto a dir qual era è cosa dura",
        "example_english": "Ah, how hard a thing it is to tell what it was",
        "note": (
            "From Latin qualis (of what kind). Qual is the apocopated form used before consonants. "
            "Dir qual era = to tell what it was (qual = what, of what kind). "
            "Also used in comparisons: tal … qual = such … as (line 55). "
            "Unchanged in modern Italian."
        ),
        "category": "function",
    },
    {
        "id": "tanto",
        "italian": "tanto / tant'",
        "english": "so much, so",
        "pos": "adverb / adjective",
        "example_italian": "Tant'è amara che poco è più morte",
        "example_english": "So bitter is it that death is scarcely more",
        "note": (
            "From Latin tantus. Tant'è = tanto è (elision before è): so much is it, so bitter is it. "
            "Tanto … che = so … that (result clause). "
            "Unchanged in modern Italian."
        ),
        "category": "function",
    },
    {
        "id": "poco",
        "italian": "poco",
        "english": "little, a little; scarcely",
        "pos": "adverb / adjective",
        "example_italian": "Tant'è amara che poco è più morte",
        "example_english": "So bitter is it that death is scarcely more",
        "note": (
            "From Latin paucus (few, little). As adverb: a little, scarcely "
            "(poco più morte = death is little more, i.e. scarcely worse than this wood). "
            "Un poco = a little. Unchanged in modern Italian."
        ),
        "category": "function",
    },
    {
        "id": "piu",
        "italian": "più",
        "english": "more",
        "pos": "adverb / adjective",
        "example_italian": "Tant'è amara che poco è più morte",
        "example_english": "So bitter is it that death is scarcely more",
        "note": (
            "From Latin plus (more). Forms comparatives: più amara = more bitter. "
            "Non … più = no longer. Il più = the most. "
            "Più … che / di = more … than. Unchanged in modern Italian."
        ),
        "category": "function",
    },
    {
        "id": "adv_vi",
        "italian": "vi",
        "english": "there; to you; yourselves",
        "pos": "adverb of place / pronoun clitic (2nd pers. pl.)",
        "example_italian": "ma per trattar del ben ch'i' vi trovai",
        "example_english": "but in order to speak of the good that I found there",
        "note": (
            "As adverb (Latin ibi): there, in that place. Vi trovai = I found there. "
            "V' is the elided form before a vowel: v'ho scorte (line 9), v'intrai (line 10). "
            "Also a clitic pronoun: 2nd person plural (to you / yourselves). "
            "Context determines which: after a verb of motion or 'trovare', vi = there."
        ),
        "category": "function",
    },

    # Indefinite article
    {
        "id": "art_un",
        "italian": "un / una",
        "english": "a, an",
        "pos": "indefinite article",
        "example_italian": "mi ritrovai per una selva oscura",
        "example_english": "I came to myself in a dark wood",
        "note": (
            "Forms: un (m., before most consonants and vowels), uno (m., before s+cons./z/gn), "
            "una (f., before consonants), un' (f., before vowels). "
            "Una selva = a wood (selva is feminine). Unchanged in modern Italian."
        ),
        "category": "function",
    },
]

# ─── Word-order exercises ──────────────────────────────────────────────────────
# tokens: the line split as it will be displayed; checker strips punctuation.

WORD_ORDER = [
    {
        "id": "wo1",
        "line_number": 1,
        "tokens": ["Nel", "mezzo", "del", "cammin", "di", "nostra", "vita"],
        "translation": "In the middle of the journey of our life",
        "hint": "The first line of the entire poem. Del = di + il.",
    },
    {
        "id": "wo2",
        "line_number": 2,
        "tokens": ["mi", "ritrovai", "per", "una", "selva", "oscura,"],
        "translation": "I came to myself in a dark wood,",
        "hint": "Ritrovai is the passato remoto of ritrovarsi (reflexive: to find oneself). Mi is the reflexive pronoun.",
    },
    {
        "id": "wo3",
        "line_number": 3,
        "tokens": ["ché", "la", "diritta", "via", "era", "smarrita."],
        "translation": "for the straight way was lost.",
        "hint": "Ché = because, for. Era smarrita = pluperfect passive of smarrire.",
    },
    {
        "id": "wo4",
        "line_number": 16,
        "tokens": ["guardai", "in", "alto", "e", "vidi", "le", "sue", "spalle"],
        "translation": "I looked up high and saw its shoulders",
        "hint": "Guardai and vidi are both passato remoto. Sue spalle = its shoulders (spalle is plural of spalla).",
    },
    {
        "id": "wo5",
        "line_number": 19,
        "tokens": ["Allor", "fu", "la", "paura", "un", "poco", "queta,"],
        "translation": "Then the fear was a little quieted,",
        "hint": "Allor = allora (then). Queta is the predicate adjective, feminine agreeing with paura.",
    },
    {
        "id": "wo6",
        "line_number": 32,
        "tokens": ["una", "lonza", "leggera", "e", "presta", "molto,"],
        "translation": "a leopard, light and very swift,",
        "hint": "Presta = swift, ready. Leggera = light (feminine of leggero). Both adjectives modify lonza (f.).",
    },
    {
        "id": "wo7",
        "line_number": 62,
        "tokens": ["dinanzi", "a", "li", "occhi", "mi", "si", "fu", "offerto"],
        "translation": "before my eyes there was offered to me",
        "hint": "Dinanzi = before, in front of. Li is the medieval plural article (= i). Si fu offerto = passive reflexive.",
    },
    {
        "id": "wo8",
        "line_number": 73,
        "tokens": ["Poeta", "fui,", "e", "cantai", "di", "quel", "giusto"],
        "translation": "A poet was I, and I sang of that just",
        "hint": "Fui = I was (passato remoto of essere). Cantai = I sang. Poeta placed first for emphasis.",
    },
    {
        "id": "wo9",
        "line_number": 113,
        "tokens": ["che", "tu", "mi", "segua,", "e", "io", "sarò", "tua", "guida,"],
        "translation": "that you follow me, and I will be your guide,",
        "hint": "Segua is present subjunctive (that you follow). Sarò = I will be (future of essere).",
    },
    {
        "id": "wo10",
        "line_number": 136,
        "tokens": ["Allor", "si", "mosse,", "e", "io", "li", "tenni", "dietro."],
        "translation": "Then he moved on, and I kept close behind.",
        "hint": "Mosse = he moved (passato remoto of muoversi). Tenni dietro = kept behind, followed closely.",
    },
]

# ─── Translation exercises ─────────────────────────────────────────────────────

TRANSLATION = [
    {
        "id": "tr1",
        "lines": (1, 3),
        "prompt": (
            "In the middle of the journey of our life\n"
            "myself I found again in a wood dark,\n"
            "for the straight way was lost."
        ),
        "italian": (
            "Nel mezzo del cammin di nostra vita\n"
            "mi ritrovai per una selva oscura,\n"
            "ché la diritta via era smarrita."
        ),
        "english": (
            "In the middle of the journey of our life\n"
            "I came to myself in a dark wood,\n"
            "for the straight way was lost."
        ),
        "note": (
            "Mi ritrovai is reflexive (ritrovarsi): literally 'I found myself again'. "
            "Ché (with accent) = because/for, not to be confused with che (that/which). "
            "Diritta via and verace via (line 12) are parallel phrases for the right path."
        ),
    },
    {
        "id": "tr2",
        "lines": (4, 6),
        "prompt": (
            "Ah how much to say what it was is a thing hard\n"
            "this wood savage and harsh and fierce\n"
            "that in the thought renews the fear!"
        ),
        "italian": (
            "Ahi quanto a dir qual era è cosa dura\n"
            "esta selva selvaggia e aspra e forte\n"
            "che nel pensier rinova la paura!"
        ),
        "english": (
            "Ah, how hard a thing it is to say\n"
            "what that wood was, so savage and harsh and dense,\n"
            "which in the very thought renews the fear!"
        ),
        "note": (
            "Esta is the archaic/poetic demonstrative (= questa, this). "
            "Selvaggia echoes selva: the adjective derives from the same root (Latin silvaticus, of the woods). "
            "Rinova is present indicative: renews (not past tense)."
        ),
    },
    {
        "id": "tr3",
        "lines": (13, 18),
        "prompt": (
            "But when I at the foot of a hill arrived,\n"
            "there where ended that valley\n"
            "that had me with fear the heart pierced,\n"
            "I looked up high and saw its shoulders\n"
            "clothed already with the rays of the planet\n"
            "that leads straight others along every path;"
        ),
        "italian": (
            "Ma poi ch'i' fui al piè d'un colle giunto,\n"
            "là dove terminava quella valle\n"
            "che m'aveva di paura il cor compunto,\n"
            "guardai in alto e vidi le sue spalle\n"
            "vestite già de' raggi del pianeta\n"
            "che mena dritto altrui per ogni calle;"
        ),
        "english": (
            "But when I had arrived at the foot of a hill,\n"
            "there where that valley ended\n"
            "that had pierced my heart with fear,\n"
            "I looked up high and saw its shoulders\n"
            "already clothed in the rays of the planet\n"
            "that leads others straight along every path;"
        ),
        "note": (
            "Ch'i' = che io (that I). Giunto is a past participle used predicatively: 'arrived'. "
            "Compunto: from Latin compungere (to prick, pierce). De' = dei = di + i. "
            "Calle (path, lane) is an archaic word; modern Italian usually uses vicolo or cammino."
        ),
    },
    {
        "id": "tr4",
        "lines": (19, 21),
        "prompt": (
            "Then was the fear a little quieted,\n"
            "that in the lake of the heart had lasted to me\n"
            "the night that I had passed with such great pity."
        ),
        "italian": (
            "Allor fu la paura un poco queta,\n"
            "che nel lago del cor m'era durata\n"
            "la notte ch'i' passai con tanta pieta."
        ),
        "english": (
            "Then the fear was a little quieted,\n"
            "that had lasted in the lake of my heart\n"
            "through the night that I had passed with such great pity."
        ),
        "note": (
            "Queta is the predicate adjective (feminine: fu … queta), from quieta. "
            "M'era durata: reflexive pluperfect, literally 'had lasted to me'. "
            "Pieta (without accent) = pity, compassion; piéta (with accent) = piety."
        ),
    },
    {
        "id": "tr5",
        "lines": (31, 36),
        "prompt": (
            "And behold, almost at the beginning of the steep,\n"
            "a leopard light and swift very,\n"
            "that with hide spotted was covered;\n"
            "and not from before my face did it depart,\n"
            "rather it so much impeded my advance,\n"
            "that to turn back many times it was turned."
        ),
        "italian": (
            "Ed ecco, quasi al cominciar de l'erta,\n"
            "una lonza leggera e presta molto,\n"
            "che di pel macolato era coverta;\n"
            "e non mi si partia dinanzi al volto,\n"
            "anzi 'mpediva tanto il mio cammino,\n"
            "che fu per tornare più volte vòlto."
        ),
        "english": (
            "And behold, almost at the beginning of the steep,\n"
            "a leopard, light and very swift,\n"
            "that was covered with a spotted hide;\n"
            "and it did not depart from before my face,\n"
            "rather it so impeded my advance\n"
            "that many a time I turned back."
        ),
        "note": (
            "Ecco (behold, here is/are) is unchanged in modern Italian. "
            "Erta = steep slope, ascent; from Latin ērecta (raised). "
            "Macolato = spotted; from Latin macula (spot, stain). "
            "Vòlto: past participle of volgere (to turn), with the accent marking the stressed syllable."
        ),
    },
    {
        "id": "tr6",
        "lines": (61, 66),
        "prompt": (
            "While I was rushing down to a low place,\n"
            "before my eyes to me was offered\n"
            "one who from long silence seemed faint.\n"
            "When I saw him in the great wasteland,\n"
            "\"Have mercy on me\" I cried out to him,\n"
            "\"whatever you may be, either shade or real man!\""
        ),
        "italian": (
            "Mentre ch'i' rovinava in basso loco,\n"
            "dinanzi a li occhi mi si fu offerto\n"
            "chi per lungo silenzio parea fioco.\n"
            "Quando vidi costui nel gran diserto,\n"
            "«Miserere di me» gridai a lui,\n"
            "«qual che tu sii, od ombra od omo vero!»"
        ),
        "english": (
            "While I was rushing down to a low place,\n"
            "before my eyes there was offered to me\n"
            "one who seemed faint from long silence.\n"
            "When I saw him in that great wasteland,\n"
            "\"Have mercy on me,\" I cried out to him,\n"
            "\"whatever you are, either shade or real man!\""
        ),
        "note": (
            "Ch'i' = che io. Rovinava: imperfect of rovinare (to rush down, to tumble; from rovina, ruin). "
            "Fioco: faint, hoarse, dim; from Latin floccus (wisp, trifle) → weak, thin. "
            "Miserere is Latin: 'have mercy' (2nd pers. imperative of misereri). "
            "Omo = uomo (man); the o-form is archaic/poetic."
        ),
    },
    {
        "id": "tr7",
        "lines": (67, 75),
        "prompt": (
            "He answered me: \"Not man; man once I was,\n"
            "and my parents were Lombards,\n"
            "Mantuan by country both of them.\n"
            "I was born sub Julio, though it was late,\n"
            "and I lived at Rome under the good Augustus\n"
            "in the time of the gods false and lying.\n"
            "A poet was I, and I sang of that just\n"
            "son of Anchises who came from Troy,\n"
            "after the proud Ilion was burned.\""
        ),
        "italian": (
            "Rispuosemi: «Non omo, omo già fui,\n"
            "e li parenti miei furon lombardi,\n"
            "mantoani per patrïa ambedui.\n"
            "Nacqui sub Iulio, ancor che fosse tardi,\n"
            "e vissi a Roma sotto 'l buono Augusto\n"
            "nel tempo de li dèi falsi e bugiardi.\n"
            "Poeta fui, e cantai di quel giusto\n"
            "figliuol d'Anchise che venne di Troia,\n"
            "poi che 'l superbo Ilïón fu combusto."
        ),
        "english": (
            "He answered me: \"Not man; man once I was,\n"
            "and both my parents were Lombards,\n"
            "Mantuans by country, both of them.\n"
            "I was born sub Julio, though it was late,\n"
            "and I lived at Rome under the good Augustus,\n"
            "in the time of the false and lying gods.\n"
            "A poet was I, and I sang of that just\n"
            "son of Anchises who came from Troy,\n"
            "after proud Ilion was burned.\""
        ),
        "note": (
            "Rispuosemi: passato remoto of rispondere + mi (dative: to me). "
            "Sub Iulio: Latin ablative, 'under Julius (Caesar)'. Dante uses Latin for Roman historical figures. "
            "Ambedui = entrambi (both); archaic dual form. "
            "Combusto = burned; from Latin combustus (past participle of comburere). "
            "Dèi: the grave accent distinguishes dèi (gods, plural of dio) from dei (= di + i)."
        ),
    },
    {
        "id": "tr8",
        "lines": (79, 87),
        "prompt": (
            "\"Now are you that Virgil and that spring\n"
            "that you pour of speech so wide a river?\"\n"
            "I answered him with shame and face.\n"
            "\"O of the other poets honor and light,\n"
            "may avail me the long study and the great love\n"
            "that has made me search your volume.\n"
            "You are my master and my author,\n"
            "you alone are the one from whom I took\n"
            "the beautiful style that has brought me honor.\""
        ),
        "italian": (
            "«Or se' tu quel Virgilio e quella fonte\n"
            "che spandi di parlar sì largo fiume?»\n"
            "rispuos'io lui con vergogna e fronte.\n"
            "«O de li altri poeti onore e lume,\n"
            "vagliami 'l lungo studio e 'l grande amore\n"
            "che m'ha fatto cercar lo tuo volume.\n"
            "Tu se' lo mio maestro e 'l mio autore,\n"
            "tu se' solo colui da cu' io tolsi\n"
            "lo bello stilo che m'ha fatto onore."
        ),
        "english": (
            "\"Are you then that Virgil and that spring\n"
            "that pours forth so wide a river of speech?\"\n"
            "I answered him with bashful face.\n"
            "\"O honour and light of the other poets,\n"
            "may the long study and the great love avail me\n"
            "that have made me search your volume.\n"
            "You are my master and my author,\n"
            "you alone are the one from whom I took\n"
            "the beautiful style that has brought me honour.\""
        ),
        "note": (
            "Se' = sei (2nd pers. singular of essere); the apostrophe marks the dropped -i. "
            "'l = il (article, elided). Vagliami: present subjunctive of valere (to be worth) + mi (dative), "
            "expressing a wish: 'may it avail me'. "
            "Cu' = cui (whom, relative pronoun); the -i drops before a vowel. "
            "Lo is the archaic form of the article (= il) before certain consonants."
        ),
    },
    {
        "id": "tr9",
        "lines": (112, 120),
        "prompt": (
            "Wherefore for your good I think and judge\n"
            "that you follow me, and I will be your guide,\n"
            "and will lead you hence through an eternal place;\n"
            "and you will hear the desperate shrieks,\n"
            "you will see the ancient spirits suffering,\n"
            "that the second death each one cries out at;\n"
            "and you will see those who are content\n"
            "in the fire, because they hope to come,\n"
            "whenever it may be, to the blessed people;"
        ),
        "italian": (
            "Ond'io per lo tuo me' penso e discerno\n"
            "che tu mi segua, e io sarò tua guida,\n"
            "e trarrotti di qui per loco etterno;\n"
            "e udrai le disperate strida,\n"
            "vedrai li antichi spiriti dolenti,\n"
            "che la seconda morte ciascun grida;\n"
            "e vederai color che son contenti\n"
            "nel foco, perché speran di venire\n"
            "quando che sia a le beate genti;"
        ),
        "english": (
            "Wherefore I think and judge it best for you\n"
            "that you follow me, and I will be your guide,\n"
            "and will lead you hence through an eternal place;\n"
            "and you will hear desperate shrieks,\n"
            "you will see the ancient suffering spirits,\n"
            "each one crying out at the second death;\n"
            "and you will see those who are content\n"
            "in the fire, because they hope to come,\n"
            "whenever it may be, to the blessed people;"
        ),
        "note": (
            "Me' = meglio (better); apocopated comparative adverb. "
            "Trarrotti: future of trarre (to lead, draw) + ti (2nd pers. object) + -tti (assimilation). "
            "Strida: plural of strido (shriek, cry); archaic plural form. "
            "Segua: present subjunctive of seguire (to follow), expressing purpose/wish after che."
        ),
    },
    {
        "id": "tr10",
        "lines": (130, 136),
        "prompt": (
            "And I to him: \"Poet, I beseech you\n"
            "by that God whom you did not know,\n"
            "so that I may flee this evil and worse,\n"
            "that you lead me there where now you said,\n"
            "so that I may see the gate of Saint Peter\n"
            "and those whom you make so sorrowful.\"\n"
            "Then he moved on, and I behind him kept."
        ),
        "italian": (
            "E io a lui: «Poeta, io ti richieggio\n"
            "per quello Dio che tu non conoscesti,\n"
            "acciò ch'io fugga questo male e peggio,\n"
            "che tu mi meni là dov'or dicesti,\n"
            "sì ch'io vegga la porta di san Pietro\n"
            "e color che tu fai cotanto mesti».\n"
            "Allor si mosse, e io li tenni dietro."
        ),
        "english": (
            "And I to him: \"Poet, I beseech you\n"
            "by that God whom you did not know,\n"
            "so that I may escape this evil and worse,\n"
            "that you lead me there where you now said,\n"
            "so that I may see the gate of Saint Peter\n"
            "and those whom you make so sorrowful.\"\n"
            "Then he moved on, and I kept close behind."
        ),
        "note": (
            "Richieggio: present indicative of richiedere (to beseech, request); archaic first person singular. "
            "Acciò ch'io fugga: purpose clause with present subjunctive (fugga = that I may flee). "
            "Meni, vegga: present subjunctive forms (lead, may see). "
            "Dov'or = dove ora (where now). Li tenni dietro: tenni is passato remoto of tenere; "
            "dietro = behind."
        ),
    },
]

# ─── Unified learn flow: first three sentences ────────────────────────────────
# Each entry bundles the Italian text, vocabulary to learn/review, one
# word-order exercise, and one translation exercise for a single tercet.

SENTENCES = [
    {
        "id": "s1",
        "lines": (1, 3),
        "italian": (
            "Nel mezzo del cammin di nostra vita\n"
            "mi ritrovai per una selva oscura,\n"
            "ché la diritta via era smarrita."
        ),
        # Words from VOCABULARY that appear in this tercet, in order
        "vocab_ids": [
            "nel", "mezzo", "del", "cammin", "prep_di", "nostra", "vita",
            "pron_mi", "ritrovai", "prep_per", "art_un", "selva", "oscura",
            "conj_ché", "art_la", "diritta", "via", "essere", "smarrita",
        ],
        # person_idx: 0=io 1=tu 2=egli 3=noi 4=voi 5=essi
        "verb_highlights": {
            "essere":   [{"tense": "imperfect",      "person_idx": 2}],  # era
            "ritrovai": [{"tense": "passato_remoto", "person_idx": 0}],  # mi ritrovai
        },
        "word_order": [
            {
                "line": 1,
                "tokens": ["Nel", "mezzo", "del", "cammin", "di", "nostra", "vita"],
                "translation": "In the middle of the journey of our life",
                "hint": (
                    "Del = di + il. The poem opens in medias res — Dante is midway through life's journey. "
                    "Nostra vita = our life (nostra is feminine, agreeing with vita)."
                ),
            },
            {
                "line": 2,
                "tokens": ["mi", "ritrovai", "per", "una", "selva", "oscura,"],
                "translation": "I came to myself in a dark wood,",
                "hint": (
                    "Ritrovai is passato remoto of ritrovarsi (reflexive: to find oneself again). "
                    "Mi is the reflexive pronoun. Per = in, through."
                ),
            },
            {
                "line": 3,
                "tokens": ["ché", "la", "diritta", "via", "era", "smarrita."],
                "translation": "for the straight way was lost.",
                "hint": (
                    "Ché = because, for (note the grave accent — different from che, which/that). "
                    "Era smarrita: imperfect passive of smarrire (to lose one's way)."
                ),
            },
        ],
        "translation": {
            "lines": (1, 3),
            "prompt": (
                "In the middle of the journey of our life\n"
                "myself I found again in a wood dark,\n"
                "for the straight way was lost."
            ),
            "italian": (
                "Nel mezzo del cammin di nostra vita\n"
                "mi ritrovai per una selva oscura,\n"
                "ché la diritta via era smarrita."
            ),
            "note": (
                "Mi ritrovai is reflexive (ritrovarsi): 'I found myself again'. "
                "Ché (with accent) = because/for, distinct from che (that/which). "
                "Diritta via = the straight way, echoed by verace via at line 12."
            ),
        },
    },
    {
        "id": "s2",
        "lines": (4, 6),
        "italian": (
            "Ahi quanto a dir qual era è cosa dura\n"
            "esta selva selvaggia e aspra e forte\n"
            "che nel pensier rinova la paura!"
        ),
        # New: interj_ahi, quanto, prep_a, dire, qual, essere, cosa, duro,
        #      esta, selvaggio, conj_e, aspro, forte, pensier, rinova
        # Review: selva, conj_che, nel, art_la, paura
        "vocab_ids": [
            "interj_ahi", "quanto", "prep_a", "dire", "qual", "essere",
            "cosa", "duro", "esta", "selva", "selvaggio", "conj_e",
            "aspro", "forte", "conj_che", "nel", "pensier", "rinova",
            "art_la", "paura",
        ],
        # essere appears as both è (present 3sg) and era (imperfect 3sg) in line 4
        "verb_highlights": {
            "essere": [
                {"tense": "present",   "person_idx": 2},   # è
                {"tense": "imperfect", "person_idx": 2},   # era
            ],
            "dire":   [],   # dir is an infinitive — no cell to highlight
            "rinova": [{"tense": "present", "person_idx": 2}],  # rinnova/rinova
        },
        "word_order": [
            {
                "line": 4,
                "tokens": ["Ahi", "quanto", "a", "dir", "qual", "era", "è", "cosa", "dura"],
                "translation": "Ah, how hard a thing it is to tell what it was",
                "hint": (
                    "Ahi = alas! Quanto = how (much). Dir qual era = to tell what it was. "
                    "È cosa dura = it is a hard thing. "
                    "Note era (imperfect: was) and è (present: is) side by side."
                ),
            },
            {
                "line": 5,
                "tokens": ["esta", "selva", "selvaggia", "e", "aspra", "e", "forte"],
                "translation": "this wood savage and harsh and fierce",
                "hint": (
                    "Esta = questa (this), archaic poetic form. "
                    "Three adjectives build up the description: selvaggia (savage), aspra (harsh), forte (fierce). "
                    "All feminine, agreeing with selva (f.)."
                ),
            },
            {
                "line": 6,
                "tokens": ["che", "nel", "pensier", "rinova", "la", "paura!"],
                "translation": "which in thought renews the fear!",
                "hint": (
                    "Che = which (relative pronoun, referring back to the wood). "
                    "Nel = in + il. Rinova is 3rd person singular present indicative."
                ),
            },
        ],
        "translation": {
            "lines": (4, 6),
            "prompt": (
                "Ah how much to say what it was is a thing hard\n"
                "this wood savage and harsh and fierce\n"
                "that in the thought renews the fear!"
            ),
            "italian": (
                "Ahi quanto a dir qual era è cosa dura\n"
                "esta selva selvaggia e aspra e forte\n"
                "che nel pensier rinova la paura!"
            ),
            "note": (
                "Esta is the archaic/poetic demonstrative (= questa, this). "
                "Selvaggia echoes selva: the adjective derives from the same root (Latin silvaticus). "
                "Rinova is present indicative: renews, not past tense."
            ),
        },
    },
    {
        "id": "s3",
        "lines": (7, 9),
        "italian": (
            "Tant'è amara che poco è più morte;\n"
            "ma per trattar del ben ch'i' vi trovai,\n"
            "dirò de l'altre cose ch'i' v'ho scorte."
        ),
        # New: tanto, essere, amaro, poco, piu, trattare, ben, adv_vi,
        #      trovare, dire, altro, cosa, avere, scorgere
        # Review: conj_che, morte, conj_ma, prep_per, del
        "vocab_ids": [
            "tanto", "essere", "amaro", "conj_che", "poco", "piu", "morte",
            "conj_ma", "prep_per", "trattare", "del", "ben", "adv_vi",
            "trovare", "dire", "altro", "cosa", "avere", "scorgere",
        ],
        "verb_highlights": {
            "essere":   [{"tense": "present",        "person_idx": 2}],  # è
            "trattare": [],   # trattar is infinitive
            "trovare":  [{"tense": "passato_remoto", "person_idx": 0}],  # trovai
            "dire":     [{"tense": "future",         "person_idx": 0}],  # dirò
            "avere":    [{"tense": "present",        "person_idx": 0}],  # ho
            "scorgere": [{"tense": "past_participle","person_idx": 3}],  # scòrte (f.pl.)
        },
        "word_order": [
            {
                "line": 7,
                "tokens": ["Tant'è", "amara", "che", "poco", "è", "più", "morte;"],
                "translation": "So bitter is it that death is scarcely more;",
                "hint": (
                    "Tant'è = tanto è (elision before è): so much is it, so bitter. "
                    "Poco è più morte = death is little more (scarcely worse than the wood). "
                    "Note che here introduces a result clause (so … that)."
                ),
            },
            {
                "line": 8,
                "tokens": ["ma", "per", "trattar", "del", "ben", "ch'i'", "vi", "trovai,"],
                "translation": "but in order to speak of the good that I found there,",
                "hint": (
                    "Ma = but. Per + infinitive = in order to (trattar = to treat, speak of). "
                    "Del = di + il. Ch'i' = che io (elided). Vi = there (adverb)."
                ),
            },
            {
                "line": 9,
                "tokens": ["dirò", "de", "l'altre", "cose", "ch'i'", "v'ho", "scorte."],
                "translation": "I will tell of the other things that I have seen there.",
                "hint": (
                    "Dirò = I will tell (1st sg. future of dire). "
                    "De l'altre = di le altre = of the other. "
                    "Ch'i' = che io. V'ho scorte = vi ho scorgere, I have perceived/seen there."
                ),
            },
        ],
        "translation": {
            "lines": (7, 9),
            "prompt": (
                "So much is it bitter that little is more death;\n"
                "but in order to treat of the good that I there found,\n"
                "I will tell of the other things that I there have seen."
            ),
            "italian": (
                "Tant'è amara che poco è più morte;\n"
                "ma per trattar del ben ch'i' vi trovai,\n"
                "dirò de l'altre cose ch'i' v'ho scorte."
            ),
            "note": (
                "Tant'è = tanto è (elision before è): so much/so bitter is it. "
                "Per trattar: per + infinitive expresses purpose (in order to speak of). "
                "Ch'i' = che io; vi = there (adverb of place, archaic/poetic). "
                "Dirò: future of dire (I will tell). Scorte: past participle of scorgere (to perceive, see)."
            ),
        },
    },
]
