# How to connect to MongoDB
import sys
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


def getClient():
    # Function to connect to MongoDB
    try:
        client = MongoClient(host='localhost', port=27017)
        print("Connected Succesfully")
        return client
    except ConnectionFailure as error:
        sys.stderr.write("Could not connect to MongoDB: %s" % error)
        sys.exit(1)


if __name__ == '__main__':
    getClient()
