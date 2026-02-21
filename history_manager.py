import sqlite3

def init_db():
    conn = sqlite3.connect("history.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            test_name TEXT,
            status TEXT,
            execution_time TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_history(username, results):
    conn = sqlite3.connect("history.db")
    c = conn.cursor()
    c.execute("""
        INSERT INTO history (username, test_name, status, execution_time)
        VALUES (?, ?, ?, ?)
    """, (
        username,
        results.get("test_name"),
        results.get("status"),
        results.get("execution_time")
    ))
    conn.commit()
    conn.close()

def get_user_history(username):
    conn = sqlite3.connect("history.db")
    c = conn.cursor()
    c.execute("SELECT * FROM history WHERE username=? ORDER BY id DESC", (username,))
    data = c.fetchall()
    conn.close()
    return data