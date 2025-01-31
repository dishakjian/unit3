## Code
```.py
import sqlite3

haiku = """Code flows like a stream
Algorithms guide its way
In silence, it solves"""

# Create Database with table Words
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE Words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word TEXT,
    length INTEGER
)
""")
# Insert every word and its length into the database
for word in haiku.split():
    cursor.execute("INSERT INTO Words (word, length) VALUES (?, ?)", (word, len(word)))

# Query the average of all the lengths
cursor.execute("SELECT AVG(length) FROM Words")
out = cursor.fetchone()[0]

# Close the database
conn.close()

print("average word length is", out)

```

## Proof Code Works

![image](https://github.com/user-attachments/assets/b69a9088-9a5a-4cf2-bee3-a9ed7c538d4f)
