"""
╔══════════════════════════════════════════════════════════╗
║   REBIS PROJECT — BOT 3: CRESCITA & REFERRAL            ║
║   Funzione: incentiva inviti, traccia crescita canale    ║
╚══════════════════════════════════════════════════════════╝

INSTALLAZIONE:
  pip install pyTelegramBotAPI

AVVIO:
  python3 bot3_crescita.py

COME FUNZIONA:
  - Ogni utente riceve un link referral unico
  - Chi porta 3 amici riceve un contenuto esclusivo
  - Chi porta 10 amici viene contattato da Dr. REBIS
  - Traccia statistiche di crescita del canale
"""

import telebot
import json
import os
from datetime import datetime

TOKEN = "8948642005:AAH6fCdMGQLthj4zMJLdK_eTCO5Hp41eKkw"
CANALE = "https://t.me/rebisprojectTGNews"
DB_FILE = "rebis_referral_db.json"

bot = telebot.TeleBot(TOKEN)

# ─── Database JSON semplice ───────────────────────────────────────────────────
def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    return {"users": {}, "total_referrals": 0, "joined_today": 0}

def save_db(db):
    with open(DB_FILE, 'w') as f:
        json.dump(db, f, indent=2)

def get_user(db, user_id):
    uid = str(user_id)
    if uid not in db["users"]:
        db["users"][uid] = {
            "referrals": 0,
            "joined": datetime.now().isoformat(),
            "rewards_claimed": [],
            "username": ""
        }
    return db["users"][uid]

# ─── Premi per livello ────────────────────────────────────────────────────────
REWARDS = {
    3: {
        "emoji": "🎁",
        "title": "CONTENUTO ESCLUSIVO",
        "text": (
            "🎁 *PREMIO — 3 amici invitati!*\n\n"
            "Grazie per diffondere la luce di Rebis Project! 🌟\n\n"
            "Ecco il tuo contenuto esclusivo:\n\n"
            "🔥 *MEDITAZIONE AVANZATA DI DR. REBIS*\n\n"
            "_La Tecnica del Testimone Silenzioso:_\n\n"
            "1. Siediti in posizione comoda. Schiena dritta.\n"
            "2. Chiudi gli occhi. Respira profondamente 3 volte.\n"
            "3. Immagina di essere seduto in una stanza vuota, "
            "al centro. Ogni pensiero che emerge è un ospite "
            "che entra dalla porta. Tu lo osservi. Non lo giudichi. "
            "Non lo segui. Lo lasci uscire dall'altra porta.\n"
            "4. Pratica per 15 minuti ogni giorno per 21 giorni.\n\n"
            "_Dopo 21 giorni, qualcosa in te cambierà per sempre._\n\n"
            "Per approfondire con Dr. REBIS:\n"
            "📲 wa.me/393515355835\n\n"
            "Continua a invitare per sbloccare il premio successivo! 👇"
        )
    },
    10: {
        "emoji": "⭐",
        "title": "SESSIONE GRATUITA",
        "text": (
            "⭐ *STRAORDINARIO — 10 amici invitati!*\n\n"
            "Sei un vero Guerriero della Luce! 🌟\n\n"
            "Il tuo premio:\n"
            "*Una sessione gratuita di 30 minuti con Dr. REBIS!*\n\n"
            "Contatta Dr. REBIS menzonando questo messaggio:\n"
            "📲 WhatsApp: *+39 351 535 5835*\n"
            "📧 rebis.project69@gmail.com\n\n"
            "_La tua dedizione alla crescita spirituale della community "
            "merita un riconoscimento speciale._ 🙏\n\n"
            "Divinely!!! ✨👽"
        )
    },
    25: {
        "emoji": "👑",
        "title": "AMBASCIATORE REBIS",
        "text": (
            "👑 *LEGGENDARIO — 25 amici invitati!*\n\n"
            "Sei un *Ambasciatore Ufficiale di Rebis Project*! 🌟\n\n"
            "Il tuo premio:\n"
            "• 🎓 Accesso prioritario a tutti i nuovi corsi\n"
            "• 📚 Un libro di Dr. REBIS in omaggio\n"
            "• 🌟 Menzione speciale sul canale\n"
            "• 💬 Canale diretto con Dr. REBIS\n\n"
            "Contattaci SUBITO:\n"
            "📲 WhatsApp: *+39 351 535 5835*\n\n"
            "_Sei parte integrante della crescita spirituale di questa community._\n\n"
            "Divinely!!! ✨👑"
        )
    }
}

# ─── /start con referral tracking ────────────────────────────────────────────
@bot.message_handler(commands=['start'])
def cmd_start(message):
    db = load_db()
    user = get_user(db, message.from_user.id)
    user["username"] = message.from_user.username or message.from_user.first_name or "Anonimo"

    # Controlla se arrivato tramite referral
    args = message.text.split()
    if len(args) > 1:
        referrer_id = args[1]
        if referrer_id != str(message.from_user.id) and referrer_id in db["users"]:
            referrer = db["users"][referrer_id]
            referrer["referrals"] += 1
            db["total_referrals"] += 1

            # Notifica chi ha invitato
            count = referrer["referrals"]
            bot.send_message(
                int(referrer_id),
                f"🎉 Qualcuno si è unito tramite il tuo link!\n"
                f"Hai invitato *{count}* {' persona' if count == 1 else ' persone'}.\n\n"
                f"{'🎁 Scrivi /premio per ritirare il tuo regalo!' if count in REWARDS else f'👉 Ancora {min([k for k in REWARDS.keys() if k > count], default=25) - count} inviti per il prossimo premio!'}",
                parse_mode='Markdown'
            )

            # Controlla premi
            for soglia in sorted(REWARDS.keys()):
                if count >= soglia and soglia not in referrer.get("rewards_claimed", []):
                    referrer.setdefault("rewards_claimed", []).append(soglia)
                    bot.send_message(
                        int(referrer_id),
                        REWARDS[soglia]["text"],
                        parse_mode='Markdown'
                    )
                    break

    save_db(db)

    # Messaggio benvenuto con link personale
    user_id = message.from_user.id
    link_personale = f"https://t.me/RebisProjectBot?start={user_id}"

    bot.send_message(
        message.chat.id,
        f"🌟 *Benvenuto nel programma crescita Rebis Project!* 🌟\n\n"
        f"Aiutaci a portare la luce spirituale a più persone!\n\n"
        f"🔗 *Il tuo link personale:*\n`{link_personale}`\n\n"
        f"Ogni volta che qualcuno si unisce tramite il tuo link, accumuli punti per premi esclusivi!\n\n"
        f"🎁 *Premi disponibili:*\n"
        f"• 3 inviti → Meditazione esclusiva di Dr. REBIS\n"
        f"• 10 inviti → Sessione GRATUITA 30min con Dr. REBIS\n"
        f"• 25 inviti → Ambasciatore Rebis Project 👑\n\n"
        f"📊 Scrivi /statistiche per vedere i tuoi progressi\n"
        f"🏆 Scrivi /classifica per vedere i top invitatori\n\n"
        f"Condividi il link ovunque:\nInstagram · Facebook · WhatsApp · TikTok\n\n"
        f"Ogni anima che porti qui è un atto d'Amore. 🙏",
        parse_mode='Markdown'
    )

# ─── /statistiche ────────────────────────────────────────────────────────────
@bot.message_handler(commands=['statistiche', 'stats'])
def cmd_stats(message):
    db = load_db()
    user = get_user(db, message.from_user.id)
    count = user["referrals"]

    prossimo = next((k for k in sorted(REWARDS.keys()) if k > count), None)
    mancano = (prossimo - count) if prossimo else 0

    testo = (
        f"📊 *Le tue statistiche*\n\n"
        f"👥 Amici invitati: *{count}*\n"
        f"🏆 Premi ricevuti: *{len(user.get('rewards_claimed', []))}*\n\n"
    )

    if prossimo:
        testo += f"🎯 Prossimo premio: *{REWARDS[prossimo]['emoji']} {REWARDS[prossimo]['title']}*\n"
        testo += f"📍 Mancano: *{mancano} inviti*\n\n"
    else:
        testo += "👑 Hai raggiunto il massimo livello! Sei un Ambasciatore!\n\n"

    user_id = message.from_user.id
    link = f"https://t.me/RebisProjectBot?start={user_id}"
    testo += f"🔗 Il tuo link:\n`{link}`"

    bot.send_message(message.chat.id, testo, parse_mode='Markdown')

# ─── /classifica ─────────────────────────────────────────────────────────────
@bot.message_handler(commands=['classifica', 'top'])
def cmd_classifica(message):
    db = load_db()
    users = db["users"]

    # Ordina per referrals
    top = sorted(users.items(), key=lambda x: x[1].get("referrals", 0), reverse=True)[:10]

    testo = "🏆 *TOP INVITATORI REBIS PROJECT*\n\n"
    medaglie = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

    for i, (uid, data) in enumerate(top):
        nome = data.get("username", "Anonimo")
        count = data.get("referrals", 0)
        if count > 0:
            testo += f"{medaglie[i]} *{nome}* — {count} inviti\n"

    testo += f"\n👥 Totale iscritti portati dalla community: *{db.get('total_referrals', 0)}*\n\n"
    testo += "Vuoi salire in classifica? Condividi il tuo link!\n/statistiche per il tuo link personale"

    bot.send_message(message.chat.id, testo, parse_mode='Markdown')

# ─── /premio ─────────────────────────────────────────────────────────────────
@bot.message_handler(commands=['premio'])
def cmd_premio(message):
    db = load_db()
    user = get_user(db, message.from_user.id)
    count = user["referrals"]
    claimed = user.get("rewards_claimed", [])

    premio_disponibile = None
    for soglia in sorted(REWARDS.keys()):
        if count >= soglia and soglia not in claimed:
            premio_disponibile = soglia
            break

    if premio_disponibile:
        user.setdefault("rewards_claimed", []).append(premio_disponibile)
        save_db(db)
        bot.send_message(message.chat.id,
                        REWARDS[premio_disponibile]["text"],
                        parse_mode='Markdown')
    else:
        prossimo = next((k for k in sorted(REWARDS.keys()) if k > count), None)
        if prossimo:
            bot.send_message(message.chat.id,
                f"🎯 Non hai ancora raggiunto il prossimo premio.\n\n"
                f"Mancano *{prossimo - count} inviti* per:\n"
                f"{REWARDS[prossimo]['emoji']} *{REWARDS[prossimo]['title']}*\n\n"
                f"Usa /statistiche per il tuo link personale!",
                parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id,
                "👑 Hai già riscattato tutti i premi disponibili!\n"
                "Sei un vero Ambasciatore di Rebis Project! Grazie! 🙏",
                parse_mode='Markdown')

# ─── /canale — link al canale ─────────────────────────────────────────────────
@bot.message_handler(commands=['canale'])
def cmd_canale(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(
        "📢 Unisciti al Canale Rebis Project", url=CANALE))
    bot.send_message(message.chat.id,
        "📢 *Rebis Project — Canale Telegram Ufficiale*\n\n"
        "Unisciti alla nostra community spirituale!",
        parse_mode='Markdown', reply_markup=markup)

# ─── Fallback ─────────────────────────────────────────────────────────────────
@bot.message_handler(func=lambda m: True)
def fallback(message):
    bot.send_message(
        message.chat.id,
        "🌟 Usa questi comandi:\n\n"
        "/start — Ottieni il tuo link personale\n"
        "/statistiche — I tuoi progressi\n"
        "/classifica — Top invitatori\n"
        "/premio — Ritira il tuo premio\n"
        "/canale — Link al canale ufficiale\n\n"
        "📲 Per info: wa.me/393515355835"
    )

# ─── Avvio ────────────────────────────────────────────────────────────────────
print("🚀 Bot 3 — Crescita & Referral Rebis Project ATTIVO")
bot.infinity_polling()
