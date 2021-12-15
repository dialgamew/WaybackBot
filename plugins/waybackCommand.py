# HuzunluArtemis - 2021 (Licensed under GPL-v3)

from pyrogram import Client, filters
from HelperFunc.forceSubscribe import ForceSub
from config import Config
from pyrogram.types.messages_and_media.message import Message
import logging, re
from HelperFunc.messageFunc import sendMessage, editMessage
from HelperFunc.authUserCheck import AuthUserCheck
from HelperFunc.wayback import saveWebPage

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

@Client.on_message(filters.command(Config.SAVE_COMMAND))
async def waybackCommand(client: Client, message: Message):
    if not await AuthUserCheck(message): return
    if await ForceSub(client, message) == 400: return
    url = message.text.split(' ', 1)
    try:
        url = url[1]
    except IndexError:
        await sendMessage(message,"🇬🇧 Provide a link with this command. Read /help\n🇹🇷 Komutun yanında url vermen gerek. Tıkla ve oku: /yardim")
        return
    link = None
    try:
        link = re.match(r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*", url)[0]
    except TypeError:
        await sendMessage(message,"🇬🇧 Not a valid link.\n🇹🇷 Geçerli bir link değil.")
        return
    mesaj = await sendMessage(message,"🇬🇧 Wait about 5 minutes. Saving page.\n🇹🇷 5 dakika bekleyin. Sayfa kaydediliyor.")
    retLink = saveWebPage(link)
    if retLink == None:
        await editMessage(mesaj, "🇬🇧 Cannot archieved. Try again later.\n🇹🇷 Arşivlenemedi. Sonra tekrar deneyin.")
        return
    await editMessage(mesaj, f"🇬🇧 Saved webpage. 🇹🇷 Sayfa arşivlendi:\n\n{retLink}")
