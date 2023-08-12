from pymongo import MongoClient

class AnimalShelter(object):
    
    def __init__(self, username, password):
        self.client = MongoClient('mongodb://%s:%s@localhost:39329/test?authSource=AAC' % (username, password))
        self.database = self.client["AAC"]

    def create(self, data):
        if data is not None:
            insert_result = self.database.animals.insert_one(data)
            return True if insert_result.inserted_id else False
        else:
            raise Exception("Data parameter is empty")

    def read(self, criteria=None):
        if criteria is not None:
            data = self.database.animals.find(criteria, {"_id": False})
        else:
            data = self.database.animals.find({}, {"_id": False})
        return data

    def update(self, initial, change):
        if initial is not None:
            update_result = self.database.animals.update_many(initial, {"$set": change})
            return update_result.raw_result if update_result.matched_count > 0 else "No document was found"
        else:
            raise Exception("Data parameter is empty")

    def delete(self, remove):
        if remove is not None:
            delete_result = self.database.animals.delete_many(remove)
            return delete_result.raw_result if delete_result.deleted_count > 0 else "No document was found"
        else:
            raise Exception("Data parameter is empty")
