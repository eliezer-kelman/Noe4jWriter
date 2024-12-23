from app.db.database import driver


def create_relations_if_not_exist(country_id, region_id, attacker_id, event_id, attack_type_id, target_type_id):
    with driver.session() as session:
        query = """
        MATCH 
            (r:RegionLocation {uuid: $region_uuid}), 
            (c:CountryLocation {uuid: $country_uuid}),
            (e:Event {uuid: $event_uuid}),
            (a:Attackers {uuid: $attacker_uuid}),
            (at:AttackType {uuid: $attack_type_uuid}),
            (tt:TargetType {uuid: $target_type_uuid})
        MERGE (r)-[rel1:CONTAINS]->(c) 
        MERGE (r)-[rel2:OCCURRED_IN]->(e) 
        MERGE (c)-[rel3:OCCURRED_IN]->(e)  
        MERGE (e)-[rel4:OF_TYPE]->(at)  
        MERGE (e)-[rel5:TARGETING]->(tt)  
        MERGE (a)-[rel6:RESPONSIBLE_FOR]->(e)
        RETURN r, c, e, a, at, tt, rel1, rel2, rel3, rel4, rel5, rel6
        """

        parameters = {
            "country_uuid": country_id,
            "region_uuid": region_id,
            "attacker_uuid": attacker_id,
            "event_uuid": event_id,
            "attack_type_uuid": attack_type_id,
            "target_type_uuid": target_type_id
        }

        result = session.run(query, parameters).single()
        if not result:
            return None

        return {
            "region": result["r"],
            "country": result["c"],
            "event": result["e"],
            "attackers": result["a"],
            "attack_type": result["at"],
            "target_type": result["tt"],
            "relations": {
                "contains": result["rel1"],
                "occurred_in_region": result["rel2"],
                "occurred_in_country": result["rel3"],
                "of_type": result["rel4"],
                "targeting": result["rel5"],
                "responsible_for": result["rel6"],
            },
        }
