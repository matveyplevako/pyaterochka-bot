import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s:%(lineno)d'
                           ' - %(message)s', handlers=[logging.StreamHandler()], level=logging.INFO)
logger = logging.getLogger()
