## Code
```.py
import sqlite3
from passlib.context import CryptContext

pwd_config = CryptContext(
    schemes=["sha256_crypt"],
    default="sha256_crypt"
)

def check_hash(text, hash_str):
    return pwd_config.verify(text, hash_str)

db_path = "bc_exchange.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT id, sender_id, receiver_id, amount, signature FROM ledger")
transactions = cursor.fetchall()

for tx in transactions:
    tx_id, sender_id, receiver_id, amount, sign = tx
    text = f"id {tx_id},sender_id {sender_id},receiver_id {receiver_id},amount {amount}"
    if check_hash(text, sign):
        print(f"Tx(id={tx_id}) Signature matches")
    else:
        print(f"Tx(id={tx_id}) Error signature")

conn.close()
```

## Proof Code Works
![image](https://github.com/user-attachments/assets/81a3516e-3a4c-4c1b-b0f9-c497b8385157)
