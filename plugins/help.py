# HuzunluArtemis - 2021 (Licensed under GPL-v3)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from pyrogram.types.messages_and_media.message import Message
from HelperFunc.authUserCheck import AuthUserCheck
from HelperFunc.forceSubscribe import ForceSub
from HelperFunc.messageFunc import sendMessage
from config import Config
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)


@Client.on_message(filters.command(Config.HELP_COMMANDS))
async def help(client, message: Message):
	if not await AuthUserCheck(message): return
	if await ForceSub(client, message) == 400: return
	sampleText = ""
	if Config.AUTO_SAVE_ALL_URLS:
		sampleText += "🇬🇧 If you send me a link, i will wayback it for you.\n🇹🇷 Bana bir link gönderirsen onu arşivlemeye çalışacağım.\n\n"
	sampleText += f"🇬🇧 You can save a page with: /{Config.SAVE_COMMAND} -Link-\n🇹🇷 Bir sayfayı şöyle kaydedebilirsin: /{Config.SAVE_COMMAND} -Link-\n"
	sampleText += f"🇬🇧 Example / 🇹🇷 Örnek: /{Config.SAVE_COMMAND} https://www.google.com.tr"
	tumad = message.from_user.first_name
	if message.from_user.last_name != None: tumad += f" {message.from_user.last_name}"
	toSendStr = f"Esenlikler / Hi {tumad}\n\n" + sampleText
	reply_markup = None
	if Config.UPDATES_CHANNEL != None and Config.UPDATES_CHANNEL != "" and Config.UPDATES_CHANNEL != " ":
		reply_markup=InlineKeyboardMarkup(
			[
				[InlineKeyboardButton(
				text = "🔥 Güncellemeler / Updates",
				url = "https://t.me/" + Config.UPDATES_CHANNEL)
				]
			])
	await sendMessage(message,toSendStr,reply_markup)
    
