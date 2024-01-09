#логування - вивід помилок через бібліотеку
import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("debug")
logging.info("Інформація про рядок коду")
logging.warning("Попередження про можливу помилку")
logging.error("Помилка в програмі")
logging.critical("Критична помилка")