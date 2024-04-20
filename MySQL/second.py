import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Kalilinux@root000@",
    database = "Test_Database",
    autocommit = True
)
# db.autocommit = True

cursor = db.cursor()

cursor.execute("DESCRIBE TEST")
for x in cursor:
    print(x)
# cursor.execute("CREATE TABLE TEST (NAME VARCHAR(50) NOT NULL, CREATED DATETIME NOT NULL, GENDER ENUM('M','F','O') NOT NULL, ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT)")
# cursor.execute("INSERT INTO TEST (NAME, CREATED, GENDER) VALUES (%s,%s,%s)", ("ohny", datetime.now(), "F"))
# cursor.execute("SELECT * FROM TEST")
# for x in cursor:
#     print(x)
# print("-----------------------------")
# cursor.execute("SELECT * FROM TEST WHERE GENDER = 'O' ORDER BY ID DESC")
# for x in cursor:
#     print(x)
# cursor.execute("SELECT NAME, ID FROM TEST WHERE GENDER = 'O' ORDER BY ID ASC")
# for x in cursor:
#     print(x)



# cursor.execute("ALTER TABLE TEST ADD COLUMN FOOD VARCHAR(20) NOT NULL")
# cursor.execute("ALTER TABLE TEST DROP FOOD")
# cursor.execute("ALTER TABLE TEST CHANGE NAME PERSON_NAME VARCHAR(50)")
# cursor.execute("ALTER TABLE TEST CHANGE NAME PERSON_NAME VARCHAR(2)") will give error if already existing data length > new length
cursor.execute("DESCRIBE TEST")
print(cursor.fetchone())
