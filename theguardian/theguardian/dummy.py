import mysql.connector
import pymysql

# Database configuration
config = {
    'user': 'admin',
    'password': '1Ashish1joseph1',
    'host': '',
    'database': '"database-1"',
    'port': 3306  # MySQL default port
}



# Connect to the database
connection = pymysql.connect(
    host="database-1.clo2uwweuma8.eu-north-1.rds.amazonaws.com",
    port=3306,
    user="admin",
    password='1Ashish1joseph1',
    database="database-1"
)

# Create a cursor object
cursor = connection.cursor()


