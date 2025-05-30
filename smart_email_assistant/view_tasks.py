import sqlite3

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("SELECT id, task, deadline, reasoning FROM tasks ORDER BY id DESC LIMIT 10")
rows = cursor.fetchall()

for row in rows:
    print(f"\n📝 Task: {row[1]}\n📅 Deadline: {row[2]}\n🤖 Reasoning: {row[3]}")

conn.close()
