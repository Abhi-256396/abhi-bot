
import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client(
    "abhi_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

def main_menu():
    keyboard = [
        [InlineKeyboardButton("🎯 Exampur", callback_data='exampur'), InlineKeyboardButton("📝 Awadh Ojha", callback_data='awadh')],
        [InlineKeyboardButton("🎯 Pinnacle", callback_data='pinnacle'), InlineKeyboardButton("🎓 Quality Edu", callback_data='quality')],
        [InlineKeyboardButton("📘 Abhinay", callback_data='abhinay'), InlineKeyboardButton("🦅 Toppers Wing", callback_data='toppers')],
        [InlineKeyboardButton("⚡ CopyRight", callback_data='copyright'), InlineKeyboardButton("🎯 SELECTION WAY", callback_data='selection')],
        [InlineKeyboardButton("🧠 Study IQ", callback_data='studyiq'), InlineKeyboardButton("⚕️ DAMS DELHI", callback_data='dams')],
        [InlineKeyboardButton("🎓 Khan Sir 2", callback_data='khansir'), InlineKeyboardButton("🚀 FUTURE KUL", callback_data='future')],
        [InlineKeyboardButton("🏞️ My Pathshala", callback_data='mypath'), InlineKeyboardButton("🗺️ Mind Map", callback_data='mindmap')],
        [InlineKeyboardButton("🎓 Eduteria", callback_data='eduteria'), InlineKeyboardButton("📖 Abhyam Academy", callback_data='abhyam')],
        [InlineKeyboardButton("💻 Apna College", callback_data='apnacollege'), InlineKeyboardButton("📡 KD Live (VC)", callback_data='kdlive')],
        [InlineKeyboardButton("🏛️ Chandra Academy", callback_data='chandra'), InlineKeyboardButton("🎯 Tricks Wala", callback_data='tricks')],
        [InlineKeyboardButton("⭕ Jeet G", callback_data='jeet'), InlineKeyboardButton("🅷 H Help", callback_data='hhelp')],
        [InlineKeyboardButton("©️ Ceramic Academy", callback_data='ceramic'), InlineKeyboardButton("🌱 Spring Board", callback_data='spring')],
        [InlineKeyboardButton("🅰️ Avni Education", callback_data='avni'), InlineKeyboardButton("📚 Other Coaching", callback_data='other')],
        [InlineKeyboardButton("⬅️ Back", callback_data='back'), InlineKeyboardButton("🏠 Home", callback_data='home')],
        [InlineKeyboardButton("🛟 Contact Support", callback_data='support')]
    ]
    return InlineKeyboardMarkup(keyboard)

@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply_text(
        "**Abhi Bot Live Hai**\n\n💬 Need access? Contact Admin",
        reply_markup=main_menu()
    )

@app.on_message(filters.command("help"))
async def help_(_, message):
    await message.reply_text(
        "**Commands:**\n/start - Bot start\n/help - Ye message",
        reply_markup=main_menu()
    )

@app.on_callback_query()
async def callback_handler(_, query):
    data = query.data
    if data == "home" or data == "back":
        await query.message.edit_text(
            "**Abhi Bot Live Hai**\n\n💬 Need access? Contact Admin",
            reply_markup=main_menu()
        )
    elif data == "support":
        await query.answer("Support: @YourUsername", show_alert=True)
    else:
        await query.answer(f"You selected: {data}", show_alert=False)
        await query.message.reply_text(f"✅ **{data.upper()}** selected!\n\nYaha iska content aayega.")

print("Bot Started...")
app.run()
