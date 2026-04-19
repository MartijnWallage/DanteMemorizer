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

    # ─── NEW VOCABULARY (lines 10-45) ─────────────────────────────────────────

    # Verbs
    {
        "id": "abbandonare",
        "italian": "abbandonare",
        "english": "to abandon, to forsake",
        "pos": "verb (abbandonare)",
        "example_italian": "che la verace via abbandonai",
        "example_english": "that I abandoned the true way",
        "note": (
            "From Old French abandoner (to give over to another's control), ultimately from a ban "
            "(at someone's command/mercy). Abbandonai is 1st person singular passato remoto. "
            "Unchanged in modern Italian; related to English 'abandon'."
        ),
        "forms": {
            "infinitive": "abbandonare",
            "present":        ["abbandono", "abbandoni", "abbandona", "abbandoniamo", "abbandonate", "abbandonano"],
            "imperfect":      ["abbandonavo", "abbandonavi", "abbandonava", "abbandonavamo", "abbandonavate", "abbandonavano"],
            "passato_remoto": ["abbandonai", "abbandonasti", "abbandonò", "abbandonammo", "abbandonaste", "abbandonarono"],
            "future":         ["abbandonerò", "abbandonerai", "abbandonerà", "abbandoneremo", "abbandonerete", "abbandoneranno"],
            "past_participle": "abbandonato",
        },
    },
    {
        "id": "terminare",
        "italian": "terminare",
        "english": "to end, to terminate",
        "pos": "verb (terminare)",
        "example_italian": "là dove terminava quella valle",
        "example_english": "there where that valley ended",
        "note": (
            "From Latin terminare (to set a boundary), from terminus (boundary, end). "
            "Terminava is 3rd person singular imperfect (was ending / came to an end). "
            "Unchanged in modern Italian; related to English 'terminate', 'terminal'."
        ),
        "forms": {
            "infinitive": "terminare",
            "present":        ["termino", "termini", "termina", "terminiamo", "terminate", "terminano"],
            "imperfect":      ["terminavo", "terminavi", "terminava", "terminavamo", "terminavate", "terminavano"],
            "passato_remoto": ["terminai", "terminasti", "terminò", "terminammo", "terminaste", "terminarono"],
            "future":         ["terminerò", "terminerai", "terminerà", "termineremo", "terminerete", "termineranno"],
            "past_participle": "terminato",
        },
    },
    {
        "id": "guardare",
        "italian": "guardare",
        "english": "to look, to look up at, to gaze",
        "pos": "verb (guardare)",
        "example_italian": "guardai in alto e vidi le sue spalle",
        "example_english": "I looked up high and saw its shoulders",
        "note": (
            "From Frankish *wardōn (to watch, guard), via Old French garder. "
            "Guardai is 1st person singular passato remoto. "
            "Related to English 'guard'; modern Italian guardare is unchanged. "
            "Guardare in alto = to look up high."
        ),
        "forms": {
            "infinitive": "guardare",
            "present":        ["guardo", "guardi", "guarda", "guardiamo", "guardate", "guardano"],
            "imperfect":      ["guardavo", "guardavi", "guardava", "guardavamo", "guardavate", "guardavano"],
            "passato_remoto": ["guardai", "guardasti", "guardò", "guardammo", "guardaste", "guardarono"],
            "future":         ["guarderò", "guarderai", "guarderà", "guarderemo", "guarderete", "guarderanno"],
            "past_participle": "guardato",
        },
    },
    {
        "id": "vedere",
        "italian": "vedere",
        "english": "to see",
        "pos": "verb (vedere)",
        "example_italian": "guardai in alto e vidi le sue spalle",
        "example_english": "I looked up high and saw its shoulders",
        "note": (
            "From Latin videre. Vidi is 1st person singular passato remoto (I saw), "
            "directly descended from Latin vidi. "
            "Related to English 'video', 'vision', 'evident'. "
            "Common throughout the Commedia; Dante repeatedly says vidi (I saw)."
        ),
        "forms": {
            "infinitive": "vedere",
            "present":        ["vedo", "vedi", "vede", "vediamo", "vedete", "vedono"],
            "imperfect":      ["vedevo", "vedevi", "vedeva", "vedevamo", "vedevate", "vedevano"],
            "passato_remoto": ["vidi", "vedesti", "vide", "vedemmo", "vedeste", "videro"],
            "future":         ["vedrò", "vedrai", "vedrà", "vedremo", "vedrete", "vedranno"],
            "past_participle": "visto / veduto",
        },
    },
    {
        "id": "menare",
        "italian": "menare",
        "english": "to lead, to guide, to bring",
        "pos": "verb (menare)",
        "example_italian": "che mena dritto altrui per ogni calle",
        "example_english": "that leads others straight along every path",
        "note": (
            "From Latin minare (to drive animals by threatening), related to minari (to threaten). "
            "Mena is 3rd person singular present indicative. "
            "Medieval Italian menare = to lead; the sun (the planet) leads people along the right path. "
            "In modern Italian, condurre or guidare is preferred; menare survives in some dialects."
        ),
        "forms": {
            "infinitive": "menare",
            "present":        ["meno", "meni", "mena", "meniamo", "menate", "menano"],
            "imperfect":      ["menavo", "menavi", "menava", "menavamo", "menavate", "menavano"],
            "passato_remoto": ["menai", "menasti", "menò", "menammo", "menaste", "menarono"],
            "future":         ["menerò", "menerai", "menerà", "meneremo", "menerete", "meneranno"],
            "past_participle": "menato",
        },
    },
    {
        "id": "durare",
        "italian": "durare",
        "english": "to last, to endure",
        "pos": "verb (durare)",
        "example_italian": "che nel lago del cor m'era durata",
        "example_english": "that had lasted in the lake of my heart",
        "note": (
            "From Latin durare (to harden, to last), related to durus (hard). "
            "M'era durata is 3rd person singular pluperfect: 'had lasted to me'. "
            "The reflexive dative m' (= mi) is a common medieval construction expressing "
            "personal involvement. Related to English 'durable', 'duration', 'endure'."
        ),
        "forms": {
            "infinitive": "durare",
            "present":        ["duro", "duri", "dura", "duriamo", "durate", "durano"],
            "imperfect":      ["duravo", "duravi", "durava", "duravamo", "duravate", "duravano"],
            "passato_remoto": ["durai", "durasti", "durò", "durammo", "duraste", "durarono"],
            "future":         ["durerò", "durerai", "durerà", "dureremo", "durerete", "dureranno"],
            "past_participle": "durato",
        },
    },
    {
        "id": "passare",
        "italian": "passare",
        "english": "to pass, to spend (time)",
        "pos": "verb (passare)",
        "example_italian": "la notte ch'i' passai con tanta pieta",
        "example_english": "the night that I passed with such great pity",
        "note": (
            "From Latin passus (step), via Vulgar Latin *passare. "
            "Passai is 1st person singular passato remoto. "
            "Passare il tempo / la notte = to spend time / the night. "
            "Related to English 'pass', 'passage'. Unchanged in modern Italian."
        ),
        "forms": {
            "infinitive": "passare",
            "present":        ["passo", "passi", "passa", "passiamo", "passate", "passano"],
            "imperfect":      ["passavo", "passavi", "passava", "passavamo", "passavate", "passavano"],
            "passato_remoto": ["passai", "passasti", "passò", "passammo", "passaste", "passarono"],
            "future":         ["passerò", "passerai", "passerà", "passeremo", "passerete", "passeranno"],
            "past_participle": "passato",
        },
    },
    {
        "id": "volgere",
        "italian": "volgere",
        "english": "to turn, to turn back",
        "pos": "verb (volgere)",
        "example_italian": "si volge a l'acqua perigliosa e guata",
        "example_english": "turns to the perilous water and gazes",
        "note": (
            "From Latin volvere (to roll, turn). Irregular. "
            "Si volge = 3rd sg. present reflexive (turns himself). "
            "Si volse = 3rd sg. passato remoto reflexive (turned himself). "
            "Vòlto (line 36) is the past participle, with the accent marking the stressed open o. "
            "Related to English 'revolve', 'involve'."
        ),
        "forms": {
            "infinitive": "volgere",
            "present":        ["volgo", "volgi", "volge", "volgiamo", "volgete", "volgono"],
            "imperfect":      ["volgevo", "volgevi", "volgeva", "volgevamo", "volgevate", "volgevano"],
            "passato_remoto": ["volsi", "volgesti", "volse", "volgemmo", "volgeste", "volsero"],
            "future":         ["volgerò", "volgerai", "volgerà", "volgeremo", "volgerete", "volgeranno"],
            "past_participle": "vòlto",
        },
    },
    {
        "id": "fuggire",
        "italian": "fuggire",
        "english": "to flee, to fly away",
        "pos": "verb (fuggire)",
        "example_italian": "così l'animo mio, ch'ancor fuggiva",
        "example_english": "so my spirit, which was still fleeing",
        "note": (
            "From Latin fugere (to flee). Fuggiva is 3rd person singular imperfect "
            "(was still fleeing — the imperfect marks continuing action). "
            "Related to English 'fugitive', 'refuge'. Unchanged in modern Italian."
        ),
        "forms": {
            "infinitive": "fuggire",
            "present":        ["fuggo", "fuggi", "fugge", "fuggiamo", "fuggite", "fuggono"],
            "imperfect":      ["fuggivo", "fuggivi", "fuggiva", "fuggivamo", "fuggivate", "fuggivano"],
            "passato_remoto": ["fuggii", "fuggisti", "fuggì", "fuggimmo", "fuggiste", "fuggirono"],
            "future":         ["fuggirò", "fuggirai", "fuggirà", "fuggiremo", "fuggirete", "fuggiranno"],
            "past_participle": "fuggito",
        },
    },
    {
        "id": "rimirare",
        "italian": "rimirare",
        "english": "to gaze back at, to contemplate",
        "pos": "verb (rimirare)",
        "example_italian": "si volse a retro a rimirar lo passo",
        "example_english": "turned back to gaze upon the pass",
        "note": (
            "Ri- (again, back) + mirare (to look at, aim at), from Latin mirare (to wonder at). "
            "Rimirar is the apocopated infinitive. "
            "The prefix ri- adds the sense of looking back at something already passed. "
            "Related to English 'admire', 'mirror'. Modern Italian: rimirare (literary)."
        ),
        "forms": {
            "infinitive": "rimirare",
            "present":        ["rimiro", "rimiri", "rimira", "rimiriamo", "rimirate", "rimirano"],
            "imperfect":      ["rimiravo", "rimiravi", "rimirava", "rimiravamo", "rimiravate", "rimiravano"],
            "passato_remoto": ["rimirài", "rimirasti", "rimirò", "rimirammo", "rimiraste", "rimirarono"],
            "future":         ["rimirerò", "rimirerai", "rimirerà", "rimireremo", "rimirerete", "rimireranno"],
            "past_participle": "rimirato",
        },
    },
    {
        "id": "posare",
        "italian": "posare",
        "english": "to rest, to set down",
        "pos": "verb (posare)",
        "example_italian": "Poi ch'èi posato un poco il corpo lasso",
        "example_english": "After I had rested a little the weary body",
        "note": (
            "From Latin pausare (to pause, rest), from Greek pausis (a stop). "
            "Posato is the past participle used with avere (ch'èi posato = after I had rested). "
            "Note ch'èi = che io ho in contracted/archaic form. "
            "Related to English 'pause'. Modern Italian: posare (to rest, to put down)."
        ),
        "forms": {
            "infinitive": "posare",
            "present":        ["poso", "posi", "posa", "posiamo", "posate", "posano"],
            "imperfect":      ["posavo", "posavi", "posava", "posavamo", "posavate", "posavano"],
            "passato_remoto": ["posai", "posasti", "posò", "posammo", "posaste", "posarono"],
            "future":         ["poserò", "poserai", "poserà", "poseremo", "poserete", "poseranno"],
            "past_participle": "posato",
        },
    },
    {
        "id": "riprendere",
        "italian": "riprendere",
        "english": "to resume, to take up again",
        "pos": "verb (riprendere)",
        "example_italian": "ripresi via per la piaggia diserta",
        "example_english": "I resumed my way along the deserted slope",
        "note": (
            "Ri- (again) + prendere (to take), from Latin prehendere. "
            "Ripresi is 1st person singular passato remoto. "
            "Ripresi via = I resumed (my) way/journey. "
            "Prendere gives English 'apprehend', 'comprehend'. Modern Italian: riprendere."
        ),
        "forms": {
            "infinitive": "riprendere",
            "present":        ["riprendo", "riprendi", "riprende", "riprendiamo", "riprendete", "riprendono"],
            "imperfect":      ["riprendevo", "riprendevi", "riprendeva", "riprendevamo", "riprendevate", "riprendevano"],
            "passato_remoto": ["ripresi", "riprendesti", "riprese", "riprendemmo", "riprendeste", "ripresero"],
            "future":         ["riprenderò", "riprenderai", "riprenderà", "riprenderemo", "riprenderete", "riprenderanno"],
            "past_participle": "ripreso",
        },
    },
    {
        "id": "cominciare",
        "italian": "cominciare",
        "english": "to begin",
        "pos": "verb (cominciare)",
        "example_italian": "quasi al cominciar de l'erta",
        "example_english": "almost at the beginning of the steep",
        "note": (
            "From Latin *comitiare (to inaugurate), from comitia (public assembly). "
            "Cominciar is the apocopated infinitive used as a noun: 'the beginning'. "
            "Al cominciar = at the beginning. Modern Italian: cominciare (also iniziare)."
        ),
        "forms": {
            "infinitive": "cominciare",
            "present":        ["comincio", "cominci", "comincia", "cominciamo", "cominciate", "cominciano"],
            "imperfect":      ["cominciavo", "cominciavi", "cominciava", "cominciavamo", "cominciavate", "cominciavano"],
            "passato_remoto": ["cominciai", "cominciasti", "cominciò", "cominciammo", "cominciaste", "cominciarono"],
            "future":         ["comincerò", "comincerai", "comincerà", "cominceremo", "comincerete", "cominceranno"],
            "past_participle": "cominciato",
        },
    },
    {
        "id": "partire",
        "italian": "partire",
        "english": "to depart, to leave",
        "pos": "verb (partire)",
        "example_italian": "e non mi si partia dinanzi al volto",
        "example_english": "and it did not depart from before my face",
        "note": (
            "From Latin partire (to divide, depart). "
            "Partia is the syncopated imperfect of partire (= partiva): 3rd person singular. "
            "Non mi si partia = did not depart from before me. "
            "Modern Italian: partire (to leave, depart). The syncopated imperfect -ia for -iva "
            "is a common feature of medieval Italian verse."
        ),
        "forms": {
            "infinitive": "partire",
            "present":        ["parto", "parti", "parte", "partiamo", "partite", "partono"],
            "imperfect":      ["partivo", "partivi", "partiva", "partivamo", "partivate", "partivano"],
            "passato_remoto": ["partii", "partisti", "partì", "partimmo", "partiste", "partirono"],
            "future":         ["partirò", "partirai", "partirà", "partiremo", "partirete", "partiranno"],
            "past_participle": "partito",
        },
    },
    {
        "id": "impedire",
        "italian": "impedire",
        "english": "to impede, to hinder, to block",
        "pos": "verb (impedire)",
        "example_italian": "anzi 'mpediva tanto il mio cammino",
        "example_english": "rather it so much impeded my advance",
        "note": (
            "From Latin impedire (to shackle, to hinder), from in- + pes/pedis (foot). "
            "'Mpediva is the imperfect of impedire with elision of the initial i-. "
            "The apostrophe marks the dropped vowel: 'mpediva = impediva. "
            "Related to English 'impede', 'impediment'. Unchanged in modern Italian."
        ),
        "forms": {
            "infinitive": "impedire",
            "present":        ["impedisco", "impedisci", "impedisce", "impediamo", "impedite", "impediscono"],
            "imperfect":      ["impedivo", "impedivi", "impediva", "impedivamo", "impedivate", "impedivano"],
            "passato_remoto": ["impedii", "impedisti", "impedì", "impedimmo", "impediste", "impedirono"],
            "future":         ["impedirò", "impedirai", "impedirà", "impediremo", "impedirete", "impediranno"],
            "past_participle": "impedito",
        },
    },
    {
        "id": "tornare",
        "italian": "tornare",
        "english": "to return, to turn back",
        "pos": "verb (tornare)",
        "example_italian": "che fu per tornare più volte vòlto",
        "example_english": "that many times it was turned back to return",
        "note": (
            "From Latin tornare (to turn on a lathe), related to tornus (lathe). "
            "Fu per tornare = was on the verge of returning (fu per + infinitive = was about to). "
            "Unchanged in modern Italian. Related to English 'turn', 'tour', 'tournament'."
        ),
        "forms": {
            "infinitive": "tornare",
            "present":        ["torno", "torni", "torna", "torniamo", "tornate", "tornano"],
            "imperfect":      ["tornavo", "tornavi", "tornava", "tornavamo", "tornavate", "tornavano"],
            "passato_remoto": ["tornai", "tornasti", "tornò", "tornammo", "tornaste", "tornarono"],
            "future":         ["tornerò", "tornerai", "tornerà", "torneremo", "tornerete", "torneranno"],
            "past_participle": "tornato",
        },
    },
    {
        "id": "montare",
        "italian": "montare",
        "english": "to climb, to mount, to rise",
        "pos": "verb (montare)",
        "example_italian": "e 'l sol montava 'n sù con quelle stelle",
        "example_english": "and the sun was climbing upward with those stars",
        "note": (
            "From Latin montare (to mount), from mons/montis (mountain). "
            "Montava is 3rd person singular imperfect (was climbing/mounting). "
            "'l sol = il sole (apocopated + elided). "
            "'n sù = in su (upward): double elision, poetic form. "
            "Related to English 'mount', 'mountain'."
        ),
        "forms": {
            "infinitive": "montare",
            "present":        ["monto", "monti", "monta", "montiamo", "montate", "montano"],
            "imperfect":      ["montavo", "montavi", "montava", "montavamo", "montavate", "montavano"],
            "passato_remoto": ["montai", "montasti", "montò", "montammo", "montaste", "montarono"],
            "future":         ["monterò", "monterai", "monterà", "monteremo", "monterete", "monteranno"],
            "past_participle": "montato",
        },
    },
    {
        "id": "muovere",
        "italian": "muovere",
        "english": "to move, to set in motion",
        "pos": "verb (muovere)",
        "example_italian": "mosse di prima quelle cose belle",
        "example_english": "first moved those beautiful things",
        "note": (
            "From Latin movere. Mosse is 3rd person singular passato remoto (moved). "
            "The subject is l'amor divino (divine love, line 39), which at Creation "
            "first set the heavens in motion. "
            "Related to English 'move', 'motion', 'emotion'. Modern Italian: muovere / muoversi."
        ),
        "forms": {
            "infinitive": "muovere",
            "present":        ["muovo", "muovi", "muove", "muoviamo", "muovete", "muovono"],
            "imperfect":      ["movevo", "movevi", "moveva", "movevamo", "movevate", "movevano"],
            "passato_remoto": ["mossi", "movesti", "mosse", "movemmo", "moveste", "mossero"],
            "future":         ["muoverò", "muoverai", "muoverà", "muoveremo", "muoverete", "muoveranno"],
            "past_participle": "mosso",
        },
    },
    {
        "id": "sperare",
        "italian": "sperare",
        "english": "to hope",
        "pos": "verb (sperare)",
        "example_italian": "sì ch'a bene sperar m'era cagione",
        "example_english": "so that it gave me cause to hope for good",
        "note": (
            "From Latin sperare (to hope, to expect). "
            "Sperar is the apocopated infinitive. "
            "Bene sperar = to hope for good things. "
            "Related to English 'despair' (de + sperare = to stop hoping). "
            "Unchanged in modern Italian."
        ),
        "forms": {
            "infinitive": "sperare",
            "present":        ["spero", "speri", "spera", "speriamo", "sperate", "sperano"],
            "imperfect":      ["speravo", "speravi", "sperava", "speravamo", "speravate", "speravano"],
            "passato_remoto": ["sperai", "sperasti", "sperò", "sperammo", "speraste", "sperarono"],
            "future":         ["spererò", "spererai", "spererà", "spereremo", "spererete", "spereranno"],
            "past_participle": "sperato",
        },
    },
    {
        "id": "dare",
        "italian": "dare",
        "english": "to give",
        "pos": "verb (dare)",
        "example_italian": "ma non sì che paura non mi desse",
        "example_english": "but not so much that fear did not give me",
        "note": (
            "From Latin dare. Highly irregular. "
            "Desse is 3rd person singular imperfect subjunctive (might give, would give). "
            "Ma non sì che … non mi desse = but not so much that it did not give me (fear). "
            "The double negative (non sì … non) is emphatic: it did indeed give him fear. "
            "Related to English 'data', 'date' (given time)."
        ),
        "forms": {
            "infinitive": "dare",
            "present":        ["do", "dai", "dà", "diamo", "date", "danno"],
            "imperfect":      ["davo", "davi", "dava", "davamo", "davate", "davano"],
            "passato_remoto": ["diedi", "desti", "diede", "demmo", "deste", "diedero"],
            "future":         ["darò", "darai", "darà", "daremo", "darete", "daranno"],
            "past_participle": "dato",
        },
    },
    {
        "id": "apparire",
        "italian": "apparire",
        "english": "to appear, to come into view",
        "pos": "verb (apparire)",
        "example_italian": "la vista d'un leon che m'apparve poscia",
        "example_english": "the sight of a lion that afterwards appeared to me",
        "note": (
            "From Latin apparere (to come in sight), from ad- + parere (to show oneself). "
            "Apparve is 3rd person singular passato remoto (appeared). "
            "M'apparve = mi apparve (appeared to me). "
            "Related to English 'appear', 'apparent', 'apparition'. Modern Italian: apparire."
        ),
        "forms": {
            "infinitive": "apparire",
            "present":        ["appaio", "appari", "appare", "appariamo", "apparite", "appaiono"],
            "imperfect":      ["apparivo", "apparivi", "appariva", "apparivamo", "apparivate", "apparivano"],
            "passato_remoto": ["apparvi", "apparisti", "apparve", "apparimmo", "appariste", "apparvero"],
            "future":         ["apparirò", "apparirai", "apparirà", "appariremo", "apparirete", "appariranno"],
            "past_participle": "apparso",
        },
    },
    {
        "id": "guatare",
        "italian": "guatare",
        "english": "to gaze at, to stare",
        "pos": "verb (guatare)",
        "example_italian": "si volge a l'acqua perigliosa e guata",
        "example_english": "turns to the perilous water and gazes",
        "note": (
            "From Old High German *wahtan (to watch), related to Germanic *wahtaz. "
            "Guata is 3rd person singular present indicative. "
            "An archaic/poetic verb in Italian; modern Italian would use guardare or fissare. "
            "The word evokes a sustained, rapt stare — the survivor cannot look away from the sea."
        ),
        "forms": {
            "infinitive": "guatare",
            "present":        ["guato", "guati", "guata", "guatiamo", "guatate", "guatano"],
            "passato_remoto": ["guatai", "guatasti", "guatò", "guatammo", "guataste", "guatarono"],
            "past_participle": "guatato",
        },
    },

    # Nouns (lines 10-45)
    {
        "id": "sonno",
        "italian": "sonno",
        "english": "sleep",
        "pos": "noun (m.)",
        "example_italian": "tant'era pien di sonno a quel punto",
        "example_english": "so full of sleep was I at that point",
        "note": (
            "From Latin somnus (sleep). Unchanged in modern Italian. "
            "Pien di sonno = full of sleep (pien is the apocopated form of pieno). "
            "The sleep stands for spiritual torpor — Dante's falling into sin. "
            "Related to English 'somnambulism', 'insomnia'."
        ),
    },
    {
        "id": "spalle",
        "italian": "spalle",
        "english": "shoulders",
        "pos": "noun (f. pl.)",
        "example_italian": "vidi le sue spalle / vestite già de' raggi del pianeta",
        "example_english": "I saw its shoulders / already clothed in the rays of the planet",
        "note": (
            "Plural of spalla (shoulder), from Late Latin spatula (shoulder blade, small spatula). "
            "Le sue spalle = its shoulders (referring to the hill, personified). "
            "De' raggi = dei raggi (of the rays): de' is a poetic contraction of dei. "
            "Related to English 'spatula', 'epaulette'."
        ),
    },
    {
        "id": "raggio",
        "italian": "raggio",
        "english": "ray, beam (of light)",
        "pos": "noun (m.)",
        "example_italian": "vestite già de' raggi del pianeta",
        "example_english": "already clothed in the rays of the planet",
        "note": (
            "From Latin radius (ray, spoke of a wheel). Plural: raggi. "
            "De' raggi = di + i + raggi (of the rays), poetically contracted. "
            "Related to English 'radius', 'radiant'. Unchanged in modern Italian."
        ),
    },
    {
        "id": "calle",
        "italian": "calle",
        "english": "path, lane, narrow way",
        "pos": "noun (f. or m.)",
        "example_italian": "che mena dritto altrui per ogni calle",
        "example_english": "that leads others straight along every path",
        "note": (
            "From Latin callis (narrow path, sheep track). "
            "Archaic in standard Italian; survives in Venetian placenames (e.g., Calle Larga). "
            "Per ogni calle = along every path. "
            "The sun is said to lead all creatures along their proper way."
        ),
    },
    {
        "id": "pieta",
        "italian": "pieta / pietà",
        "english": "pity, compassion; piety",
        "pos": "noun (f.)",
        "example_italian": "la notte ch'i' passai con tanta pieta",
        "example_english": "the night that I passed with such great pity/anguish",
        "note": (
            "From Latin pietas (dutiful conduct, piety, affection). "
            "In Dante, pieta (without accent, for metre) = pity, grief, compassion. "
            "Pietà (with accent) in modern Italian = pity, compassion; also the art term "
            "(Michelangelo's Pietà). The commentators debate: pieta here may mean spiritual anguish "
            "as much as pity."
        ),
    },
    {
        "id": "lena",
        "italian": "lena",
        "english": "breath, energy, strength",
        "pos": "noun (f.)",
        "example_italian": "E come quei che con lena affannata",
        "example_english": "And like one who with laboured breath",
        "note": (
            "From Latin halena / alena (breath), related to halare (to breathe). "
            "Lena affannata = laboured/breathless breath. "
            "In modern Italian lena survives in the idiom di buona lena (energetically, with a will). "
            "The simile compares Dante's soul to a swimmer who has just escaped the sea."
        ),
    },
    {
        "id": "pelago",
        "italian": "pelago",
        "english": "open sea, deep water",
        "pos": "noun (m.)",
        "example_italian": "uscito fuor del pelago a la riva",
        "example_english": "having come out of the open sea to the shore",
        "note": (
            "From Greek pelagos (open sea) via Latin pelagus. "
            "An elevated, literary word — the common word is mare. "
            "Fuor del pelago = out of the open sea. "
            "Dante uses the term also in Paradiso to describe his spiritual sea-voyage. "
            "Related to English 'pelagic' (of the open sea)."
        ),
    },
    {
        "id": "riva",
        "italian": "riva",
        "english": "shore, bank",
        "pos": "noun (f.)",
        "example_italian": "uscito fuor del pelago a la riva",
        "example_english": "having come out of the open sea to the shore",
        "note": (
            "From Latin ripa (bank, shore). Unchanged in modern Italian. "
            "A la riva = to the shore (a + la). "
            "Related to English 'river', 'arrive' (ad + ripam, to reach the bank). "
            "Rival originally meant someone who uses the same stream."
        ),
    },
    {
        "id": "acqua",
        "italian": "acqua",
        "english": "water",
        "pos": "noun (f.)",
        "example_italian": "si volge a l'acqua perigliosa e guata",
        "example_english": "turns to the perilous water and gazes",
        "note": (
            "From Latin aqua. Unchanged in modern Italian. "
            "A l'acqua = a + la + acqua (elision before vowel). "
            "Related to English 'aquatic', 'aquarium', 'aqueduct'."
        ),
    },
    {
        "id": "animo",
        "italian": "animo",
        "english": "soul, spirit, mind",
        "pos": "noun (m.)",
        "example_italian": "così l'animo mio, ch'ancor fuggiva",
        "example_english": "so my spirit, which was still fleeing",
        "note": (
            "From Latin animus (mind, spirit, courage). "
            "Distinct from anima (soul, breath of life, f.): animo suggests the rational, "
            "volitional mind; anima the vital soul. "
            "L'animo mio = my spirit/soul. Related to English 'animate', 'animal', 'unanimous'."
        ),
    },
    {
        "id": "passo",
        "italian": "passo",
        "english": "pass, passage; step",
        "pos": "noun (m.)",
        "example_italian": "si volse a retro a rimirar lo passo",
        "example_english": "turned back to gaze upon the pass",
        "note": (
            "From Latin passus (step, pace). "
            "Lo passo here refers to the dangerous pass or passage through the dark wood, "
            "not a physical footstep. Lo is the archaic article (= il) before p-. "
            "Related to English 'pass', 'passage', 'trespass'. Unchanged in modern Italian."
        ),
    },
    {
        "id": "persona",
        "italian": "persona",
        "english": "person, soul",
        "pos": "noun (f.)",
        "example_italian": "che non lasciò già mai persona viva",
        "example_english": "that never yet left any person alive",
        "note": (
            "From Latin persona (mask, character in a play, person). "
            "Non lasciò già mai persona viva = the pass/dark wood has never let anyone "
            "escape with their life. Unchanged in modern Italian. "
            "Related to English 'person', 'personal', 'impersonate'."
        ),
    },
    {
        "id": "corpo",
        "italian": "corpo",
        "english": "body",
        "pos": "noun (m.)",
        "example_italian": "riposato un poco il corpo lasso",
        "example_english": "having rested a little the weary body",
        "note": (
            "From Latin corpus, corporis (body). Unchanged in modern Italian. "
            "Il corpo lasso = the weary body (lasso = weary). "
            "Related to English 'corps', 'corpse', 'corporeal', 'incorporate'."
        ),
    },
    {
        "id": "piaggia",
        "italian": "piaggia",
        "english": "hillside, slope; shore",
        "pos": "noun (f.)",
        "example_italian": "ripresi via per la piaggia diserta",
        "example_english": "I resumed my way along the deserted slope",
        "note": (
            "From Latin plaga (region, zone). In Dante, piaggia = slope, hillside. "
            "The word also means beach or shore in some contexts. "
            "Diserta (= deserted, lonely) is a predicate adjective agreeing with piaggia (f.). "
            "Modern Italian: piaggia (rare, poetic); spiaggia = beach."
        ),
    },
    {
        "id": "erta",
        "italian": "erta",
        "english": "steep slope, ascent",
        "pos": "noun (f.)",
        "example_italian": "quasi al cominciar de l'erta",
        "example_english": "almost at the beginning of the steep",
        "note": (
            "From Latin ērecta (raised, erect), past participle of erigere. "
            "L'erta = the steep slope (l' = la, elided before vowel). "
            "De l'erta = di la erta = of the steep. "
            "In modern Italian: erta (steep path, ascent); also stare sull'erta = to be on guard."
        ),
    },
    {
        "id": "pelo",
        "italian": "pelo",
        "english": "hide, fur, hair, coat",
        "pos": "noun (m.)",
        "example_italian": "che di pel macolato era coverta",
        "example_english": "that was covered with a spotted hide",
        "note": (
            "From Latin pilus (a hair). Pel is the apocopated form. "
            "Di pel macolato = with a spotted hide/coat. "
            "The word refers to an animal's coat or hide. "
            "Related to English 'pile' (as in velvet pile), 'depilatory'. Modern Italian: pelo."
        ),
    },
    {
        "id": "volto",
        "italian": "volto",
        "english": "face; (past participle of volgere) turned",
        "pos": "noun (m.) / past participle",
        "example_italian": "e non mi si partia dinanzi al volto",
        "example_english": "and it did not depart from before my face",
        "note": (
            "As noun: face, from Latin vultus (face, expression). Dinanzi al volto = before my face. "
            "Also the past participle of volgere (to turn): vòlto (line 36, with accent). "
            "Fu per tornare più volte vòlto = was many times turned to return. "
            "The two senses are etymologically distinct: vultus (face) vs volutus (turned)."
        ),
    },
    {
        "id": "cammino",
        "italian": "cammino",
        "english": "way, path, advance",
        "pos": "noun (m.)",
        "example_italian": "anzi 'mpediva tanto il mio cammino",
        "example_english": "rather it so much impeded my advance",
        "note": (
            "Full form of cammin (see entry cammin). From Late Latin camminus. "
            "Il mio cammino = my way/advance. "
            "Cammino can mean the physical path or the act of walking/journeying. "
            "The canto opens with cammin (apocopated) and uses cammino here — both forms appear."
        ),
    },
    {
        "id": "tempo",
        "italian": "tempo",
        "english": "time, season; weather",
        "pos": "noun (m.)",
        "example_italian": "Temp'era dal principio del mattino",
        "example_english": "It was the time from the beginning of morning",
        "note": (
            "From Latin tempus (time). Temp'era = tempo era (elision before e). "
            "The word covers both 'time' and 'weather' in Italian. "
            "Dal principio = from the beginning (dal = da + il). "
            "Related to English 'temporal', 'temporary', 'tempo' (in music)."
        ),
    },
    {
        "id": "mattino",
        "italian": "mattino",
        "english": "morning",
        "pos": "noun (m.)",
        "example_italian": "Temp'era dal principio del mattino",
        "example_english": "It was the time from the beginning of morning",
        "note": (
            "From Latin matutinum (morning), from Matuta (goddess of dawn). "
            "Del mattino = of the morning. Dante specifies the time: spring dawn. "
            "L'ora del mattino (line 43): the hour of the morning. "
            "Modern Italian: mattino (morning); mattina is the more common form."
        ),
    },
    {
        "id": "stella",
        "italian": "stella",
        "english": "star",
        "pos": "noun (f.)",
        "example_italian": "e 'l sol montava 'n sù con quelle stelle",
        "example_english": "and the sun was climbing upward with those stars",
        "note": (
            "From Latin stella. Unchanged in modern Italian. "
            "Quelle stelle = those stars (the constellation of Aries, under which "
            "God created the world, according to medieval tradition). "
            "Related to English 'stellar', 'constellation', 'star' (via Germanic)."
        ),
    },
    {
        "id": "amor",
        "italian": "amor / amore",
        "english": "love",
        "pos": "noun (m.)",
        "example_italian": "quando l'amor divino",
        "example_english": "when divine love",
        "note": (
            "From Latin amor, amoris. Amor is the apocopated form used in verse. "
            "L'amor divino = divine love, the creative force that set the universe in motion at Creation. "
            "Dante's cosmology places Love as the prime mover. "
            "Related to English 'amorous', 'enamoured'. Modern Italian: amore."
        ),
    },
    {
        "id": "cagione",
        "italian": "cagione",
        "english": "cause, reason",
        "pos": "noun (f.)",
        "example_italian": "sì ch'a bene sperar m'era cagione",
        "example_english": "so that it gave me cause to hope for good",
        "note": (
            "From Latin occasionem (opportunity, cause), accusative of occasio. "
            "M'era cagione = was (a) cause to me / gave me reason. "
            "Also used at line 78: principio e cagion di tutta gioia. "
            "Modern Italian: cagione (archaic/literary); common synonyms: causa, ragione."
        ),
    },
    {
        "id": "pelle",
        "italian": "pelle",
        "english": "skin, hide, pelt",
        "pos": "noun (f.)",
        "example_italian": "di quella fiera a la gaìa pelle",
        "example_english": "of that beast with the gay-coloured hide",
        "note": (
            "From Latin pellis (skin, hide). Unchanged in modern Italian. "
            "A la gaìa pelle = with the gay/bright-coloured hide. "
            "Related to English 'peel', 'film' (via Latin pellicula). "
            "Pelle in modern Italian = skin (of humans and animals); also leather goods."
        ),
    },
    {
        "id": "stagione",
        "italian": "stagione",
        "english": "season",
        "pos": "noun (f.)",
        "example_italian": "la stagion nova e l'ora del mattino",
        "example_english": "the new season and the hour of morning",
        "note": (
            "From Latin stationem (a standing, station → season), accusative of statio. "
            "Stagion is the apocopated form (final -e dropped). "
            "La stagion nova = the new season (spring). "
            "Related to English 'station'. Modern Italian: stagione (unchanged)."
        ),
    },
    {
        "id": "ora",
        "italian": "ora",
        "english": "hour, time of day; (adverb) now",
        "pos": "noun (f.) / adverb",
        "example_italian": "la stagion nova e l'ora del mattino",
        "example_english": "the new season and the hour of morning",
        "note": (
            "From Latin hora (hour), from Greek hora (time, season). "
            "L'ora del mattino = the hour of morning (spring dawn). "
            "As adverb: ora = now (modern Italian). Dante uses or (apocopated) as adverb: "
            "or se' tu = are you now (line 79). "
            "Related to English 'hour', 'horoscope'."
        ),
    },
    {
        "id": "vista",
        "italian": "vista",
        "english": "sight, view, appearance",
        "pos": "noun (f.)",
        "example_italian": "la vista d'un leon che m'apparve poscia",
        "example_english": "the sight of a lion that afterwards appeared to me",
        "note": (
            "Past participle of vedere (to see), used as a noun: 'the thing seen', hence sight, view. "
            "La vista d'un leon = the sight of a lion. "
            "In modern Italian vista = sight, view (also: in vista = in sight, a vista d'occhio = visibly). "
            "Related to English 'vista', 'visit', 'vision'."
        ),
    },
    {
        "id": "principio",
        "italian": "principio",
        "english": "beginning, principle",
        "pos": "noun (m.)",
        "example_italian": "Temp'era dal principio del mattino",
        "example_english": "It was the time from the beginning of morning",
        "note": (
            "From Latin principium (beginning, origin), from princeps (first, chief). "
            "Dal principio = from the beginning. "
            "Also used at line 78: principio e cagion di tutta gioia. "
            "Related to English 'principle', 'principal', 'prince'. Unchanged in modern Italian."
        ),
    },

    # Adjectives / Adverbs / Function words (lines 10-45)
    {
        "id": "verace",
        "italian": "verace",
        "english": "true, truthful",
        "pos": "adjective",
        "example_italian": "che la verace via abbandonai",
        "example_english": "that I abandoned the true way",
        "note": (
            "From Latin verax, veracis (truthful, speaking truth), from verus (true). "
            "La verace via = the true way, the right path. "
            "Echoes la diritta via (line 3) — both phrases denote the path of righteousness. "
            "Related to English 'veracious', 'verify', 'verity'. Modern Italian: verace."
        ),
    },
    {
        "id": "alto",
        "italian": "alto",
        "english": "high, up; (adverb) up high",
        "pos": "adjective / adverb",
        "example_italian": "guardai in alto e vidi le sue spalle",
        "example_english": "I looked up high and saw its shoulders",
        "note": (
            "From Latin altus (high, deep). In alto = up high (used as adverbial phrase). "
            "Con la test'alta (line 47): with head held high. "
            "In music, alto = high voice. In modern Italian: alto/a (adjective: high, tall); "
            "in alto (upward, up there). Related to English 'altitude', 'alto', 'exalt'."
        ),
    },
    {
        "id": "dritto",
        "italian": "dritto",
        "english": "straight, direct",
        "pos": "adverb / adjective",
        "example_italian": "che mena dritto altrui per ogni calle",
        "example_english": "that leads others straight along every path",
        "note": (
            "Variant form of diritto/diritta (see entry diritta). From Latin directus. "
            "Here used as an adverb: mena dritto = leads straight. "
            "The sun as planet was believed to guide creatures along the right path. "
            "Dritto and diritta are interchangeable forms in Dante."
        ),
    },
    {
        "id": "altrui",
        "italian": "altrui",
        "english": "others, other people; to others",
        "pos": "pronoun (invariable)",
        "example_italian": "che mena dritto altrui per ogni calle",
        "example_english": "that leads others straight along every path",
        "note": (
            "From Latin alteri (to others), dative of alter. Invariable form. "
            "Functions as object or dative: mena altrui = leads others. "
            "Medieval Italian uses altrui freely; modern Italian prefers gli altri (others). "
            "Also used genetically: l'altrui = someone else's."
        ),
        "category": "function",
    },
    {
        "id": "allor",
        "italian": "allor / allora",
        "english": "then, at that point",
        "pos": "adverb (temporal)",
        "example_italian": "Allor fu la paura un poco queta",
        "example_english": "Then the fear was a little quieted",
        "note": (
            "From Latin ad + illam + horam (at that hour). Allor is the apocopated form. "
            "Used to mark a narrative turning point: then, at that moment. "
            "Appears again at line 136: Allor si mosse (Then he moved on). "
            "Modern Italian: allora (unchanged, also used as filler: well, so)."
        ),
        "category": "function",
    },
    {
        "id": "queto",
        "italian": "queto / quieto",
        "english": "quiet, stilled, calmed",
        "pos": "adjective",
        "example_italian": "Allor fu la paura un poco queta",
        "example_english": "Then the fear was a little quieted",
        "note": (
            "From Latin quietus (at rest, quiet). Queta is the feminine form, "
            "agreeing with paura (f.). La paura fu queta = the fear was quieted. "
            "The apocopated form queta (for quieta) is used for metre. "
            "Modern Italian: quieto/a (adj.), quietare (to calm, quieten)."
        ),
    },
    {
        "id": "compunto",
        "italian": "compunto",
        "english": "pierced, stricken, moved (with feeling)",
        "pos": "past participle / adjective (m.)",
        "example_italian": "che m'aveva di paura il cor compunto",
        "example_english": "that had pierced my heart with fear",
        "note": (
            "Past participle of compungere (to prick, pierce, sting), from Latin compungere "
            "(com- + pungere, to prick). Compunto agrees with cor (m.). "
            "M'aveva compunto il cor = had pierced my heart. "
            "In religious language compunto means contrite, moved to repentance "
            "(related to English 'compunction')."
        ),
    },
    {
        "id": "affannato",
        "italian": "affannato",
        "english": "breathless, exhausted, gasping",
        "pos": "past participle / adjective",
        "example_italian": "E come quei che con lena affannata",
        "example_english": "And like one who with laboured breath",
        "note": (
            "Past participle of affannare (to distress, to breathe with difficulty), "
            "from affanno (laboured breathing, anguish), possibly from Latin ad + *fannum. "
            "Affannata (feminine) agrees with lena (f.): laboured breath. "
            "Modern Italian: affannato (breathless, gasping); affanno (breathlessness, worry)."
        ),
    },
    {
        "id": "perigliosa",
        "italian": "periglioso / perigliosa",
        "english": "perilous, dangerous",
        "pos": "adjective",
        "example_italian": "si volge a l'acqua perigliosa e guata",
        "example_english": "turns to the perilous water and gazes",
        "note": (
            "From Latin periculum (danger, trial), via Old Italian periglio (= modern pericolo). "
            "Perigliosa is the feminine form agreeing with acqua (f.). "
            "The form periglio (for pericolo) is archaic/poetic. "
            "Related to English 'peril', 'perilous'. Modern Italian: pericoloso/a."
        ),
    },
    {
        "id": "diserto",
        "italian": "diserto",
        "english": "deserted, desolate",
        "pos": "adjective",
        "example_italian": "ripresi via per la piaggia diserta",
        "example_english": "I resumed my way along the deserted slope",
        "note": (
            "From Latin desertus (abandoned, desolate), past participle of deserere. "
            "Diserta is the feminine form agreeing with piaggia (f.). "
            "Gran diserto = great wasteland (line 64). "
            "Related to English 'desert', 'deserted', 'desertion'. "
            "Modern Italian: deserto/a (unchanged)."
        ),
    },
    {
        "id": "fermo",
        "italian": "fermo",
        "english": "firm, steady, fixed",
        "pos": "adjective",
        "example_italian": "sì che 'l piè fermo sempre era 'l più basso",
        "example_english": "so that the firm foot was always the lower",
        "note": (
            "From Latin firmus (firm, steadfast). Il piè fermo = the firm/stationary foot. "
            "In climbing a slope, one foot stays lower and steady while the other advances: "
            "the 'firm foot' is always the lower one. "
            "Related to English 'firm', 'infirmary'. Modern Italian: fermo/a."
        ),
    },
    {
        "id": "sempre",
        "italian": "sempre",
        "english": "always",
        "pos": "adverb",
        "example_italian": "sì che 'l piè fermo sempre era 'l più basso",
        "example_english": "so that the firm foot was always the lower",
        "note": (
            "From Latin semper (always). Unchanged in modern Italian. "
            "One of the most common adverbs in Italian poetry. "
            "Related to English expressions via Latin: semper fidelis (always faithful)."
        ),
        "category": "function",
    },
    {
        "id": "basso",
        "italian": "basso",
        "english": "low, lower",
        "pos": "adjective / adverb",
        "example_italian": "sì che 'l piè fermo sempre era 'l più basso",
        "example_english": "so that the firm foot was always the lower",
        "note": (
            "From Late Latin bassus (short, fat, low). "
            "Il più basso = the lower (one) — superlative/comparative with più. "
            "Also in line 61: in basso loco (in a low place). "
            "Related to English 'bass' (musical term), 'base', 'abase'. Modern Italian: basso/a."
        ),
    },
    {
        "id": "quasi",
        "italian": "quasi",
        "english": "almost, nearly",
        "pos": "adverb",
        "example_italian": "quasi al cominciar de l'erta",
        "example_english": "almost at the beginning of the steep",
        "note": (
            "From Latin quasi (as if, almost). Unchanged in modern Italian. "
            "Quasi introduces the dramatic entrance of the leopard: almost at the very start "
            "of the ascent, the beast appears. "
            "Related to English 'quasi-' (prefix meaning almost, seemingly)."
        ),
        "category": "function",
    },
    {
        "id": "leggero",
        "italian": "leggero / leggera",
        "english": "light, swift, nimble",
        "pos": "adjective",
        "example_italian": "una lonza leggera e presta molto",
        "example_english": "a leopard, light and very swift",
        "note": (
            "From Latin leviarius (from levis, light in weight). "
            "Leggera is the feminine form agreeing with lonza (f.). "
            "Combined with presta (swift), the two adjectives evoke the leopard's dangerous agility. "
            "Modern Italian: leggero/a (light in weight or character). "
            "Related to English 'levity' (via Latin levis)."
        ),
    },
    {
        "id": "presto",
        "italian": "presto",
        "english": "swift, ready; (adverb) quickly, soon",
        "pos": "adjective / adverb",
        "example_italian": "una lonza leggera e presta molto",
        "example_english": "a leopard, light and very swift",
        "note": (
            "From Latin praestus (ready, at hand), from praesto (available). "
            "Presta (feminine) agrees with lonza (f.). Molto = very. "
            "As adverb presto = quickly, soon (common in modern Italian). "
            "Borrowed into music: presto = fast tempo. Related to English 'presto' (as in presto!)."
        ),
    },
    {
        "id": "macolato",
        "italian": "macolato",
        "english": "spotted, mottled",
        "pos": "adjective",
        "example_italian": "che di pel macolato era coverta",
        "example_english": "that was covered with a spotted hide",
        "note": (
            "From Latin macula (spot, stain, blemish). "
            "Di pel macolato = with a spotted hide. The word is archaic/poetic; "
            "modern Italian uses macchiato or maculato (also used in zoological terminology). "
            "Related to English 'immaculate' (without spot, from im- + macula)."
        ),
    },
    {
        "id": "coperto",
        "italian": "coperto",
        "english": "covered",
        "pos": "past participle / adjective",
        "example_italian": "che di pel macolato era coverta",
        "example_english": "that was covered with a spotted hide",
        "note": (
            "Past participle of coprire (to cover), from Latin cooperire. "
            "Coverta is the older/poetic feminine form (= modern coperta). "
            "Era coverta = was covered (imperfect passive). "
            "Related to English 'cover', 'covert', 'discover'. "
            "Modern Italian: coperto/a (covered), scoperto/a (uncovered, discovered)."
        ),
    },
    {
        "id": "dinanzi",
        "italian": "dinanzi",
        "english": "before, in front of",
        "pos": "preposition / adverb",
        "example_italian": "e non mi si partia dinanzi al volto",
        "example_english": "and it did not depart from before my face",
        "note": (
            "From Latin de + in + antius (from before). "
            "Dinanzi al volto = before my face. "
            "Medieval Italian form; also dinanzi a = in front of. "
            "Modern Italian: davanti (a) is more common; dinanzi survives in formal/literary use."
        ),
        "category": "function",
    },
    {
        "id": "anzi",
        "italian": "anzi",
        "english": "rather, on the contrary; indeed",
        "pos": "adverb / conjunction (adversative)",
        "example_italian": "anzi 'mpediva tanto il mio cammino",
        "example_english": "rather, it so much impeded my advance",
        "note": (
            "From Latin ante (before, in front of → on the contrary). "
            "Adversative: introduces a stronger contradiction or intensification. "
            "Anzi = not merely not departing, but actively blocking. "
            "Modern Italian: anzi = on the contrary; indeed (often used to strengthen or correct)."
        ),
        "category": "function",
    },
    {
        "id": "retro",
        "italian": "retro / a retro",
        "english": "back, behind",
        "pos": "adverb",
        "example_italian": "si volse a retro a rimirar lo passo",
        "example_english": "turned back to gaze upon the pass",
        "note": (
            "From Latin retro (backwards, behind). A retro = backwards. "
            "Si volse a retro = turned himself back. "
            "Survives in modern Italian as a prefix (retro-: retrogrado, etc.) "
            "and in the phrase guardare indietro (to look back). "
            "Related to English 'retro', 'retrograde'."
        ),
        "category": "function",
    },
    {
        "id": "divino",
        "italian": "divino",
        "english": "divine",
        "pos": "adjective",
        "example_italian": "quando l'amor divino",
        "example_english": "when divine love",
        "note": (
            "From Latin divinus (of the gods, divine), from divus (god). "
            "L'amor divino = divine love, the creative force of God. "
            "Dante uses divino throughout the Commedia: la divina commedia, the poem's title. "
            "Related to English 'divine', 'divinity'. Unchanged in modern Italian."
        ),
    },
    {
        "id": "novo",
        "italian": "novo / nuovo",
        "english": "new",
        "pos": "adjective",
        "example_italian": "la stagion nova e l'ora del mattino",
        "example_english": "the new season and the hour of morning",
        "note": (
            "From Latin novus (new). Nova is the poetic/archaic form (= modern nuova). "
            "La stagion nova = the new season, spring. "
            "Dante prefers novo/nova in verse for metrical reasons. "
            "Related to English 'novel', 'novelty', 'innovate'. Modern Italian: nuovo/nuova."
        ),
    },
    {
        "id": "gaio",
        "italian": "gaio / gaìa",
        "english": "gay, bright, joyful",
        "pos": "adjective",
        "example_italian": "di quella fiera a la gaìa pelle",
        "example_english": "of that beast with the gay-coloured hide",
        "note": (
            "From Old Provençal gai (joyful, bright). Gaìa (with diaeresis on the i) is the feminine, "
            "marking that the i and a are pronounced as two separate syllables (ga-ì-a). "
            "A la gaìa pelle = with the bright/gay-coloured hide. "
            "In medieval usage, gai/gaio = joyful, lively, brightly coloured. "
            "Related to English 'gay' (in its original sense of bright, merry)."
        ),
    },
    {
        "id": "poscia",
        "italian": "poscia",
        "english": "afterwards, then, next",
        "pos": "adverb (temporal)",
        "example_italian": "la vista d'un leon che m'apparve poscia",
        "example_english": "the sight of a lion that afterwards appeared to me",
        "note": (
            "From Latin post + -ia. Archaic/poetic adverb, equivalent to poi or dopo. "
            "M'apparve poscia = appeared to me afterwards (after the leopard). "
            "Dante uses poscia frequently in the Commedia for narrative sequence. "
            "Modern Italian: poi, dopo; poscia survives in formal/literary use."
        ),
        "category": "function",
    },
    {
        "id": "prima",
        "italian": "prima",
        "english": "first, at first; before",
        "pos": "adverb / adjective",
        "example_italian": "mosse di prima quelle cose belle",
        "example_english": "first moved those beautiful things",
        "note": (
            "From Latin prima (feminine of primus, first). "
            "Di prima = first, for the first time, at the beginning. "
            "Refers to the first moment of Creation when divine love set the heavens in motion. "
            "Modern Italian: prima (first, before) — unchanged. Related to English 'primary', 'prime'."
        ),
        "category": "function",
    },
    {
        "id": "bello",
        "italian": "bello / bella",
        "english": "beautiful, fair",
        "pos": "adjective",
        "example_italian": "mosse di prima quelle cose belle",
        "example_english": "first moved those beautiful things",
        "note": (
            "From Latin bellus (fine, pretty). Belle is the feminine plural, agreeing with cose (f. pl.). "
            "Quelle cose belle = those beautiful things (the heavenly bodies/the world at Creation). "
            "Related to English 'belle', 'belladonna', 'embellish'. Modern Italian: bello/bella."
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
    {
        "id": "s4",
        "lines": (10, 12),
        "italian": (
            "Io non so ben ridir com'i' v'intrai,\n"
            "tant'era pien di sonno a quel punto\n"
            "che la verace via abbandonai."
        ),
        "vocab_ids": [
            "essere", "adv_non", "dire", "ben", "adv_vi",
            "tanto", "sonno", "al", "poco", "verace", "via", "abbandonare",
            "conj_che", "art_la",
        ],
        "verb_highlights": {
            "essere":      [{"tense": "imperfect",      "person_idx": 0}],  # tant'era
            "dire":        [{"tense": "present",        "person_idx": 0}],  # so … ridir (infinitive)
            "abbandonare": [{"tense": "passato_remoto", "person_idx": 0}],  # abbandonai
        },
        "word_order": [
            {
                "line": 10,
                "tokens": ["Io", "non", "so", "ben", "ridir", "com'i'", "v'intrai,"],
                "translation": "I do not know well how to tell again how I entered there,",
                "hint": (
                    "So = I know (1st sg. present of sapere). Ridir = ridire (to re-tell), "
                    "apocopated infinitive. Com'i' = come io (how I). "
                    "V'intrai = vi entrai (I entered there), passato remoto of entrare."
                ),
            },
            {
                "line": 11,
                "tokens": ["tant'era", "pien", "di", "sonno", "a", "quel", "punto"],
                "translation": "so full of sleep was I at that point",
                "hint": (
                    "Tant'era = tanto era (elision before e): so much was I. "
                    "Pien = pieno (full), apocopated. Di sonno = of sleep. "
                    "A quel punto = at that point."
                ),
            },
            {
                "line": 12,
                "tokens": ["che", "la", "verace", "via", "abbandonai."],
                "translation": "that I abandoned the true way.",
                "hint": (
                    "Che introduces a result clause: so full of sleep … that I abandoned. "
                    "Verace = true, genuine (from Latin verax). Abbandonai = I abandoned "
                    "(1st sg. passato remoto)."
                ),
            },
        ],
        "translation": {
            "lines": (10, 12),
            "prompt": (
                "I not know well to tell again how I there entered,\n"
                "so much was full of sleep at that point\n"
                "that the true way I abandoned."
            ),
            "italian": (
                "Io non so ben ridir com'i' v'intrai,\n"
                "tant'era pien di sonno a quel punto\n"
                "che la verace via abbandonai."
            ),
            "note": (
                "Com'i' = come io: the pronoun io contracts after come. "
                "V'intrai = vi entrai: vi (there) elides to v' before a vowel. "
                "The result clause (tanto … che) explains not just how Dante lost his way, "
                "but implies moral as well as physical sleep — spiritual negligence."
            ),
        },
    },
    {
        "id": "s5",
        "lines": (13, 15),
        "italian": (
            "Ma poi ch'i' fui al piè d'un colle giunto,\n"
            "là dove terminava quella valle\n"
            "che m'aveva di paura il cor compunto,"
        ),
        "vocab_ids": [
            "conj_ma", "conj_poi", "essere", "al", "pie", "prep_di", "art_un",
            "colle", "adv_là", "terminare", "valle", "conj_che",
            "avere", "paura", "art_il", "cor", "compunto",
        ],
        "verb_highlights": {
            "essere":    [{"tense": "passato_remoto", "person_idx": 0}],  # fui
            "terminare": [{"tense": "imperfect",      "person_idx": 2}],  # terminava
            "avere":     [{"tense": "imperfect",      "person_idx": 2}],  # m'aveva (pluperfect)
        },
        "word_order": [
            {
                "line": 13,
                "tokens": ["Ma", "poi", "ch'i'", "fui", "al", "piè", "d'un", "colle", "giunto,"],
                "translation": "But when I had arrived at the foot of a hill,",
                "hint": (
                    "Poi ch'i' = poi che io (once that I, when I). Fui = I was/I had been "
                    "(passato remoto of essere). Giunto = arrived (past participle of giungere). "
                    "Al piè = at the foot (al = a + il). D'un = di + un."
                ),
            },
            {
                "line": 14,
                "tokens": ["là", "dove", "terminava", "quella", "valle"],
                "translation": "there where that valley ended",
                "hint": (
                    "Là dove = there where (introduces a relative place clause). "
                    "Terminava = was ending (imperfect of terminare). "
                    "Quella valle = that valley (quella is the demonstrative feminine)."
                ),
            },
            {
                "line": 15,
                "tokens": ["che", "m'aveva", "di", "paura", "il", "cor", "compunto,"],
                "translation": "that had pierced my heart with fear,",
                "hint": (
                    "Che = which (relative pronoun, referring to the valley). "
                    "M'aveva compunto = had pierced me (pluperfect: aveva + past participle). "
                    "Di paura = with fear. Il cor = the heart (cor = cuore, apocopated)."
                ),
            },
        ],
        "translation": {
            "lines": (13, 15),
            "prompt": (
                "But when I at the foot of a hill arrived,\n"
                "there where was ending that valley\n"
                "that had me with fear the heart pierced,"
            ),
            "italian": (
                "Ma poi ch'i' fui al piè d'un colle giunto,\n"
                "là dove terminava quella valle\n"
                "che m'aveva di paura il cor compunto,"
            ),
            "note": (
                "Giunto is a past participle used predicatively after fui: 'I was arrived' = 'I had arrived'. "
                "The Italian object order differs from English: m'aveva di paura il cor compunto "
                "places the subject (il cor) after the past participle (compunto), a common Dantesque inversion. "
                "Compunto derives from Latin compungere (to prick); related to 'compunction'."
            ),
        },
    },
    {
        "id": "s6",
        "lines": (16, 18),
        "italian": (
            "guardai in alto e vidi le sue spalle\n"
            "vestite già de' raggi del pianeta\n"
            "che mena dritto altrui per ogni calle;"
        ),
        "vocab_ids": [
            "guardare", "prep_in", "alto", "conj_e", "vedere", "art_le", "spalle",
            "adv_già", "raggio", "del", "pianeta",
            "conj_che", "menare", "dritto", "altrui", "prep_per", "calle",
        ],
        "verb_highlights": {
            "guardare": [{"tense": "passato_remoto", "person_idx": 0}],  # guardai
            "vedere":   [{"tense": "passato_remoto", "person_idx": 0}],  # vidi
            "menare":   [{"tense": "present",        "person_idx": 2}],  # mena
        },
        "word_order": [
            {
                "line": 16,
                "tokens": ["guardai", "in", "alto", "e", "vidi", "le", "sue", "spalle"],
                "translation": "I looked up high and saw its shoulders",
                "hint": (
                    "Guardai and vidi are both 1st person singular passato remoto. "
                    "In alto = up high (in + alto used adverbially). "
                    "Sue spalle = its shoulders (sue is the possessive agreeing with spalle, f. pl.)."
                ),
            },
            {
                "line": 17,
                "tokens": ["vestite", "già", "de'", "raggi", "del", "pianeta"],
                "translation": "already clothed in the rays of the planet",
                "hint": (
                    "Vestite = clothed (past participle, feminine plural agreeing with spalle). "
                    "Già = already. De' = dei = di + i (of the). "
                    "Pianeta = the sun (Ptolemaic cosmology: the sun is one of seven planets)."
                ),
            },
            {
                "line": 18,
                "tokens": ["che", "mena", "dritto", "altrui", "per", "ogni", "calle;"],
                "translation": "that leads others straight along every path;",
                "hint": (
                    "Che = which (relative, referring to the sun/planet). "
                    "Mena = leads (present of menare). Dritto = straight (adverb). "
                    "Altrui = others (invariable pronoun). Calle = path, lane (archaic)."
                ),
            },
        ],
        "translation": {
            "lines": (16, 18),
            "prompt": (
                "I looked up high and saw its shoulders\n"
                "clothed already with the rays of the planet\n"
                "that leads straight others along every path;"
            ),
            "italian": (
                "guardai in alto e vidi le sue spalle\n"
                "vestite già de' raggi del pianeta\n"
                "che mena dritto altrui per ogni calle;"
            ),
            "note": (
                "The hill's 'shoulders' are a bold personification. "
                "The planet = the sun; de' = dei (di + i, of the) contracted poetically. "
                "The sun leads creatures to their proper path, making it a symbol of right reason "
                "and divine guidance. Mena (present tense) stresses the sun's ongoing, universal action."
            ),
        },
    },
    {
        "id": "s7",
        "lines": (19, 21),
        "italian": (
            "Allor fu la paura un poco queta,\n"
            "che nel lago del cor m'era durata\n"
            "la notte ch'i' passai con tanta pieta."
        ),
        "vocab_ids": [
            "allor", "essere", "art_la", "paura", "art_un", "poco", "queto",
            "conj_che", "nel", "lago", "del", "cor", "pron_mi", "durare",
            "notte", "passare", "prep_con", "tanto", "pieta",
        ],
        "verb_highlights": {
            "essere":  [{"tense": "passato_remoto", "person_idx": 2}],  # fu
            "durare":  [{"tense": "imperfect",      "person_idx": 2}],  # m'era durata (pluperfect)
            "passare": [{"tense": "passato_remoto", "person_idx": 0}],  # passai
        },
        "word_order": [
            {
                "line": 19,
                "tokens": ["Allor", "fu", "la", "paura", "un", "poco", "queta,"],
                "translation": "Then the fear was a little quieted,",
                "hint": (
                    "Allor = allora (then), apocopated. Fu = it was (passato remoto of essere, 3rd sg.). "
                    "Queta = quieted, stilled (feminine, agreeing with paura). "
                    "Un poco = a little."
                ),
            },
            {
                "line": 20,
                "tokens": ["che", "nel", "lago", "del", "cor", "m'era", "durata"],
                "translation": "that had lasted in the lake of my heart",
                "hint": (
                    "Che = which (relative, referring to paura). "
                    "Nel lago del cor = in the lake of the heart (metaphor). "
                    "M'era durata = had lasted to me (pluperfect: era + past participle)."
                ),
            },
            {
                "line": 21,
                "tokens": ["la", "notte", "ch'i'", "passai", "con", "tanta", "pieta."],
                "translation": "through the night that I had passed with such great pity.",
                "hint": (
                    "La notte is the subject of m'era durata (the fear had lasted … through the night). "
                    "Ch'i' = che io (that I). Passai = I passed (passato remoto). "
                    "Pieta (without accent) = pity, grief; con tanta pieta = with such great anguish."
                ),
            },
        ],
        "translation": {
            "lines": (19, 21),
            "prompt": (
                "Then was the fear a little quieted,\n"
                "that in the lake of the heart had lasted to me\n"
                "the night that I passed with such great pity."
            ),
            "italian": (
                "Allor fu la paura un poco queta,\n"
                "che nel lago del cor m'era durata\n"
                "la notte ch'i' passai con tanta pieta."
            ),
            "note": (
                "Nel lago del cor is a striking metaphor: fear pooled like a lake in the heart. "
                "M'era durata: the dative mi (to me) expresses personal involvement with the lasting fear. "
                "Pieta (without accent) = compassion/pity/grief; distinct from pietà (piety). "
                "The pluperfect m'era durata indicates the fear preceded and lasted through the night already past."
            ),
        },
    },
    {
        "id": "s8",
        "lines": (22, 24),
        "italian": (
            "E come quei che con lena affannata,\n"
            "uscito fuor del pelago a la riva,\n"
            "si volge a l'acqua perigliosa e guata,"
        ),
        "vocab_ids": [
            "conj_e", "pron_si", "lena", "affannato", "prep_con",
            "pelago", "prep_a", "riva", "volgere", "acqua", "perigliosa", "guatare",
            "prep_di",
        ],
        "verb_highlights": {
            "volgere": [{"tense": "present", "person_idx": 2}],  # si volge
            "guatare": [{"tense": "present", "person_idx": 2}],  # guata
        },
        "word_order": [
            {
                "line": 22,
                "tokens": ["E", "come", "quei", "che", "con", "lena", "affannata,"],
                "translation": "And like one who with laboured breath,",
                "hint": (
                    "Come = like, as (introducing a simile). "
                    "Quei = colui, that one (demonstrative pronoun, subject of si volge). "
                    "Lena affannata = laboured breath (lena = breath; affannata = gasping, f.)."
                ),
            },
            {
                "line": 23,
                "tokens": ["uscito", "fuor", "del", "pelago", "a", "la", "riva,"],
                "translation": "having come out of the open sea to the shore,",
                "hint": (
                    "Uscito = having exited/come out (past participle of uscire, used absolutely). "
                    "Fuor del = fuori dal (out of). Pelago = open sea (literary/archaic). "
                    "A la riva = to the shore."
                ),
            },
            {
                "line": 24,
                "tokens": ["si", "volge", "a", "l'acqua", "perigliosa", "e", "guata,"],
                "translation": "turns to the perilous water and gazes,",
                "hint": (
                    "Si volge = turns (reflexive, 3rd sg. present of volgere). "
                    "A l'acqua = a + l'acqua (elision). Perigliosa = perilous, dangerous (archaic form). "
                    "Guata = gazes intently (present of guatare, archaic/poetic verb)."
                ),
            },
        ],
        "translation": {
            "lines": (22, 24),
            "prompt": (
                "And like one who with breath laboured,\n"
                "having come out from the open sea to the shore,\n"
                "turns to the perilous water and gazes,"
            ),
            "italian": (
                "E come quei che con lena affannata,\n"
                "uscito fuor del pelago a la riva,\n"
                "si volge a l'acqua perigliosa e guata,"
            ),
            "note": (
                "This is a classic Dantesque epic simile: come … così (as … so), completed at line 25. "
                "Quei = colui che (the one who) — an archaic demonstrative. "
                "Pelago (open sea) is elevated literary vocabulary, from Greek pelagos. "
                "Guatare (to stare, gaze) is an archaic/Germanic verb, distinct from guardare."
            ),
        },
    },
    {
        "id": "s9",
        "lines": (25, 27),
        "italian": (
            "così l'animo mio, ch'ancor fuggiva,\n"
            "si volse a retro a rimirar lo passo\n"
            "che non lasciò già mai persona viva."
        ),
        "vocab_ids": [
            "animo", "fuggire", "pron_si", "volgere", "retro", "rimirare",
            "passo", "conj_che", "adv_non", "adv_già", "adv_mai", "persona",
        ],
        "verb_highlights": {
            "fuggire":  [{"tense": "imperfect",      "person_idx": 2}],  # fuggiva
            "volgere":  [{"tense": "passato_remoto", "person_idx": 2}],  # si volse
            "rimirare": [],  # rimirar is apocopated infinitive
        },
        "word_order": [
            {
                "line": 25,
                "tokens": ["così", "l'animo", "mio,", "ch'ancor", "fuggiva,"],
                "translation": "so my spirit, which was still fleeing,",
                "hint": (
                    "Così = so, thus (completing the simile begun with come at line 22). "
                    "L'animo mio = my spirit/mind (l' = il, elided before vowel). "
                    "Ch'ancor = che ancora (which still). Fuggiva = was fleeing (imperfect)."
                ),
            },
            {
                "line": 26,
                "tokens": ["si", "volse", "a", "retro", "a", "rimirar", "lo", "passo"],
                "translation": "turned back to gaze upon the pass",
                "hint": (
                    "Si volse = turned itself (passato remoto reflexive of volgere). "
                    "A retro = backwards. A rimirar = to gaze upon (a + apocopated infinitive). "
                    "Lo passo = the pass (lo is the archaic article = il before p-)."
                ),
            },
            {
                "line": 27,
                "tokens": ["che", "non", "lasciò", "già", "mai", "persona", "viva."],
                "translation": "that never yet had left any person alive.",
                "hint": (
                    "Che = which (relative, referring to the pass). "
                    "Non … già mai = never ever (triple negation: non + già + mai). "
                    "Lasciò = left (3rd sg. passato remoto of lasciare). "
                    "Persona viva = a living person / anyone alive."
                ),
            },
        ],
        "translation": {
            "lines": (25, 27),
            "prompt": (
                "so my spirit, which still was fleeing,\n"
                "turned itself back to gaze upon the pass\n"
                "that not ever yet a person living left."
            ),
            "italian": (
                "così l'animo mio, ch'ancor fuggiva,\n"
                "si volse a retro a rimirar lo passo\n"
                "che non lasciò già mai persona viva."
            ),
            "note": (
                "The simile (come … così) spans lines 22–26. "
                "Non lasciò già mai: Dante intensifies the negative with three words "
                "— non, già, and mai — a common medieval Italian emphatic pattern. "
                "Lo passo (not il passo) illustrates the archaic article lo before p-. "
                "The soul looks back even while still fleeing, capturing the psychology of escape."
            ),
        },
    },
    {
        "id": "s10",
        "lines": (28, 30),
        "italian": (
            "Poi ch'èi posato un poco il corpo lasso,\n"
            "ripresi via per la piaggia diserta,\n"
            "sì che 'l piè fermo sempre era 'l più basso."
        ),
        "vocab_ids": [
            "conj_poi", "posare", "poco", "corpo", "lasso",
            "riprendere", "via", "prep_per", "art_la", "piaggia", "diserto",
            "adv_sì", "pie", "fermo", "sempre", "essere", "piu", "basso",
        ],
        "verb_highlights": {
            "posare":    [{"tense": "past_participle", "person_idx": 0}],  # posato
            "riprendere":[{"tense": "passato_remoto",  "person_idx": 0}],  # ripresi
            "essere":    [{"tense": "imperfect",       "person_idx": 2}],  # era
        },
        "word_order": [
            {
                "line": 28,
                "tokens": ["Poi", "ch'èi", "posato", "un", "poco", "il", "corpo", "lasso,"],
                "translation": "After I had rested a little the weary body,",
                "hint": (
                    "Poi ch'èi = poi che io ho (after I have/had). "
                    "Posato = rested (past participle of posare). "
                    "Il corpo lasso = the weary body (lasso = weary, from Latin laxus)."
                ),
            },
            {
                "line": 29,
                "tokens": ["ripresi", "via", "per", "la", "piaggia", "diserta,"],
                "translation": "I resumed my way along the deserted slope,",
                "hint": (
                    "Ripresi = I resumed (1st sg. passato remoto of riprendere). "
                    "Via = way (here the object). Per = along, through. "
                    "Piaggia diserta = deserted slope (piaggia = hillside; diserta = deserted, f.)."
                ),
            },
            {
                "line": 30,
                "tokens": ["sì", "che", "'l", "piè", "fermo", "sempre", "era", "'l", "più", "basso."],
                "translation": "so that the firm foot was always the lower.",
                "hint": (
                    "Sì che = so that (result clause). 'l = il (article, elided). "
                    "Il piè fermo = the firm foot (the downhill foot in climbing). "
                    "Sempre era il più basso = was always the lower (comparative: più basso)."
                ),
            },
        ],
        "translation": {
            "lines": (28, 30),
            "prompt": (
                "After I had rested a little the body weary,\n"
                "I resumed my way along the slope deserted,\n"
                "so that the foot firm always was the more low."
            ),
            "italian": (
                "Poi ch'èi posato un poco il corpo lasso,\n"
                "ripresi via per la piaggia diserta,\n"
                "sì che 'l piè fermo sempre era 'l più basso."
            ),
            "note": (
                "Ch'èi posato is an archaic contracted form of che io ho posato (after I have rested). "
                "Piè fermo: the 'firm foot' is the lower, steadying foot when climbing a steep slope — "
                "the image vividly conveys the difficulty of ascending. "
                "Sì che here introduces a result or manner clause: in such a way that / so that."
            ),
        },
    },
    {
        "id": "s11",
        "lines": (31, 33),
        "italian": (
            "Ed ecco, quasi al cominciar de l'erta,\n"
            "una lonza leggera e presta molto,\n"
            "che di pel macolato era coverta;"
        ),
        "vocab_ids": [
            "conj_e", "interj_ecco", "quasi", "al", "cominciare", "erta",
            "art_un", "lonza", "leggero", "presto", "tanto",
            "conj_che", "pelo", "macolato", "essere", "coperto",
        ],
        "verb_highlights": {
            "essere": [{"tense": "imperfect", "person_idx": 2}],  # era coverta
        },
        "word_order": [
            {
                "line": 31,
                "tokens": ["Ed", "ecco,", "quasi", "al", "cominciar", "de", "l'erta,"],
                "translation": "And behold, almost at the beginning of the steep,",
                "hint": (
                    "Ed = e (and), used before a vowel to avoid hiatus. "
                    "Ecco = behold, here (presentative adverb). Quasi = almost. "
                    "Al cominciar = at the beginning (al + infinitive used as noun). "
                    "De l'erta = di la erta (of/at the steep slope)."
                ),
            },
            {
                "line": 32,
                "tokens": ["una", "lonza", "leggera", "e", "presta", "molto,"],
                "translation": "a leopard, light and very swift,",
                "hint": (
                    "Una lonza: the subject of this tercet finally arrives — the leopard. "
                    "Leggera = light (f., agreeing with lonza). Presta = swift, ready (f.). "
                    "Molto = very. Both adjectives agree in gender with lonza (f.)."
                ),
            },
            {
                "line": 33,
                "tokens": ["che", "di", "pel", "macolato", "era", "coverta;"],
                "translation": "that was covered with a spotted hide;",
                "hint": (
                    "Che = which (relative, referring to the lonza). "
                    "Di pel macolato = with a spotted hide (pel = pelo, apocopated). "
                    "Era coverta = was covered (imperfect passive; coverta is poetic for coperta)."
                ),
            },
        ],
        "translation": {
            "lines": (31, 33),
            "prompt": (
                "And behold, almost at the beginning of the steep,\n"
                "a leopard light and swift very,\n"
                "that with hide spotted was covered;"
            ),
            "italian": (
                "Ed ecco, quasi al cominciar de l'erta,\n"
                "una lonza leggera e presta molto,\n"
                "che di pel macolato era coverta;"
            ),
            "note": (
                "Ed ecco is a dramatic presentative formula (from Latin ecce, look!). "
                "The leopard appears as a sudden obstacle almost at the very start of the ascent — "
                "the irony is sharp. Lonza: the exact species is debated; most identify it as a leopard. "
                "Coverta (for coperta) is an archaic feminine past participle."
            ),
        },
    },
    {
        "id": "s12",
        "lines": (34, 36),
        "italian": (
            "e non mi si partia dinanzi al volto,\n"
            "anzi 'mpediva tanto il mio cammino,\n"
            "che fu per tornare più volte vòlto."
        ),
        "vocab_ids": [
            "conj_e", "adv_non", "pron_mi", "pron_si", "partire", "dinanzi", "al", "volto",
            "anzi", "impedire", "tanto", "cammino",
            "conj_che", "essere", "prep_per", "tornare", "piu", "volgere",
        ],
        "verb_highlights": {
            "partire":  [{"tense": "imperfect",      "person_idx": 2}],  # partia (= partiva)
            "impedire": [{"tense": "imperfect",      "person_idx": 2}],  # 'mpediva
            "essere":   [{"tense": "passato_remoto", "person_idx": 2}],  # fu
            "tornare":  [],  # infinitive after fu per
        },
        "word_order": [
            {
                "line": 34,
                "tokens": ["e", "non", "mi", "si", "partia", "dinanzi", "al", "volto,"],
                "translation": "and it did not depart from before my face,",
                "hint": (
                    "Non mi si partia = did not depart from before me. "
                    "Mi si = to me (double clitic). Partia = partiva (syncopated imperfect). "
                    "Dinanzi al volto = before my face (dinanzi = in front of; volto = face)."
                ),
            },
            {
                "line": 35,
                "tokens": ["anzi", "'mpediva", "tanto", "il", "mio", "cammino,"],
                "translation": "rather, it so much impeded my advance,",
                "hint": (
                    "Anzi = rather, on the contrary (adversative — not just failing to leave, but actively blocking). "
                    "'Mpediva = impediva (imperfect of impedire), the initial vowel elided. "
                    "Tanto = so much. Il mio cammino = my advance, my path."
                ),
            },
            {
                "line": 36,
                "tokens": ["che", "fu", "per", "tornare", "più", "volte", "vòlto."],
                "translation": "that many times it/I was turned back to return.",
                "hint": (
                    "Che introduces a result clause. Fu per + infinitive = was about to / was forced to. "
                    "Più volte = many times. Vòlto = turned (past participle of volgere, with accent "
                    "marking the stressed syllable, and punning on volto = face at line 34)."
                ),
            },
        ],
        "translation": {
            "lines": (34, 36),
            "prompt": (
                "and not to me departed from before the face,\n"
                "rather it impeded so much my advance,\n"
                "that it was on the point of turning many times turned."
            ),
            "italian": (
                "e non mi si partia dinanzi al volto,\n"
                "anzi 'mpediva tanto il mio cammino,\n"
                "che fu per tornare più volte vòlto."
            ),
            "note": (
                "Partia = partiva: medieval Italian syncopates -iva to -ia in the imperfect of -ire verbs. "
                "Anzi escalates: the beast does not merely stay — it actively blocks. "
                "Vòlto as past participle of volgere puns with volto (face) at line 34, a typical Dantesque wordplay. "
                "Fu per tornare: the construction fu per + infinitive = was on the point of / was forced to."
            ),
        },
    },
    {
        "id": "s13",
        "lines": (37, 39),
        "italian": (
            "Temp'era dal principio del mattino,\n"
            "e 'l sol montava 'n sù con quelle stelle\n"
            "ch'eran con lui quando l'amor divino"
        ),
        "vocab_ids": [
            "tempo", "essere", "prep_da", "principio", "del", "mattino",
            "conj_e", "sole", "montare", "stella",
            "conj_quando", "amor", "divino",
        ],
        "verb_highlights": {
            "essere":  [
                {"tense": "imperfect", "person_idx": 2},   # Temp'era
                {"tense": "imperfect", "person_idx": 5},   # ch'eran
            ],
            "montare": [{"tense": "imperfect", "person_idx": 2}],  # montava
        },
        "word_order": [
            {
                "line": 37,
                "tokens": ["Temp'era", "dal", "principio", "del", "mattino,"],
                "translation": "It was the time from the beginning of morning,",
                "hint": (
                    "Temp'era = tempo era (elision before e): it was the time / it was the season. "
                    "Dal principio = from the beginning (da + il = dal). "
                    "Del mattino = of the morning."
                ),
            },
            {
                "line": 38,
                "tokens": ["e", "'l", "sol", "montava", "'n", "sù", "con", "quelle", "stelle"],
                "translation": "and the sun was climbing upward with those stars",
                "hint": (
                    "'l = il (elided). Sol = sole (apocopated). Montava = was climbing (imperfect). "
                    "'n sù = in su (upward): double elision common in Dante. "
                    "Quelle stelle = those stars (Aries, the spring constellation)."
                ),
            },
            {
                "line": 39,
                "tokens": ["ch'eran", "con", "lui", "quando", "l'amor", "divino"],
                "translation": "that were with it when divine love",
                "hint": (
                    "Ch'eran = che erano (that were), with elision. Con lui = with it (the sun). "
                    "Quando = when. L'amor = il + amor (elision). "
                    "Divino = divine (adjective modifying amor)."
                ),
            },
        ],
        "translation": {
            "lines": (37, 39),
            "prompt": (
                "It was the time from the beginning of morning,\n"
                "and the sun was climbing upward with those stars\n"
                "that were with it when divine love"
            ),
            "italian": (
                "Temp'era dal principio del mattino,\n"
                "e 'l sol montava 'n sù con quelle stelle\n"
                "ch'eran con lui quando l'amor divino"
            ),
            "note": (
                "Dante places the encounter in the spring at sunrise — "
                "the sun in Aries, the same configuration medieval tradition assigned to Creation. "
                "This tercet opens a longer sentence ending at line 43; the verse structure enacts suspense. "
                "Sol = apocopated sole; 'n sù = in su (upward). Ch'eran = che erano."
            ),
        },
    },
    {
        "id": "s14",
        "lines": (40, 42),
        "italian": (
            "mosse di prima quelle cose belle;\n"
            "sì ch'a bene sperar m'era cagione\n"
            "di quella fiera a la gaìa pelle"
        ),
        "vocab_ids": [
            "muovere", "prima", "cosa", "bello",
            "adv_sì", "ben", "sperare", "pron_mi", "essere", "cagione",
            "prep_di", "fiera", "prep_a", "gaio", "pelle",
        ],
        "verb_highlights": {
            "muovere": [{"tense": "passato_remoto", "person_idx": 2}],  # mosse
            "sperare": [],  # sperar is apocopated infinitive
            "essere":  [{"tense": "imperfect",      "person_idx": 2}],  # m'era
        },
        "word_order": [
            {
                "line": 40,
                "tokens": ["mosse", "di", "prima", "quelle", "cose", "belle;"],
                "translation": "first moved those beautiful things;",
                "hint": (
                    "Mosse = moved (3rd sg. passato remoto of muovere). "
                    "Di prima = for the first time, at first. "
                    "Quelle cose belle = those beautiful things (the heavens, at Creation). "
                    "Belle is the feminine plural agreeing with cose (f. pl.)."
                ),
            },
            {
                "line": 41,
                "tokens": ["sì", "ch'a", "bene", "sperar", "m'era", "cagione"],
                "translation": "so that it gave me cause to hope for good",
                "hint": (
                    "Sì ch'a = sì che a (so that, followed by the infinitive phrase). "
                    "Bene sperar = to hope for good (ben = bene, adverb; sperar = apocopated infinitive). "
                    "M'era cagione = was (a) cause to me / gave me reason."
                ),
            },
            {
                "line": 42,
                "tokens": ["di", "quella", "fiera", "a", "la", "gaìa", "pelle"],
                "translation": "of that beast with the gay-coloured hide",
                "hint": (
                    "Di quella fiera = of that beast (the leopard). "
                    "A la gaìa pelle = with the bright/gay hide (a la = with). "
                    "Gaìa (note diaeresis: two syllables ga-ì-a). Pelle = skin, hide."
                ),
            },
        ],
        "translation": {
            "lines": (40, 42),
            "prompt": (
                "moved at first those things beautiful;\n"
                "so that to good to hope to me was cause\n"
                "of that beast with the gay hide"
            ),
            "italian": (
                "mosse di prima quelle cose belle;\n"
                "sì ch'a bene sperar m'era cagione\n"
                "di quella fiera a la gaìa pelle"
            ),
            "note": (
                "The subject of mosse is l'amor divino (line 39): divine love first moved the heavens. "
                "Sì ch'a bene sperar m'era cagione: the spring sunrise gives Dante hope despite the beast. "
                "Gaìa: the diaeresis (two dots over ì) signals that i and a are separate syllables, "
                "maintaining the poem's hendecasyllabic metre."
            ),
        },
    },
    {
        "id": "s15",
        "lines": (43, 45),
        "italian": (
            "la stagion nova e l'ora del mattino;\n"
            "ma non sì che paura non mi desse\n"
            "la vista d'un leon che m'apparve poscia."
        ),
        "vocab_ids": [
            "stagione", "novo", "conj_e", "ora", "del", "mattino",
            "conj_ma", "adv_non", "adv_sì", "paura", "pron_mi", "dare",
            "art_la", "vista", "art_un", "leone", "conj_che", "apparire", "poscia",
        ],
        "verb_highlights": {
            "dare":    [{"tense": "imperfect", "person_idx": 2}],  # desse (imperfect subjunctive)
            "apparire":[{"tense": "passato_remoto", "person_idx": 2}],  # apparve
        },
        "word_order": [
            {
                "line": 43,
                "tokens": ["la", "stagion", "nova", "e", "l'ora", "del", "mattino;"],
                "translation": "the new season and the hour of morning;",
                "hint": (
                    "Stagion = stagione (apocopated). Nova = nuova (new), archaic/poetic form. "
                    "L'ora = la + ora (elision). Del mattino = of the morning. "
                    "These are the subjects (with di quella fiera, line 42) of m'era cagione."
                ),
            },
            {
                "line": 44,
                "tokens": ["ma", "non", "sì", "che", "paura", "non", "mi", "desse"],
                "translation": "but not so much that fear did not give me",
                "hint": (
                    "Ma = but (adversative turn). Non sì che = not so much that. "
                    "Desse = imperfect subjunctive of dare (might give, would give). "
                    "The double non (non sì … non desse) is emphatic: the fear does grip him."
                ),
            },
            {
                "line": 45,
                "tokens": ["la", "vista", "d'un", "leon", "che", "m'apparve", "poscia."],
                "translation": "the sight of a lion that afterwards appeared to me.",
                "hint": (
                    "La vista = the sight (subject of desse). D'un = di + un. "
                    "Leon = leone (apocopated). M'apparve = appeared to me "
                    "(apparve is 3rd sg. passato remoto of apparire). "
                    "Poscia = afterwards (archaic adverb)."
                ),
            },
        ],
        "translation": {
            "lines": (43, 45),
            "prompt": (
                "the season new and the hour of morning;\n"
                "but not so much that fear not to me gave\n"
                "the sight of a lion that to me appeared afterwards."
            ),
            "italian": (
                "la stagion nova e l'ora del mattino;\n"
                "ma non sì che paura non mi desse\n"
                "la vista d'un leon che m'apparve poscia."
            ),
            "note": (
                "Stagion nova and l'ora del mattino are the final subjects of the long sentence "
                "beginning at line 37: the spring morning gave cause for hope … but not enough. "
                "Desse is an imperfect subjunctive (3rd sg. of dare), expressing what the hope "
                "was not sufficient to prevent. The double negative (non sì … non mi desse) "
                "confirms that fear wins: the lion does frighten him. "
                "Poscia (afterwards) is an archaic adverb equivalent to modern poi or dopo."
            ),
        },
    },
    {
        "id": "s16",
        "lines": (46, 48),
        "italian": (
            "Questi parea che contra me venisse\n"
            "con la test'alta e con rabbiosa fame,\n"
            "sì che parea che l'aere ne tremesse;"
        ),
        "literal": [
            "This one seemed that against me he was coming",
            "with head high and with rabid hunger,",
            "so that it seemed that the air thereof trembled;",
        ],
    },
    {
        "id": "s17",
        "lines": (49, 51),
        "italian": (
            "ed una lupa, che di tutte brame\n"
            "sembrava carca ne la sua magrezza,\n"
            "e molte genti fé già viver grame,"
        ),
        "literal": [
            "and a she-wolf, who of all cravings",
            "seemed laden in her leanness,",
            "and many peoples has made already to live in misery,",
        ],
    },
    {
        "id": "s18",
        "lines": (52, 54),
        "italian": (
            "questa mi porse tanto di gravezza\n"
            "con la paura ch'uscia di sua vista,\n"
            "che io perdei la speranza de l'altezza."
        ),
        "literal": [
            "this one upon me laid such weight of heaviness",
            "with the fear that issued from her sight,",
            "that I lost the hope of the height.",
        ],
    },
    {
        "id": "s19",
        "lines": (55, 57),
        "italian": (
            "E qual è quei che volentieri acquista,\n"
            "e giugne 'l tempo che perder lo face,\n"
            "che 'n tutt'i suoi pensier piange e s'attrista;"
        ),
        "literal": [
            "And such as is he who willingly acquires,",
            "and the time arrives that makes him lose,",
            "that in all his thoughts he weeps and grows sad;",
        ],
    },
    {
        "id": "s20",
        "lines": (58, 60),
        "italian": (
            "tal mi fece la bestia sanza pace,\n"
            "che, venendomi 'ncontro, a poco a poco\n"
            "mi ripigneva là dove 'l sol tace."
        ),
        "literal": [
            "such did make me the beast without peace,",
            "which, coming against me, little by little",
            "was driving me back there where the sun is silent.",
        ],
    },
    {
        "id": "s21",
        "lines": (61, 63),
        "italian": (
            "Mentre ch'i' rovinava in basso loco,\n"
            "dinanzi a li occhi mi si fu offerto\n"
            "chi per lungo silenzio parea fioco."
        ),
        "literal": [
            "While I was tumbling down to a low place,",
            "before my eyes there offered itself to me",
            "one who by long silence seemed faint.",
        ],
    },
    {
        "id": "s22",
        "lines": (64, 66),
        "italian": (
            "Quando vidi costui nel gran diserto,\n"
            "«Miserere di me» gridai a lui,\n"
            "«qual che tu sii, od ombra od omo vero!»"
        ),
        "literal": [
            "When I saw this one in the great desert,",
            "«Have mercy on me» I cried to him,",
            "«whatever you may be, or shade or true man!»",
        ],
    },
    {
        "id": "s23",
        "lines": (67, 69),
        "italian": (
            "Rispuosemi: «Non omo, omo già fui,\n"
            "e li parenti miei furon lombardi,\n"
            "mantoani per patrïa ambedui."
        ),
        "literal": [
            "He answered me: «Not man, man once I was,",
            "and my parents were Lombards,",
            "Mantuans by homeland both.",
        ],
    },
    {
        "id": "s24",
        "lines": (70, 72),
        "italian": (
            "Nacqui sub Iulio, ancor che fosse tardi,\n"
            "e vissi a Roma sotto 'l buono Augusto\n"
            "nel tempo de li dèi falsi e bugiardi."
        ),
        "literal": [
            "I was born under Julius, though it was late,",
            "and I lived in Rome under the good Augustus",
            "in the time of the false and lying gods.",
        ],
    },
]
