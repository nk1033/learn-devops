# Scenario: I need to hit amazon.com url for 3 times if we dont have success response , capture the response in a error_log.tx file and send Email along with the file.


import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

URL = "https://amazon.com"
RETRY_COUNT = 3
ERROR_LOG_FILE = "error_log.txt"

# Email Configuration
SENDER_EMAIL = "sender@yourdomain.com"
RECEIVER_EMAIL = "your_email@example.com"
SMTP_SERVER = "smtp.your-server.com"
SMTP_PORT = 587
SMTP_USERNAME = "your_smtp_username"
SMTP_PASSWORD = "your_smtp_password"

print(f"Attempting to access {URL}...")

def send_email_with_attachment(subject, body, file_path):
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        with open(file_path, "rb") as f:
            attachment = MIMEApplication(f.read(), _subtype="txt")
            attachment.add_header("Content-Disposition", "attachment", filename=file_path)
            msg.attach(attachment)
    except FileNotFoundError:
        print(f"Attachment file not found: {file_path}")

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
            print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Main logic to hit the URL
try:
    for i in range(RETRY_COUNT):
        response = requests.get(URL, timeout=10)
        
        if response.status_code == 200:
            print(f"Success! Received status code 200 on attempt {i + 1}.")
            exit(0)
        else:
            print(f"Attempt {i + 1} failed with status code {response.status_code}.")
            if i < RETRY_COUNT - 1:
                print("Retrying in 5 seconds...")
                # time.sleep(5)  # Uncomment for a real delay
    
    # If the loop completes without success
    print(f"All {RETRY_COUNT} attempts failed. Capturing response and sending email.")
    with open(ERROR_LOG_FILE, "w") as f:
        f.write(response.text)
    
    email_subject = "[ALERT] Failed to access Amazon.com"
    email_body = f"The URL {URL} could not be reached after {RETRY_COUNT} attempts. Please see the attached error log for details."
    
    send_email_with_attachment(email_subject, email_body, ERROR_LOG_FILE)

except requests.exceptions.RequestException as e:
    print(f"A network error occurred: {e}")
    with open(ERROR_LOG_FILE, "w") as f:
        f.write(str(e))
    
    email_subject = "[ERROR] Network Error Accessing Amazon.com"
    email_body = f"A network error occurred while trying to access {URL}. See the attached log for details."
    send_email_with_attachment(email_subject, email_body, ERROR_LOG_FILE)