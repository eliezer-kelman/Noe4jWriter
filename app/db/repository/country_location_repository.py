from returns.maybe import Maybe
from app.db.database import driver
from app.db.models import CountryLocation
import uuid


def create_country_if_not_exist(country: CountryLocation) -> Maybe[dict]:
    with driver.session() as session:
        query = """
        MERGE (c:CountryLocation {
            country: $country
        })
        ON CREATE SET 
            c.uuid = $uuid
        RETURN c.uuid AS uuid, c
        """
        parameters = {
            "uuid": str(uuid.uuid4()),
            "country": country.country
        }
        result = session.run(query, parameters).single()
        if result is None or result.get('c') is None:
            return Maybe.from_value(None).map(lambda _: None)

        return Maybe.from_value({"uuid": result.get('uuid'), "node": result.get('c')})
