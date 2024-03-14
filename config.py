from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", "22672907"))
    API_HASH = environ.get("API_HASH", "0ff15ae2153bd8e03b48cb293010bc6a")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7191328870:AAGdI04YGNdasxFik-YWVTEqXXoU1yK_V9s") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://thahero196:lP9Fb6aKL7T0y47U@cluster0.whs2bkj.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "clon")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6287591671').split()]
    
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
