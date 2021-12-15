# HuzunluArtemis - 2021 (Licensed under GPL-v3)

import logging
from config import Config
import pyrogram
import logging, os
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

if __name__ == '__main__':
    
    plugins = dict(root = 'plugins')
    
    app = pyrogram.Client("WaybackBot",
      bot_token = Config.BOT_TOKEN,
      api_id = Config.APP_ID,
      api_hash = Config.API_HASH,
      plugins = plugins)
    
    app.start()
    
    botUserName = app.get_me()['username']
    LOGGER.info(f"#botUsername: {botUserName}")
    LOGGER.info(msg="App Started.")
    LOGGER.info("ownerid: " + str(Config.OWNER_ID))
    try:
      app.send_message(text= "ayaktayım efendim.\ni am awaken.",chat_id=Config.OWNER_ID)
    except Exception as t:
      LOGGER.info("you did not entered ownerid. no problem.")
      LOGGER.error(str(t))
    
    pyrogram.idle()
    
    LOGGER.info(msg="App Stopped.")
