from neo4j import GraphDatabase
from app.settings.config import neo4j_url, neo4j_user, neo4j_password

driver = GraphDatabase.driver(
    neo4j_url,
    auth=(neo4j_user, neo4j_password)
)
