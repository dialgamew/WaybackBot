# HuzunluArtemis - 2021 (Licensed under GPL-v3)

import logging, os, time
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    if not BOT_USERNAME.startswith('@'): BOT_USERNAME = '@' + BOT_USERNAME # bu satıra dokunmayın.
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", '')
    CHANNEL_OR_CONTACT = os.environ.get("CHANNEL_OR_CONTACT", 'HuzunluArtemis')
    JOIN_CHANNEL_STR = os.environ.get('JOIN_CHANNEL_STR',
        "Merhaba / Hi {}\n\n" + \
        "🇬🇧 First subscribe my channel from button, then send /start again.\n" + \
        "🇹🇷 Önce butondan kanala abone ol, sonra bana /start yaz.")
    YOU_ARE_BANNED_STR = os.environ.get('YOU_ARE_BANNED_STR',
        "🇬🇧 You are Banned to use me.\n🇹🇷 Banlanmışsın ezik.\n\nDestek / Support: {}")
    JOIN_BUTTON_STR = os.environ.get('JOIN_BUTTON_STR', "🇬🇧 Join / 🇹🇷 Katıl")
    OWNER_ID = int(os.environ.get('OWNER_ID', 0)) # give your owner id # if given 0 shell will not works
    AUTH_IDS = [int(x) for x in os.environ.get("AUTH_IDS", "0").split()] # if open to everyone give 0
    AUTH_IDS.append(OWNER_ID)
    # forcesub vars
    FORCE_SUBSCRIBE_CHANNEL = os.environ.get('FORCE_SUBSCRIBE_CHANNEL', '') # force subscribe channel link.
    if FORCE_SUBSCRIBE_CHANNEL == "" or FORCE_SUBSCRIBE_CHANNEL == " " or FORCE_SUBSCRIBE_CHANNEL == None: FORCE_SUBSCRIBE_CHANNEL = None # bu satıra dokunmayın.
    LOGGER.info(f"FORCE_SUBSCRIBE_CHANNEL: {FORCE_SUBSCRIBE_CHANNEL}") # debug
    # commands
    LOG_COMMAND = os.environ.get('LOG_COMMAND','log')
    LOG_COMMAND = [LOG_COMMAND, LOG_COMMAND+BOT_USERNAME] # bu satıra dokunmayın.

    SAVE_COMMAND = os.environ.get('SAVE_COMMAND','save')
    SAVE_COMMAND = [SAVE_COMMAND, SAVE_COMMAND+BOT_USERNAME] # bu satıra dokunmayın.

    PING_COMMAND = os.environ.get('PING_COMMAND','ping')
    PING_COMMAND = [PING_COMMAND, PING_COMMAND+BOT_USERNAME] # bu satıra dokunmayın.

    botStartTime = time.time() # dont touch
    
    AUTO_SAVE_ALL_URLS = str(os.environ.get('AUTO_SAVE_ALL_URLS','False')).lower() == "true"

    HELP_COMMANDS = ["start", "help", "about", "yardım", "h", "y",
        f"start{BOT_USERNAME}", f"help{BOT_USERNAME}", f"about{BOT_USERNAME}",
        f"yardım{BOT_USERNAME}", f"h{BOT_USERNAME}", f"y{BOT_USERNAME}"]

    ALL_COMMANDS = HELP_COMMANDS + LOG_COMMAND + PING_COMMAND + SAVE_COMMAND
    # bu satıra dokunmayın.
