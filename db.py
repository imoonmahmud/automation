import sqlite3

conn = sqlite3.connect('database.db')
def init_db():
    conn.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            lead_id TEXT PRIMARY KEY,
            message TEXT,
            category TEXT,
            customer_name TEXT,
            product TEXT,
            budget INTEGER
        )
    """)
    conn.commit()

def add_order(id, message, category, name, product, budget):
    conn = sqlite3.connect('database.db')
    try:
        conn.execute("""
            INSERT INTO orders (
                lead_id,
                message,
                category,
                customer_name,
                product,
                budget
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """,(id, message, category, name, product, budget))
        conn.commit()
        return 'saved'
    except sqlite3.IntegrityError:
        return 'duplicate, skipped'
    finally:
        conn.close()
