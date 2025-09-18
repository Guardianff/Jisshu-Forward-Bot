# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "27485646")
    API_HASH = environ.get("API_HASH", "60d9b4cac575e735e25c1a00885e91d9")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7334566762:AAGh_zrIbGTMyysKoxPccUcHWftu2bJe9rE") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6124951040').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 

    PICS = (environ.get('PICS', 'https://graph.org/file/e223aea8aca83e99162bb.jpg'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://AMMAAAAA:AMMAAAAA@cluster0.mi7ldio.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002724956257'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "-1001940661697") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "False")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
