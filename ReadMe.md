📦 Installation Guide (Step-by-Step)

1. 📁 Clone the Repository

git clone https://github.com/STALPHA2708/smart_email_assistant
cd smart-email-assistant

2. 🐍 Create a Virtual Environment

python -m venv venv
venv\Scripts\activate   # On Windows
# Or
source venv/bin/activate  # On macOS/Linux

3. ✅ Install Dependencies

pip install python-dotenv requests

4. 🔐 Setup Environment Variables

Create a file called .env in the root directory with your Gmail credentials:

EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_gmail_app_password

📌 You must use an App Password, not your regular Gmail password.
Generate one here: https://myaccount.google.com/apppasswords