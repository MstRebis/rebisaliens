"""
╔══════════════════════════════════════════════════════════╗
║   REBIS PROJECT — BOT 2 v2: ASSISTENTE FAQ COMPLETO     ║
║   Aggiornato con database ecosistema completo            ║
╚══════════════════════════════════════════════════════════╝
"""

import telebot
from rebis_database import *

TOKEN = "8948642005:AAH6fCdMGQLthj4zMJLdK_eTCO5Hp41eKkw"
bot = telebot.TeleBot(TOKEN)

# ─── Keyboards ───────────────────────────────────────────
def menu_principale():
    m = telebot.types.InlineKeyboardMarkup(row_width=2)
    m.add(
        telebot.types.InlineKeyboardButton("👤 Chi è Dr. REBIS", callback_data="bio"),
        telebot.types.InlineKeyboardButton("🎓 Tutti i Corsi", callback_data="corsi"),
        telebot.types.InlineKeyboardButton("📚 Libri su Amazon", callback_data="libri"),
        telebot.types.InlineKeyboardButton("🛠️ Servizi", callback_data="servizi"),
        telebot.types.InlineKeyboardButton("🏛️ Centri Fisici", callback_data="centri"),
        telebot.types.InlineKeyboardButton("🎁 PDF Gratuito", callback_data="pdf"),
        telebot.types.InlineKeyboardButton("📲 Contatti", callback_data="contatti"),
        telebot.types.InlineKeyboardButton("🛒 Gadget & Prodotti", callback_data="gadget"),
    )
    return m

def menu_corsi():
    m = telebot.types.InlineKeyboardMarkup(row_width=2)
    categorie = [
        ("🔥 Alchimia Gnostica", "corso_alchimia"),
        ("⚡ Superpoteri", "corso_superpoteri"),
        ("🧘 Yoga", "corso_yoga"),
        ("🌙 Viaggio Astrale", "corso_astrale"),
        ("🔮 Tarot & Rune", "corso_tarot"),
        ("💫 Twin Flame", "corso_twin"),
        ("🌟 Merkabah", "corso_merkabah"),
        ("🌳 Kabbalah", "corso_kabbalah"),
        ("💰 Economia Spirituale", "corso_economia"),
        ("👽 Realtà Extraterrestri", "corso_et"),
        ("🏠 Costellazioni Familiari", "corso_costellazioni"),
        ("📿 Reiki", "corso_reiki"),
        ("🌀 Tutti i 40+ temi", "corso_tutti"),
    ]
    for label, cb in categorie:
        m.add(telebot.types.InlineKeyboardButton(label, callback_data=cb))
    m.add(telebot.types.InlineKeyboardButton("🔙 Menu principale", callback_data="menu"))
    return m

def menu_libri():
    m = telebot.types.InlineKeyboardMarkup(row_width=1)
    for i, libro in enumerate(LIBRI[:8]):  # Primi 8
        m.add(telebot.types.InlineKeyboardButton(
            f"📖 {libro['titolo_it'][:45]}...", callback_data=f"libro_{i}"))
    m.add(telebot.types.InlineKeyboardButton("📚 Tutti i libri su Amazon", url=CONTATTI["amazon_it"]))
    m.add(telebot.types.InlineKeyboardButton("🔙 Menu principale", callback_data="menu"))
    return m

def back_menu():
    m = telebot.types.InlineKeyboardMarkup()
    m.add(
        telebot.types.InlineKeyboardButton("🔙 Menu", callback_data="menu"),
        telebot.types.InlineKeyboardButton("📲 Prenota", url=CONTATTI["whatsapp_link"]),
    )
    return m

# ─── /start ──────────────────────────────────────────────
@bot.message_handler(commands=["start", "help", "menu"])
def cmd_start(message):
    bot.send_message(
        message.chat.id,
        "🔮 *Rebis Project — Assistente Spirituale* 🔮\n\n"
        "_Creative Genes · Healers · Advanced Magic_\n\n"
        "Benvenuto! Sono qui per guidarti nell'ecosistema di *Dr. REBIS*.\n\n"
        "Cosa vuoi esplorare? 👇",
        parse_mode="Markdown",
        reply_markup=menu_principale()
    )

# ─── Callback handler ────────────────────────────────────
@bot.callback_query_handler(func=lambda c: True)
def cb(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    d = call.data
    bot.answer_callback_query(call.id)

    # ── Menu principale ──
    if d == "menu":
        bot.edit_message_text(
            "🔮 *Menu Principale — Rebis Project*\nCosa vuoi esplorare? 👇",
            cid, mid, parse_mode="Markdown", reply_markup=menu_principale())

    # ── Biografia ──
    elif d == "bio":
        testo = (
            f"👤 *DR. REBIS — Master Teacher Spirituale*\n\n"
            f"{BIOGRAFIA['completa']}\n\n"
            f"━━━━━━━━━━━━━━━━━━━\n"
            f"🌐 {CONTATTI['sito']}\n"
            f"📲 WhatsApp: {CONTATTI['whatsapp']}\n"
            f"▶️ {CONTATTI['youtube']}\n"
            f"📸 {CONTATTI['instagram']}\n"
        )
        bot.edit_message_text(testo, cid, mid, parse_mode="Markdown", reply_markup=back_menu())

    # ── Corsi (menu) ──
    elif d == "corsi":
        bot.edit_message_text(
            "🎓 *Corsi e Insegnamenti di Dr. REBIS*\n\nScegli un tema 👇",
            cid, mid, parse_mode="Markdown", reply_markup=menu_corsi())

    # ── Singoli corsi ──
    elif d == "corso_alchimia":
        temi = "\n".join([f"• {t}" for t in CORSI["Alchimia Gnostica"]])
        bot.edit_message_text(
            f"🔥 *ALCHIMIA GNOSTICA*\n\n"
            f"Temi trattati:\n{temi}\n\n"
            f"L'Alchimia Gnostica non riguarda metalli fisici — riguarda la trasformazione "
            f"della tua Coscienza. Dal Nigredo (dissoluzione) al Rubedo (rinascita), "
            f"Dr. REBIS ti guida attraverso la Grande Opera interiore.\n\n"
            f"📲 Prenota: {CONTATTI['whatsapp']}",
            cid, mid, parse_mode="Markdown", reply_markup=back_menu())

    elif d == "corso_superpoteri":
        temi = "\n".join([f"• {t}" for t in CORSI["Superpoteri"]])
        bot.edit_message_text(
            f"⚡ *SUPERPOTERI*\n\n{temi}\n\n"
            f"Telepatia, Chiaroveggenza, Guarigione — non sono miti, "
            f"sono facoltà dormienti della tua Coscienza pronte ad essere risvegliate.\n\n"
            f"📲 Prenota: {CONTATTI['whatsapp']}",
            cid, mid, parse_mode="Markdown", reply_markup=back_menu())

    elif d == "corso_yoga":
        temi = "\n".join([f"• {t}" for t in CORSI["Yoga — Immortalità & Libertà"]])
        bot.edit_message_text(
            f"🧘 *YOGA — IMMORTALITÀ & LIBERTÀ*\n\n{temi}\n\n"
            f"Yoga non come ginnastica ma come tecnologia di Liberazione. "
            f"Dr. REBIS è Maestro Tradizionale di Yoga con approccio kundalini e spirituale profondo.\n\n"
            f"📲 Prenota: {CONTATTI['whatsapp']}",
            cid, mid, parse_mode="Markdown", reply_markup=back_menu())

    elif d == "corso_astrale":
        bot.edit_message_text(
            f"🌙 *VIAGGIO ASTRALE & SOGNO LUCIDO*\n\n"
            f"Impara a uscire consciamente dal corpo fisico ed esplorare i piani sottili.\n"
            f"Dr. REBIS insegna tecniche sicure e provate di proiezione astrale, "
            f"sogno lucido e navigazione dei mondi invisibili.\n\n"
            f"📲 Prenota: {CONTATTI['whatsapp']}",
            cid, mid, parse_mode="Markdown", reply_markup=back_menu())

    elif d == "corso_tarot":
        bot.edit_message_text(
            f"🔮 *TAROT · RUNE · FUTHARK*\n\n"
            f"Il Tarot come specchio dell'anima e strumento di autoconoscenza.\n"
            f"Le Rune del Futhark come sistema sacro nordico applicato alla vita spirituale.\n"
            f"Mitologia Norrena come mappa cosmica dell'esistenza.\n\n"
            f"📲 Prenota: {CONTATTI['whatsapp']}",
            cid, mid, parse_mode="Markdown", reply_markup=back_menu())

    elif d == "corso_twin":
        bot.edit_message_text(
            f"💫 *TWIN FLAME / ANIMA GEMELLA*\n\n"
            f"Il tema più intenso e trasformativo del percorso spirituale.\n"
            f"Dr. REBIS accompagna chi vive questa esperienza con comprensione profonda, "
            f"strumenti concreti e visione multidimensionale del legame tra anime.\n\n"
            f"Include anche: La Coppia Sacra e la Sessualità Sacra.\n\n"
            f"📲 Prenota: {CONTATTI['whatsapp']}",
            cid, mid, parse_mode="Markdown", reply_markup=back_menu())

    elif d == "corso_merkabah":
        bot.edit_message_text(
            f"🌟 *MERKABAH*\n\n"
            f"Il Merkabah è il veicolo di luce della Coscienza — "
            f"un campo energetico rotante che attiva il corpo di luce "
            f"e permette la navigazione multidimensionale.\n\n"
            f"Una delle pratiche più avanzate insegnate da Dr. REBIS.\n\n"
            f"📲 Prenota: {CONTATTI['whatsapp']}",
            cid, mid, parse_mode="Markdown", reply_markup=back_menu())

    elif d == "corso_kabbalah":
        bot.edit_message_text(
            f"🌳 *KABBALAH & ALBERO DELLA VITA*\n\n"
            f"Il sistema mistico ebraico come mappa dell'universo e dell'anima.\n"
            f"I 10 Sephirot, i 22 sentieri, i 4 Mondi, l'Akasha.\n"
            f"La Kabbalah come chiave per comprendere la struttura della realtà.\n\n"
            f"📲 Prenota: {CONTATTI['whatsapp']}",
            cid, mid, parse_mode="Markdown", reply_markup=back_menu())

    elif d == "corso_economia":
        bot.edit_message_text(
            f"💰 *DENARO, FINANZA & ECONOMIA SPIRITUALE*\n\n"
            f"Il denaro è energia. Come ogni energia, può essere allineata con la tua evoluzione.\n\n"
            f"Dr. REBIS insegna come integrare prosperità materiale e cammino spirituale, "
            f"come sciogliere blocchi karmici finanziari e come applicare "
            f"la vera Legge dell'Attrazione.\n\n"
            f"📲 Prenota: {CONTATTI['whatsapp']}",
            cid, mid, parse_mode="Markdown", reply_markup=back_menu())

    elif d == "corso_et":
        bot.edit_message_text(
            f"👽 *REALTÀ EXTRATERRESTRI*\n\n"
            f"\"Alieno è sinonimo di altro. Quando nell'altro ritrovi te stesso, "
            f"quello è un atto d'Amore.\" — Dr. REBIS\n\n"
            f"Esplorazione delle realtà multidimensionali, delle intelligenze cosmiche "
            f"e della coscienza extraterrestre come specchio evolutivo dell'umanità.\n\n"
            f"📲 Prenota: {CONTATTI['whatsapp']}",
            cid, mid, parse_mode="Markdown", reply_markup=back_menu())

    elif d == "corso_costellazioni":
        bot.edit_message_text(
            f"🏠 *COSTELLAZIONI FAMILIARI*\n\n"
            f"Le dinamiche familiari trasmesse attraverso le generazioni "
            f"influenzano profondamente la nostra vita.\n"
            f"Le Costellazioni Familiari rivelano e liberano questi pattern nascosti "
            f"per una guarigione profonda e duratura.\n\n"
            f"📲 Prenota: {CONTATTI['whatsapp']}",
            cid, mid, parse_mode="Markdown", reply_markup=back_menu())

    elif d == "corso_reiki":
        bot.edit_message_text(
            f"📿 *REIKI USUI & KARUNA*\n\n"
            f"Dr. REBIS è *Maestro Tradizionale di Reiki Usui e Karuna*.\n\n"
            f"Offre iniziazioni, attunement e insegnamenti completi del sistema Reiki "
            f"per la guarigione energetica di sé e degli altri.\n\n"
            f"📲 Prenota: {CONTATTI['whatsapp']}",
            cid, mid, parse_mode="Markdown", reply_markup=back_menu())

    elif d == "corso_tutti":
        tutti = "\n".join([f"➡️ {c}" for c in list(CORSI.keys())])
        bot.edit_message_text(
            f"🎓 *TUTTI I TEMI DI INSEGNAMENTO*\n\n{tutti}\n\n"
            f"Ogni lezione è *privata e personalizzata*.\n"
            f"📲 Prenota: {CONTATTI['whatsapp']}\n"
            f"🌐 {CONTATTI['sito']}",
            cid, mid, parse_mode="Markdown", reply_markup=back_menu())

    # ── Libri ──
    elif d == "libri":
        testo = "📚 *LIBRI DI DR. REBIS*\n\nScegli un libro per i dettagli 👇"
        bot.edit_message_text(testo, cid, mid, parse_mode="Markdown", reply_markup=menu_libri())

    elif d.startswith("libro_"):
        idx = int(d.split("_")[1])
        l = LIBRI[idx]
        testo = (
            f"📖 *{l['titolo_it']}*\n\n"
            f"🇪🇸 _{l['titolo_es']}_\n\n"
            f"📝 {l['descrizione']}\n\n"
            f"{'📚 Serie: ' + l['serie'] + chr(10) if l['serie'] != '—' else ''}"
            f"{'📅 Anno: ' + l['anno'] + chr(10) if l['anno'] != '—' else ''}"
            f"💰 {l['prezzo']}\n\n"
            f"🛒 Cerca *DR. REBIS* su Amazon"
        )
        mk = telebot.types.InlineKeyboardMarkup()
        mk.add(telebot.types.InlineKeyboardButton("🛒 Vai ad Amazon", url=l["link"]))
        mk.add(
            telebot.types.InlineKeyboardButton("🔙 Libri", callback_data="libri"),
            telebot.types.InlineKeyboardButton("🏠 Menu", callback_data="menu"),
        )
        bot.edit_message_text(testo, cid, mid, parse_mode="Markdown", reply_markup=mk)

    # ── Servizi ──
    elif d == "servizi":
        elenco = "\n".join([f"✦ {s}" for s in SERVIZI])
        bot.edit_message_text(
            f"🛠️ *SERVIZI DI DR. REBIS*\n\n{elenco}\n\n"
            f"Tutti i servizi sono *personalizzati* e adattati al tuo livello evolutivo.\n\n"
            f"📲 Prenota su WhatsApp: {CONTATTI['whatsapp']}\n"
            f"📧 {CONTATTI['email']}\n"
            f"🌐 {CONTATTI['sito']}",
            cid, mid, parse_mode="Markdown", reply_markup=back_menu())

    # ── Centri fisici ──
    elif d == "centri":
        proj = "\n".join([f"• {p}" for p in BIOGRAFIA["progetti_fisici"]])
        bot.edit_message_text(
            f"🏛️ *REBIS SPIRITUAL AWAKENING CENTER*\n\n"
            f"{proj}\n\n"
            f"🗺️ Trova il centro più vicino:\n{CENTRI['google_maps']}\n\n"
            f"Per info e prenotazioni:\n"
            f"📲 {CONTATTI['whatsapp']}\n"
            f"📧 {CONTATTI['email']}",
            cid, mid, parse_mode="Markdown", reply_markup=back_menu())

    # ── PDF ──
    elif d == "pdf":
        bot.edit_message_text(
            f"🎁 *PDF GRATUITO*\n\n"
            f"Scrivi /pdf oppure contattaci per ricevere:\n\n"
            f"_\"7 Pratiche Semplici di Risveglio Spirituale\"_\n"
            f"🇮🇹 Italiano · 🇬🇧 English · 🇪🇸 Español\n\n"
            f"📲 {CONTATTI['whatsapp']}\n"
            f"📧 {CONTATTI['email']}",
            cid, mid, parse_mode="Markdown", reply_markup=back_menu())

    # ── Contatti ──
    elif d == "contatti":
        mk = telebot.types.InlineKeyboardMarkup(row_width=2)
        mk.add(
            telebot.types.InlineKeyboardButton("💬 WhatsApp", url=CONTATTI["whatsapp_link"]),
            telebot.types.InlineKeyboardButton("📧 Email", url=f"mailto:{CONTATTI['email']}"),
            telebot.types.InlineKeyboardButton("🌐 Sito Web", url=CONTATTI["sito"]),
            telebot.types.InlineKeyboardButton("▶️ YouTube", url=CONTATTI["youtube"]),
            telebot.types.InlineKeyboardButton("📸 Instagram", url=CONTATTI["instagram"]),
            telebot.types.InlineKeyboardButton("📘 Facebook", url=CONTATTI["facebook"]),
            telebot.types.InlineKeyboardButton("🎵 TikTok", url=CONTATTI["tiktok"]),
            telebot.types.InlineKeyboardButton("🎮 Discord", url=CONTATTI["discord"]),
            telebot.types.InlineKeyboardButton("🔗 Linktree", url=CONTATTI["linktree"]),
            telebot.types.InlineKeyboardButton("🗺️ Centri (Maps)", url=CENTRI["google_maps"]),
        )
        mk.add(telebot.types.InlineKeyboardButton("🔙 Menu", callback_data="menu"))
        bot.edit_message_text(
            f"📲 *TUTTI I CONTATTI DI REBIS PROJECT*\n\n"
            f"📲 WhatsApp: *{CONTATTI['whatsapp']}*\n"
            f"📧 {CONTATTI['email']}\n"
            f"🌐 {CONTATTI['sito']}\n\n"
            f"Scegli il canale che preferisci 👇",
            cid, mid, parse_mode="Markdown", reply_markup=mk)

    # ── Gadget ──
    elif d == "gadget":
        mk = telebot.types.InlineKeyboardMarkup()
        mk.add(telebot.types.InlineKeyboardButton(
            "🛒 Gadget & Prodotti Rebis Project", url=CONTATTI["zazzle_gadgets"]))
        mk.add(telebot.types.InlineKeyboardButton("🔙 Menu", callback_data="menu"))
        bot.edit_message_text(
            f"🛒 *GADGET & PRODOTTI REBIS PROJECT*\n\n"
            f"T-shirt, oggetti spirituali, articoli esclusivi Rebis Project.\n\n"
            f"Disponibili su Zazzle 👇",
            cid, mid, parse_mode="Markdown", reply_markup=mk)

# ─── Messaggi liberi con keyword matching ────────────────
KEYWORDS = {
    ("alchimia", "solve", "nigredo", "rubedo", "ombra", "drago", "pietra filosofale"):
        "corso_alchimia",
    ("superpoteri", "telepatia", "chiaroveggenza", "guarigione", "manifestazione",
     "intuizione", "magnetismo", "volontà", "premonizione"):
        "corso_superpoteri",
    ("yoga", "kundalini", "pranayama", "samadhi", "asana"):
        "corso_yoga",
    ("astrale", "viaggio astrale", "sogno lucido", "corpo astrale", "proiezione"):
        "corso_astrale",
    ("tarot", "tarocchi", "rune", "futhark", "nordica", "norrena"):
        "corso_tarot",
    ("twin flame", "anima gemella", "fiamma gemella", "sessualità sacra"):
        "corso_twin",
    ("merkabah", "merkaba", "corpo di luce"):
        "corso_merkabah",
    ("kabbalah", "albero della vita", "sephirot", "akasha"):
        "corso_kabbalah",
    ("denaro", "soldi", "finanza", "prosperità", "abbondanza", "economia"):
        "corso_economia",
    ("alieno", "extraterrestre", "ufo", "et", "multiverso", "dimensioni"):
        "corso_et",
    ("costellazioni", "famiglia", "generazioni"):
        "corso_costellazioni",
    ("reiki", "usui", "karuna"):
        "corso_reiki",
    ("libro", "libri", "amazon", "pubblicazione", "scritto"):
        "libri",
    ("prenota", "prenotare", "sessione", "lezione", "costo", "prezzo", "quanto costa"):
        "servizi",
    ("centro", "sede", "dove", "indirizzo", "maps"):
        "centri",
    ("chi è", "chi sei", "dr rebis", "rebis", "biografia", "master"):
        "bio",
    ("gadget", "prodotti", "negozio", "shop", "acquisto"):
        "gadget",
    ("contatti", "contatto", "scrivere", "email", "whatsapp", "telefono"):
        "contatti",
}

@bot.message_handler(commands=["pdf"])
def cmd_pdf(message):
    bot.send_message(message.chat.id,
        "🎁 Per ricevere il PDF gratuito:\n\n"
        "_\"7 Pratiche Semplici di Risveglio Spirituale\"_\n\n"
        f"📲 WhatsApp: *{CONTATTI['whatsapp']}*\n"
        f"📧 {CONTATTI['email']}\n\n"
        "Dicci solo 'PDF' e te lo mandiamo! 🙏",
        parse_mode="Markdown")

@bot.message_handler(func=lambda m: True)
def messaggio_libero(message):
    testo = message.text.lower()
    callback_trovato = None
    for keywords, callback in KEYWORDS.items():
        if any(k in testo for k in keywords):
            callback_trovato = callback
            break

    if callback_trovato:
        # Simula click sul callback
        fake_call = type('obj', (object,), {
            'message': type('obj', (object,), {
                'chat': type('obj', (object,), {'id': message.chat.id})(),
                'message_id': None
            })(),
            'id': None,
            'data': callback_trovato
        })()
        # Manda nuovo messaggio invece di edit
        bot.send_message(
            message.chat.id,
            f"🔍 Ho trovato info su questo argomento!\nUsa il menu qui sotto 👇",
            reply_markup=menu_principale()
        )
    else:
        import random
        citazione = random.choice(CITAZIONI)
        bot.send_message(
            message.chat.id,
            f"🔮 Non ho una risposta specifica, ma Dr. REBIS sì!\n\n"
            f"_{citazione}_\n\n"
            f"📲 Contatta Dr. REBIS direttamente:\n"
            f"WhatsApp: *{CONTATTI['whatsapp']}*\n\n"
            f"Oppure esplora il menu 👇",
            parse_mode="Markdown",
            reply_markup=menu_principale()
        )

print("🔮 Bot 2 v2 — FAQ Completo Rebis Project ATTIVO")
bot.infinity_polling()
