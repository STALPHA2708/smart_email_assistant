from email_reader import fetch_latest_emails
from task_extractor import extract_task_and_reasoning_local
from db import init_db, save_task
from email_sender import send_summary_email
import json
import re
from datetime import date


init_db()
emails = fetch_latest_emails()

summary = ""

for subject, body, sender, email_date in emails:
    print(f"Processing email: {subject}")
    result = extract_task_and_reasoning_local(body)

    try:
        if isinstance(result, str):
            json_match = re.search(r'\[.*\]|\{.*\}', result, re.DOTALL)
            if json_match:
                json_data = json_match.group()
                data_list = json.loads(json_data)
            else:
                print("⚠️ Aucune structure JSON valide trouvée.")
                continue
        else:
            data_list = [result]

        if isinstance(data_list, dict):
            data_list = [data_list]

        for data in data_list:
            task = data.get("task", "N/A")
            deadline = data.get("deadline", "None")
            reasoning = data.get("reasoning", "No reasoning")
            save_task(task, deadline, reasoning, sender)
            summary += f"\n📝 Task: {task}\n📅 Deadline: {deadline}\n🤖 Reasoning: {reasoning}\n"

    except Exception as e:
        print("❌ Error:", e)
        print("🔍 Result content:", result)



if summary:
    send_summary_email(summary)
    print("✅ Email sent with summary!")
else:
    print("No tasks found.")
