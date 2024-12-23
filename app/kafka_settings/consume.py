import json
from kafka import KafkaConsumer
from app.settings.config import bootstrap_servers



def consume_topic(topic, process_data):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=bootstrap_servers,
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    for message in consumer:
        print(message.value)
        process_data(message.value)