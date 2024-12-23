from app.kafka_settings.consume import consume_topic
from app.services.consume_service import handle_consume
from app.settings.config import neo4j_topic

if __name__ == '__main__':
    consume_topic(neo4j_topic, handle_consume)