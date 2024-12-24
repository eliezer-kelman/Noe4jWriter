from datetime import datetime
from typing import Dict
from app.db.models import AttackType, Attackers, Event, CountryLocation, RegionLocation, TargetType



def convert_event_to_classes(event_json: Dict) -> (Event, Attackers, AttackType, TargetType, CountryLocation, RegionLocation):

    location_data = event_json.get("location", {})
    country = CountryLocation(
        country=location_data.get("country", "")
    )
    region = RegionLocation(
        region=location_data.get("region", "")
    )

    attack_data = event_json.get("attack", {})
    attack_type = AttackType(
        attack_type=attack_data.get("type", "")
    )

    target_data = attack_data.get("target", {})
    target_type = TargetType(
        target_type=target_data.get("type", "")
    )

    attackers_data = event_json.get("attackers", {})
    date_string = event_json.get("date", "")
    date_object = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")
    attackers = Attackers(
        primary_group=attackers_data.get("primary_group", "")
    )
    event = Event(
        date=date_object
    )

    return country, region, attack_type, target_type, attackers, event
