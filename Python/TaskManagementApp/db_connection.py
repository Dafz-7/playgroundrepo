import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="tmastorage",
        password="jonggol",
        database="TaskManagementApp"
    )