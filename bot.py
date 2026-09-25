import os
from pyrogram import Client, filters

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client(
    "abhi_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply_text(
        "✅ **Abhi Bot Live Hai!**\n\n"
        "/help - help dekhne ke liye"
    )

@app.on_message(filters.command("help"))
async def help(_, message):
    await message.reply_text(
        "📚 **Commands:**\n"
        "/start - Bot start\n"
        "/help - Ye message"
    )

print("Bot Started...")
app.run()
