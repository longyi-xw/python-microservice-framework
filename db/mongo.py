import urllib.parse

from pymongo import MongoClient
from config.settings import settings
from decorator.singleton import singleton


@singleton
class MongoDB:
    client: MongoClient

    def __init__(self, url: str, db_name: str):
        self.client = MongoClient(url)
        self.db = self.client[db_name]
        if self.client.server_info()["version"]:
            print("Succeeded in connecting to the mongodb.")

    def close(self):
        print("Connection closed.")
        self.client.close()


mongo_user = urllib.parse.quote_plus(settings.MONGO_INITDB_ROOT_USERNAME)
mongo_pass = urllib.parse.quote_plus(settings.MONGO_INITDB_ROOT_PASSWORD)
host = settings.MONGO_INITDB_HOST

MongoDB_Wrapper = MongoDB(f"mongodb://{mongo_user}:{mongo_pass}@{host}:27017/?authSource=admin",
                          settings.MONGO_INITDB_DATABASE)
