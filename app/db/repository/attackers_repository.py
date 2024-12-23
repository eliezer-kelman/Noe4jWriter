from returns.maybe import Maybe
from app.db.database import driver
from app.db.models import Attackers
import uuid


def create_attackers_if_not_exist(attackers: Attackers) -> Maybe[dict]:
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


# def find_attackers_by_parameters(attackers: Attackers) -> Maybe[dict]:
#     with driver.session() as session:
#         query = """
#         MATCH (a:Attackers {
#             primary_group: $primary_group,
#             date: $date
#         })
#         RETURN a.uuid AS uuid, a
#         """
#         parameters = {
#             "primary_group": attackers.primary_group,
#             "date": attackers.date
#         }
#         result = session.run(query, parameters).single()
#         if result is None or result.get('a') is None:
#             return Maybe.from_value(None).map(lambda _: None)
#
#         node = convert_utils.create_attackers_from_data(result.get('a'))
#         return Maybe.from_value({"uuid": result.get('uuid'), "node": node})
