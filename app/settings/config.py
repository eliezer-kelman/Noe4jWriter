import os
from dotenv import load_dotenv

load_dotenv()

neo4j_url = os.environ['NEO4J_URI']
neo4j_user = os.environ['NEO4J_USER']
neo4j_password = os.environ['NEO4J_PASSWORD']

bootstrap_servers = os.environ['BOOTSTRAP_SERVERS']

neo4j_topic = os.environ['NOE4J_WRITER_TOPIC']
