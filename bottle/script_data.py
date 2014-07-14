import sqlite3
db = sqlite3.connect('script.db')
db.execute("CREATE TABLE script (id INTEGER PRIMARY KEY, item CHAR(100) NOT NULL, quant INTEGER NOT NULL)")
db.execute("INSERT INTO script (item,quant) VALUES ('mgt', 4)")
db.execute("INSERT INTO script (item,quant) VALUES ('tvm', 2)")
db.execute("INSERT INTO script (item,quant) VALUES ('odt', 30)")
db.execute("INSERT INTO script (item,quant) VALUES ('rdt', 1)")
db.execute("INSERT INTO script (item,quant) VALUES ('ast', 4)")
db.commit()
