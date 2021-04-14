import sys
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from getClient import getClient

'''
Function to get handle to a database
Input:
c- mongodb connection
name - name of database
'''


def getDatabase(c, db_name):
    db = c[db_name]
    return db


'''
Function to check if connection and db handle connection are the same
Input:
c- mongodb connection
name - name of database
'''


def check_connection(client, db_handle):
    assert db_handle.client == client
    print("Database handle connection is the same as input comment")


if __name__ == '__main__':
    db_name = input('Enter the name of a database\n')
    client = getClient()  # Create a connection
    db = getDatabase(client, db_name)
    # check_connection(client, db_handle)
