from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import random
from config import *
REACTIONS = [
    "❤️", "🔥",  "👍", "👏", "🎉", "💯",
  "😍", "🤔", "😢", "💩", "🤯",  "😡", "🥰"
]

KEYWORD_REACTIONS = {
    "love": "❤️",
    "cool": "🔥",
    "omg": "😲",
    "happy": "🥰",
    "sad": "😢",
    "wow": "👏",
    "yes": "👍",
    "no": "👎",
    "angry": "😡",
    "dead": "💯"
}

ABUSIVE_KEYWORDS = {
    "fuck", "shit", "bitch", "asshole", "bastard",
    "dumb", "stupid", "idiot", "retard", "fag", "slut", "whore", "nigga", "nigger"
}
ABUSIVE_REACTIONS = ["🤬", "😡", "💩"]



bot = Client("rxn_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@bot.on_message(filters.command("start"))
async def start_handler(_, message: Message):
    await message.reply_text(
        "👋 Hello! I'm your Reaction Bot!\nI react to every message in this chat!",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📢 Channel", url="https://t.me/shishyacode")],
            [InlineKeyboardButton("👤 Developer", url="https://t.me/shishyapy")]
        ])
    )


@bot.on_message(filters.command("help"))
async def help_handler(_, message: Message):
    await message.reply_text(
        "ℹ️ I automatically react to messages based on keywords or randomly.\n"
        "I also react strictly to abusive messages with 🚫 or 🤬!"
    )


@bot.on_message(filters.text)
async def react_to_message(_, message: Message):
    text = message.text.lower()
    emoji = None

    # Abusive word detection
    if any(bad_word in text for bad_word in ABUSIVE_KEYWORDS):
        emoji = random.choice(ABUSIVE_REACTIONS)

    # Keyword-based reaction
    if not emoji:
        for keyword, reaction in KEYWORD_REACTIONS.items():
            if keyword in text:
                emoji = reaction
                break

    # Random reaction if no keyword/abuse matched
    if not emoji:
        emoji = random.choice(REACTIONS)

    # React with big (animated) emoji
    try:
        await message.react(emoji, big=True)
    except Exception as e:
        print(emoji)
        print(f"Error reacting: {e}")
print("running...")

bot.run()
