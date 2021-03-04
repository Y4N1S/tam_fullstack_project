import sqlite3
from main import main



conn = sqlite3.connect('transport.db')
cur = conn.cursor()
req = "select * from infoarret"
result = cur.execute(req)
for row in result:
    print(row[0],row[1],row[2],row[3])