import sqlite3

conn = sqlite3.connect('database.db')
def init_db():
    conn.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id TEXT PRIMARY KEY,
            customer_name TEXT,
            amount TEXT
        )
    """)
    conn.commit()

def add_order(id, name, amount):
    conn = sqlite3.connect('database.db')
    try:
        conn.execute("""
            INSERT INTO orders (
                order_id,
                customer_name,
                amount
            )
            VALUES (?, ?, ?)
        """,(id, name, amount))
        conn.commit()
        return 'saved'
    except sqlite3.IntegrityError:
        return 'duplicate, skipped'
    finally:
        conn.close()

init_db()