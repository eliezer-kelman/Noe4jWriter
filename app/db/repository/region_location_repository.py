from returns.maybe import Maybe
from app.db.database import driver
from app.db.models import RegionLocation
import uuid


def create_region_if_not_exist(region: RegionLocation) -> Maybe[dict]:
    with driver.session() as session:
        query = """
        MERGE (r:RegionLocation {
            region: $region
        })
        ON CREATE SET 
            r.uuid = $uuid
        RETURN r.uuid AS uuid, r
        """
        parameters = {
            "uuid": str(uuid.uuid4()),
            "region": region.region
        }
        result = session.run(query, parameters).single()
        if result is None or result.get('r') is None:
            return Maybe.from_value(None).map(lambda _: None)

        return Maybe.from_value({"uuid": result.get('uuid'), "node": result.get('r')})
