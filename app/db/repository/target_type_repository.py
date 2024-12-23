from returns.maybe import Maybe
from app.db.database import driver
from app.db.models import TargetType
import uuid


def create_target_type_if_not_exist(target_type: TargetType) -> Maybe[dict]:
    with driver.session() as session:
        query = """
        MERGE (t:TargetType {
            target_type: $target_type
        })
        ON CREATE SET 
            t.uuid = $uuid
        RETURN t.uuid AS uuid, t
        """
        parameters = {
            "uuid": str(uuid.uuid4()),
            "target_type": target_type.target_type
        }
        result = session.run(query, parameters).single()
        if result is None or result.get('t') is None:
            return Maybe.from_value(None).map(lambda _: None)

        return Maybe.from_value({"uuid": result.get('uuid'), "node": result.get('t')})