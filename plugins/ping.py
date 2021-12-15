# HuzunluArtemis - 2021 (Licensed under GPL-v3)

from pyrogram import Client, filters
from HelperFunc.forceSubscribe import ForceSub
from config import Config
from pyrogram.types.messages_and_media.message import Message
import logging
import time
from HelperFunc.authUserCheck import AuthUserCheck
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

@Client.on_message(filters.command(Config.PING_COMMAND))
async def ping(client: Client, message: Message):
    if not await AuthUserCheck(message): return
    if await ForceSub(client, message) == 400: return
    start_time = int(round(time.time() * 1000))
    if not await AuthUserCheck(message): return
    reply = await message.reply_text("Ping", quote=True)
    end_time = int(round(time.time() * 1000))
    await reply.edit_text(f"Pong\n{end_time - start_time} ms")
