from pymongo import MongoClient


class User(object):

    db = MongoClient().valentine

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def save(self):
        self.db.users.insert(self.__dict__)