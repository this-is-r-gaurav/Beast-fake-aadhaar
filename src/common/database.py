import pymongo
class Database:
    _URI = 'mongodb://rg:1234@ds223009.mlab.com:23009/fake-aadhaar'
    _DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database._URI)
        Database._DATABASE = client['fake-aadhaar']

    @staticmethod
    def insert(collection, data):
        Database._DATABASE[collection].insert(data)

    @staticmethod
    def delete(collection, query):
        Database._DATABASE[collection].remove(query)

    @staticmethod
    def find(collection, query):
        return Database._DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database._DATABASE[collection].find_one(query)

    @staticmethod
    def count(collection,query):
        return Database._DATABASE[collection].count(query)

    @staticmethod
    def update(collection,query, data):
        Database._DATABASE[collection].update(query,data,upsert = True)

