import os, platform, logging

#Logging relevant code
if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                os.getenv('HOMEPATH'),
                                'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'),
                                'test.log')
logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s : %(message)s',
    filename = logging_file,
    filemode = 'w', #'a' opens the file for appending
)

logger = logging.getLogger('test_logger')

