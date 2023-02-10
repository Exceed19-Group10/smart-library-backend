from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv('.env') # load env file


user = os.getenv('user')
# print(user)
password = os.getenv('password')
# print(password)
client = MongoClient(f'mongodb://{user}:{password}@mongo.exceed19.online:8443/?authMechanism=DEFAULT')
db = client['exceed10']
user_database = db['user']
powerbank_database = db['powerbank']
