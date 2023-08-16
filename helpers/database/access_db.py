# (c) @AbirHasan2005

from plugins.config import Config
from helpers.database.database import Database

db = Database(Config.MONGODB_URI, Config.SESSION_NAME)
