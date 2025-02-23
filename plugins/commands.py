import os
import os
import time
import psutil
import shutil
import string
import asyncio
if bool(os.environ.get("WEBHOOK", False)):  
    from plugins.config import Config
else:
    from sample_config import Config
from translation import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@Client.on_message(filters.command(["start"]) & filters.private)
async def start(bot, update):
    await update.reply_text(
        text=Translation.START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=Translation.START_BUTTONS)
