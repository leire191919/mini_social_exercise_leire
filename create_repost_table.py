import sqlite3

con = sqlite3.connect("database.sqlite")
cur =con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS reposts(" \
"id INTEGER PRIMARY KEY AUTOINCREMENT," \
"user_id INTEGER NOT NULL," \
"original_post_id," \
"quote TEXT," \
"created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP," \
"FOREIGN KEY (user_id) REFERENCES users(id)," \
"FOREIGN KEY (original_post_id) REFERENCES posts (id));")
con.commit()
con.close()
print("Correctly created")