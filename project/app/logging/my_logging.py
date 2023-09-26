import logging
from app.logging.my_log_handler import DBHandler
from _datetime import datetime

# create logger with 'spam_application'
logger = logging.getLogger('application_logs')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
log_file_name = datetime.today().strftime('%Y%m%a')

fh = logging.FileHandler(f"logs/{log_file_name}.log")
fh.setLevel(logging.INFO)

# create console handler with a higher log level
# my_handler = DBHandler()
# my_handler.setLevel(logging.ERROR)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

# add the handlers to the logger
# logger.addHandler(my_handler)
logger.addHandler(fh)
