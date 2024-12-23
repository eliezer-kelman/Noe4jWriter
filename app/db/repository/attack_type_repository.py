from returns.maybe import Maybe
from app.db.database import driver
from app.db.models import AttackType
import uuid


def create_attack_type_if_not_exist(attack_type: AttackType) -> Maybe[dict]:
    with driver.session() as session:
        query = """
        MERGE (a:AttackType {
            attack_type: $attack_type
        })
        ON CREATE SET 
            a.uuid = $uuid
        RETURN a.uuid AS uuid, a
        """
        parameters = {
            "uuid": str(uuid.uuid4()),
            "attack_type": attack_type.attack_type
        }
        result = session.run(query, parameters).single()
        if result is None or result.get('a') is None:
            return Maybe.from_value(None).map(lambda _: None)

        return Maybe.from_value({"uuid": result.get('uuid'), "node": result.get('a')})
