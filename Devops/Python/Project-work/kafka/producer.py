from kafka import KafkaProducer
import time
import os 

KAFKA_TOPIC = "demo-topic"
KAFKA_SERVER = 'localhost:9092'
EMAIL_FILE = 'emails.txt'

def send_to_kafka():
    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
    seen_email = set()

    while True:
        if os.path.exists(EMAIL_FILE):
            with open(EMAIL_FILE, "r", encoding="utf-8") as file:
                for email in file:
                    email = email.strip()
                    if email and email not in seen_email:
                        producer.send(KAFKA_TOPIC, email.encode("utf-8"))
                        print(f"Sent Email {email} to kafka topic {KAFKA_TOPIC}")
                        seen_email.add(email)
        time.sleep(2) ## Check for new emails for every 2 seconds 

    producer.flush()
    producer.close()


send_to_kafka()