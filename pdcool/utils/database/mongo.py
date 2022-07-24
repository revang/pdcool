import pymongo
from pdcool.utils.database.config import db2 as dbconfig


class MongoDBUtil:
    def __init__(self):
        self.host = dbconfig.get("host")
        self.port = int(dbconfig.get("port"))
        self.database = dbconfig.get("database")

    def conn(self):
        self.client = pymongo.MongoClient(f"mongodb://{self.host}:{self.port}")
        self.db = self.client[self.database]

    def close(self):
        self.client.close()

    def queryone(self, collection_name, filter=None):
        self.conn()
        res = self.db[collection_name].find_one(filter=None)
        self.close()
        return res

    def query(self, collection_name, filter=None):
        self.conn()
        res = self.db[collection_name].find(filter)
        self.close()
        return res

    def show(self, collection_name):
        collection = self.db[collection_name]
        cursor = collection.find()
        for row in cursor:
            print(row)

    def insert(self, collection_name, document):
        if not isinstance(document, dict) and not isinstance(document, list):
            raise ValueError(f"invalid document: {document}")

        if isinstance(document, dict):
            self.conn()
            result = self.db[collection_name].insert_one(document)
            self.close()
            return 1

        if isinstance(document, list):
            self.conn()
            result = self.db[collection_name].insert_many(document)
            self.close()
            return len(result.inserted_ids)

    def update(self, collection_name, filter, update):
        self.conn()
        count = self.db[collection_name].update_many(filter, update)
        self.close()
        return count

    def delete(self, collection_name, filter):
        self.conn()
        count = self.db[collection_name].delete_many(filter)
        self.close()
        return count
