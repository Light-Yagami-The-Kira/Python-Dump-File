import mysql.connector

def describe_table():
    cursor.execute("DESCRIBE Person")
    for x in cursor:
        print(x)

def show_table():
    cursor.execute("SELECT * FROM Person")
    for x in cursor:
        print(x)

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Kalilinux@root000@",
    database = "Test_Database"
)

cursor = db.cursor()

# cursor.execute("CREATE DATABASE Test_Database")

## cursor.execute("CREATE TABLE Person (Name VARCHAR(20), Age smallint UNSIGNED, PersonID int PRIMARY KEY AUTO_INCREMENT)")

describe_table()

show_table()

cursor.execute("INSERT INTO Person(Name, Age) VALUES ('Admsadin', 45)")
cursor.execute("INSERT INTO Person(Name, Age) VALUES (%s, %s)", ('Kdsh', 220))
cursor.execute("INSERT INTO Person(Name, Age) VALUES ('A', 435)")
cursor.execute("INSERT INTO Person(Name, Age) VALUES (%s, %s)", ('Kasssssrisddsh', 320))
db.commit()

show_table()

# cursor.execute("DELETE FROM Person")
# db.commit()
