"""
╔══════════════════════════════════════════════════════════╗
║   REBIS PROJECT — BOT 1 v2: BENVENUTO COMPLETO          ║
║   Aggiornato con tutto l'ecosistema                      ║
╚══════════════════════════════════════════════════════════╝
"""

import telebot
import os
from rebis_database import *

TOKEN = "8948642005:AAH6fCdMGQLthj4zMJLdK_eTCO5Hp41eKkw"
PDF_PATH = "Rebis_7Pratiche_Risveglio.pdf"
bot = telebot.TeleBot(TOKEN)

BENVENUTO = (
    "🌟 *Benvenuto nel REBIS PROJECT!* 🌟\n"
    "✦ _Spiritual Soul Wisdom_ ✦\n\n"
    "_Creative Genes · Healers · Advanced Magic_\n"
    "_Lovers of Life and Humanity_\n\n"
    "Sei arrivato qui per caso?\n"
    "*Non esistono casualità.* 🙏\n\n"
    "Questo canale è il tuo spazio di evoluzione spirituale superiore "
    "con *Dr. REBIS* — filosofo, Master Teacher, scrittore, "
    "terapeuta energetico con oltre 35 anni di ricerca in 35+ paesi.\n\n"
    "🎁 Scrivi */pdf* per il tuo REGALO di benvenuto gratuito!\n\n"
    "━━━━━━━━━━━━━━━━━━━\n"
    f"📲 WhatsApp: *{CONTATTI['whatsapp']}*\n"
    f"🌐 {CONTATTI['sito']}\n"
    f"▶️ {CONTATTI['youtube']}\n"
    f"📢 {CONTATTI['telegram_canale']}\n"
    "━━━━━━━━━━━━━━━━━━━\n"
    "_Divinely!!! 🙏✨👽_"
)

def keyboard_principale():
    m = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    m.add(
        telebot.types.KeyboardButton("🎁 PDF Gratuito"),
        telebot.types.KeyboardButton("🎓 Corsi & Lezioni"),
        telebot.types.KeyboardButton("📚 Libri Amazon"),
        telebot.types.KeyboardButton("🛠️ Servizi"),
        telebot.types.KeyboardButton("📲 Contatta Dr. REBIS"),
        telebot.types.KeyboardButton("👤 Chi è Dr. REBIS"),
        telebot.types.KeyboardButton("🛒 Gadget & Prodotti"),
        telebot.types.KeyboardButton("▶️ YouTube"),
        telebot.types.KeyboardButton("📢 Canale Telegram"),
        telebot.types.KeyboardButton("🌐 Sito Web"),
    )
    return m

def social_keyboard():
    m = telebot.types.InlineKeyboardMarkup(row_width=2)
    m.add(
        telebot.types.InlineKeyboardButton("💬 WhatsApp", url=CONTATTI["whatsapp_link"]),
        telebot.types.InlineKeyboardButton("🌐 Sito Web", url=CONTATTI["sito"]),
        telebot.types.InlineKeyboardButton("▶️ YouTube", url=CONTATTI["youtube"]),
        telebot.types.InlineKeyboardButton("📸 Instagram", url=CONTATTI["instagram"]),
        telebot.types.InlineKeyboardButton("📘 Facebook", url=CONTATTI["facebook"]),
        telebot.types.InlineKeyboardButton("🎵 TikTok", url=CONTATTI["tiktok"]),
        telebot.types.InlineKeyboardButton("🎮 Discord", url=CONTATTI["discord"]),
        telebot.types.InlineKeyboardButton("🔗 Linktree", url=CONTATTI["linktree"]),
        telebot.types.InlineKeyboardButton("🛒 Amazon Libri", url=CONTATTI["amazon_it"]),
        telebot.types.InlineKeyboardButton("🎁 Gadget Zazzle", url=CONTATTI["zazzle_gadgets"]),
    )
    return m

@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.send_message(message.chat.id, BENVENUTO,
        parse_mode="Markdown", reply_markup=keyboard_principale())

@bot.message_handler(commands=["pdf"])
def cmd_pdf(message):
    bot.send_message(message.chat.id,
        "✨ *Il tuo regalo di benvenuto!*\n\n"
        "📖 _\"7 Pratiche Semplici di Risveglio Spirituale\"_\n"
        "🇮🇹 Italiano · 🇬🇧 English · 🇪🇸 Español\n\n"
        "In arrivo... 🙏", parse_mode="Markdown")
    if os.path.exists(PDF_PATH):
        with open(PDF_PATH, "rb") as f:
            bot.send_document(message.chat.id, f,
                caption=(
                    "🔮 *Rebis Project — 7 Pratiche di Risveglio*\n\n"
                    "Leggi, pratica, evolvi. 🙏\n\n"
                    f"Per approfondire con Dr. REBIS:\n"
                    f"📲 {CONTATTI['whatsapp']}\n"
                    f"🌐 {CONTATTI['sito']}\n\n"
                    "_Divinely!!! ✨_"
                ), parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id,
            f"📩 Contattaci per ricevere il PDF:\n"
            f"📲 WhatsApp: *{CONTATTI['whatsapp']}*\n"
            f"📧 {CONTATTI['email']}",
            parse_mode="Markdown")

@bot.message_handler(func=lambda m: m.text == "🎁 PDF Gratuito")
def t_pdf(msg): cmd_pdf(msg)

@bot.message_handler(func=lambda m: m.text == "🎓 Corsi & Lezioni")
def t_corsi(msg):
    tutti = "\n".join([f"➡️ {c}" for c in list(CORSI.keys())])
    bot.send_message(msg.chat.id,
        f"🎓 *40+ TEMI con Dr. REBIS*\n\n{tutti}\n\n"
        f"Ogni lezione è *privata e personalizzata*.\n\n"
        f"📲 Prenota: {CONTATTI['whatsapp']}\n"
        f"🌐 {CONTATTI['sito']}",
        parse_mode="Markdown", reply_markup=keyboard_principale())

@bot.message_handler(func=lambda m: m.text == "📚 Libri Amazon")
def t_libri(msg):
    elenco = "\n".join([f"📖 {l['titolo_it']}" for l in LIBRI])
    mk = telebot.types.InlineKeyboardMarkup()
    mk.add(telebot.types.InlineKeyboardButton(
        "🛒 Tutti i libri su Amazon IT", url=CONTATTI["amazon_it"]))
    mk.add(telebot.types.InlineKeyboardButton(
        "🛒 Amazon US", url=CONTATTI["amazon_us"]))
    bot.send_message(msg.chat.id,
        f"📚 *LIBRI DI DR. REBIS*\n\n{elenco}\n\n"
        f"🛒 Cerca *DR. REBIS* su Amazon",
        parse_mode="Markdown", reply_markup=mk)

@bot.message_handler(func=lambda m: m.text == "🛠️ Servizi")
def t_servizi(msg):
    elenco = "\n".join([f"✦ {s}" for s in SERVIZI])
    bot.send_message(msg.chat.id,
        f"🛠️ *SERVIZI DI DR. REBIS*\n\n{elenco}\n\n"
        f"📲 {CONTATTI['whatsapp']}\n📧 {CONTATTI['email']}",
        parse_mode="Markdown")

@bot.message_handler(func=lambda m: m.text == "📲 Contatta Dr. REBIS")
def t_contatti(msg):
    bot.send_message(msg.chat.id,
        f"📲 *Contatta Dr. REBIS*\n\n"
        f"Scegli il canale preferito 👇",
        parse_mode="Markdown", reply_markup=social_keyboard())

@bot.message_handler(func=lambda m: m.text == "👤 Chi è Dr. REBIS")
def t_bio(msg):
    bot.send_message(msg.chat.id,
        f"👤 *DR. REBIS*\n\n{BIOGRAFIA['completa']}",
        parse_mode="Markdown")

@bot.message_handler(func=lambda m: m.text == "🛒 Gadget & Prodotti")
def t_gadget(msg):
    mk = telebot.types.InlineKeyboardMarkup()
    mk.add(telebot.types.InlineKeyboardButton(
        "🛒 Gadget Rebis Project", url=CONTATTI["zazzle_gadgets"]))
    bot.send_message(msg.chat.id,
        "🛒 *GADGET & PRODOTTI REBIS PROJECT*\n\nDisponibili su Zazzle 👇",
        parse_mode="Markdown", reply_markup=mk)

@bot.message_handler(func=lambda m: m.text == "▶️ YouTube")
def t_yt(msg):
    mk = telebot.types.InlineKeyboardMarkup()
    mk.add(telebot.types.InlineKeyboardButton("▶️ YouTube Rebis Project", url=CONTATTI["youtube"]))
    mk.add(telebot.types.InlineKeyboardButton(
        "🎥 Conferenza Libreria IBIS", url=CONTATTI["conferenza_youtube"]))
    bot.send_message(msg.chat.id,
        "▶️ *Rebis Project su YouTube*\n\nVideo e insegnamenti di Dr. REBIS 👇",
        parse_mode="Markdown", reply_markup=mk)

@bot.message_handler(func=lambda m: m.text == "📢 Canale Telegram")
def t_tg(msg):
    mk = telebot.types.InlineKeyboardMarkup()
    mk.add(telebot.types.InlineKeyboardButton(
        "📢 Unisciti al Canale", url=CONTATTI["telegram_canale"]))
    bot.send_message(msg.chat.id,
        "📢 *Canale Telegram Ufficiale Rebis Project*\n\n"
        "Post giornalieri, insegnamenti, promozioni e contenuti esclusivi! 👇",
        parse_mode="Markdown", reply_markup=mk)

@bot.message_handler(func=lambda m: m.text == "🌐 Sito Web")
def t_sito(msg):
    mk = telebot.types.InlineKeyboardMarkup()
    mk.add(telebot.types.InlineKeyboardButton(
        "🌐 rebisproject.space", url=CONTATTI["sito"]))
    bot.send_message(msg.chat.id,
        "🌐 *Rebis Project — Sito Ufficiale*\n\nCorsi, servizi, prodotti e molto altro 👇",
        parse_mode="Markdown", reply_markup=mk)

@bot.message_handler(func=lambda m: True)
def fallback(msg):
    import random
    bot.send_message(msg.chat.id,
        f"🔮 _{random.choice(CITAZIONI)}_\n\n"
        f"Usa il menu qui sotto o scrivi */pdf* per il tuo regalo gratuito! 🎁",
        parse_mode="Markdown", reply_markup=keyboard_principale())

print("🌟 Bot 1 v2 — Benvenuto Completo Rebis Project ATTIVO")
bot.infinity_polling()
