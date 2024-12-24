from returns.maybe import Maybe
from app.db.database import driver
from app.db.models import Attackers
import uuid


def create_attackers_if_not_exist(attackers: Attackers) -> Maybe[dict]:
    if not attackers.primary_group:
        attackers.primary_group = 'Unknown'
    print(attackers)
    with driver.session() as session:
        query = """
        MERGE (a:Attackers {
            primary_group: $primary_group
        })
        ON CREATE SET 
            a.uuid = $uuid
        RETURN a.uuid AS uuid, a
        """
        parameters = {
            "uuid": str(uuid.uuid4()),
            "primary_group": attackers.primary_group
        }

        result = session.run(query, parameters).single()
        if result is None or result.get('a') is None:
            return Maybe.from_value(None).map(lambda _: None)

        return Maybe.from_value({"uuid": result.get('uuid'), "node": result.get('a')})
