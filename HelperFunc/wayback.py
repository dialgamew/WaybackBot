# HuzunluArtemis - 2021 (Licensed under GPL-v3)

import logging
import waybackpy
from HelperFunc.randomUserAgent import getRandomUserAgent

from config import LOGGER
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

def saveWebPage(pageurl:str):
    LOGGER.info("wayback running for: " + pageurl)
    user_agent = getRandomUserAgent()
    try:
        wayback = waybackpy.Url(pageurl, user_agent)
        archive = wayback.save()
        LOGGER.info("wayback success for: " + pageurl)
        return archive.archive_url
    except Exception as r:
        LOGGER.error("wayback unsuccess for: " + pageurl + " , " + str(r))
        return None
