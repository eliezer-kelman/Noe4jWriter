from returns.maybe import Maybe
from app.db.database import driver
from app.db.models import Event
import uuid


def create_event_if_not_exist(event: Event) -> Maybe[dict]:
    with driver.session() as session:
        query = """
        MERGE (e:Event {
            date: $date
        })
        ON CREATE SET 
            e.uuid = $uuid
        RETURN e.uuid AS uuid, e
        """
        parameters = {
            "uuid": str(uuid.uuid4()),
            "date": event.date
        }
        result = session.run(query, parameters).single()
        if result is None or result.get('e') is None:
            return Maybe.from_value(None).map(lambda _: None)

        return Maybe.from_value({"uuid": result.get('uuid'), "node": result.get('e')})
