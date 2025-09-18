from kafka import KafkaConsumer

KAFKA_TOPIC = 'DEMO-TOPIC'
KAFKA_SERVER = "localhost:9092"
 
def consumer_from_kafka():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_SERVER,
        auto_offset_reset='erliest',
        enable_auto_commit=True
    )

    print("waiting for messages..")

    for message in consumer:
        email = message.value.decode("utf-8")
        print(f"New signup with email {email}")

consumer_from_kafka()