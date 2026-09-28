import sqlite3

conn = sqlite3.connect('events.db')
conn.execute(
    """
    CREATE TABLE IF NOT EXISTS orders (
        order_id TEXT PRIMARY KEY,
        event TEXT
    )
""")

def save_order(order_id, event):
    conn = sqlite3.connect('events.db')
    try:
        conn.execute("INSERT INTO orders (order_id, event) VALUES (?, ?)",
                     (order_id, event))
        conn.commit()
        return 'saved'
    except sqlite3.IntegrityError:
        return 'duplicate, skipped'


for row in conn.execute("SELECT * FROM orders"):
    print(row)