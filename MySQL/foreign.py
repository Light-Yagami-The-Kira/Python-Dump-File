import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Kalilinux@root000@",
    database = "INSTAGRAM",
    autocommit = True
)

users = [
    ("Tim", "kalilinux@root"),
    ("Timmy", "kalilinparor"),
    ("Timothy", "kalilint")
]

user_scores = [
    (45,100),
    (30,200),
    (46,264)
]

cursor = db.cursor()

# cursor.execute("CREATE DATABASE INSTAGRAM")

# cursor.execute("CREATE TABLE USERS (ID INT PRIMARY KEY AUTO_INCREMENT NOT NULL, NAME VARCHAR(50), PASSWORD VARCHAR(50) )")

# cursor.execute(" CREATE TABLE SCORES ( ID INT PRIMARY KEY, FOREIGN KEY(ID) REFERENCES USERS(ID), GAME1 INT DEFAULT 0, GAME2 INT DEFAULT 0 ) ")

# cursor.execute("SHOW TABLES")
# for x in cursor:
#     print(x)

# cursor.executemany("INSERT INTO USERS (NAME,PASSWORD) VALUES (%s,%s)", users)

# cursor.execute("SELECT * FROM USERS")

# for x in cursor:
#     print(x)

# METHOD 2 FOR ADDING USERS
# for x, user in enumerate(users):
#     cursor.execute("INSERT INTO USERS (NAME,PASSWORD) VALUES (%s,%s)", user)
#     last_id = cursor.lastrowid
#     cursor.execute(" INSERT INTO SCORES (ID , GAME1 , GAME2) VALUES (%s,%s,%s) ", (last_id,) + user_scores[x])

cursor.execute("SELECT * FROM USERS")
for a in cursor:
    print(a)
cursor.execute("SELECT * FROM SCORES")
for a in cursor:
    print(a)
