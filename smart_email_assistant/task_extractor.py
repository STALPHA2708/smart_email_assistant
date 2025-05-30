import requests
import time

def extract_task_and_reasoning_local(email_body):
    #Truncate email if too long
    MAX_EMAIL_LENGTH = 4000
    if len(email_body) > MAX_EMAIL_LENGTH:
        email_body = email_body[:MAX_EMAIL_LENGTH]

    #Build the prompt
    prompt = f"""
You are a smart assistant. Analyze the following email and extract:
1. The task
2. Any deadline (if mentioned)
3. A short reasoning: why is this task important?

Email:
\"\"\"{email_body}\"\"\"

Return this in JSON format like:
{{"task": "...", "deadline": "...", "reasoning": "..."}}
"""

    #Make the POST request
    try:
        response = requests.post("http://localhost:1234/v1/chat/completions", json={
            "model": "google/gemma-3-12b",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3
        })

        #Check HTTP status
        if response.status_code != 200:
            print(f"❌ Erreur HTTP {response.status_code}: {response.text}")
            return None

        #Decode JSON response
        try:
            data = response.json()
        except ValueError:
            print("❌ Réponse non JSON :", response.text)
            return None

        #Handle API errors
        if "error" in data:
            print("❌ Erreur retournée par l'API :", data["error"])
            return None

        #Extract and return response content
        if "choices" in data and "message" in data["choices"][0]:
            return data["choices"][0]["message"]["content"]
        else:
            print("❌ Clé 'choices' ou 'message' manquante :", data)
            return None

    except requests.exceptions.RequestException as e:
        print("❌ Erreur réseau :", e)
        return None
