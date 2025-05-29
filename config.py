
import os

class Config:

    BOT_TOKEN = os.environ.get('BOT_TOKEN', '7020102164:AAFPCt7-QXvgQhRL7_0nUA_NWAWHl3IYAzc')
    APP_ID = os.environ.get('APP_ID', '20628383')
    API_HASH = os.environ.get('API_HASH', '65a242463b8af9ba7b3c41d8de9738d1')

    #comma seperated user id of users who are allowed to use
    ALLOWED_USERS = [x.strip(' ') for x in os.environ.get('ALLOWED_USERS','1446111611').split(',')]

    DOWNLOAD_DIR = 'downloads'
