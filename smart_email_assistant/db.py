import sqlite3

def init_db():
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            task TEXT,
            deadline TEXT,
            reasoning TEXT,
            sender TEXT,
            email_date TEXT
        )
    """)
    conn.commit()
    conn.close()


def save_task(task, deadline, reasoning, sender):
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute('INSERT INTO tasks (task, deadline, reasoning, sender) VALUES (?, ?, ?, ?)',
              (task, deadline, reasoning, sender))
    conn.commit()
    conn.close()


