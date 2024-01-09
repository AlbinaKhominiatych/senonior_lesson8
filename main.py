#логування - вивід помилок через бібліотеку
import logging
#запис у файл
logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode = "w")
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

try:
    print(10/0)
except Exception:
    logging.exception("Exeption")