"""
Created on Thu May  9 10:59:18 2019
@author: ernekz
"""

import pymongo
from pymongo import MongoClient
import pandas as pd
from pymongo import MongoClient
import time
import random
from faker import Faker
import datetime

client = pymongo.MongoClient("mongodb+srv://vama:vama@cluster0.cop8f.mongodb.net/app?retryWrites=true&w=majority")
db = client.app
collection = db['test']
#Checking the server status to the mongoDB
try:
	db.command("serverStatus")
except Exception as e:
	print(e)
else:
	print("you are connected!")

def create_names(fake):
    for x in range(30):
        name = fake.first_name()
        date = datetime.datetime.now()
        hum = random.randrange(10, 100, 1)
        temp = random.randrange(16, 34, 1)
        room_id = random.randrange(1, 10, 1)

        result = db.test.insert_one(
            {
                'date': date,
                'temperature': temp,
                'humidity': hum,
                'room_id': room_id,
                'name': name
            }
        )

        print('id: ' + str(result.inserted_id) + ' name: ' + name)
        time.sleep(1)


if __name__ == '__main__':
    fake = Faker()
    create_names(fake)