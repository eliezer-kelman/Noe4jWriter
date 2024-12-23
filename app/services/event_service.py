import app.db.repository.relation_repository as relation_repo
from app.db.models import AttackType, Attackers, Event, CountryLocation, RegionLocation, TargetType
import app.db.repository.country_location_repository as country_repo
import app.db.repository.region_location_repository as region_repo
import app.db.repository.attackers_repository as attackers_repo
import app.db.repository.event_repository as event_repo
import app.db.repository.attack_type_repository as attack_type_repo
import app.db.repository.target_type_repository as target_type_repo


def create_relations_between(country: CountryLocation,
                             region: RegionLocation,
                             attacker: Attackers,
                             event: Event,
                             attack_type: AttackType,
                             target_type: TargetType):

    maybe_country = country_repo.create_country_if_not_exist(country)
    print(f"DEBUG: maybe_country = {maybe_country}")
    country_id = maybe_country.unwrap()["uuid"]
    print(f"DEBUG: country_id = {country_id}")

    maybe_region = region_repo.create_region_if_not_exist(region)
    print(f"DEBUG: maybe_region = {maybe_region}")
    region_id = maybe_region.unwrap()["uuid"]
    print(f"DEBUG: region_id = {region_id}")

    maybe_attacker = attackers_repo.create_attackers_if_not_exist(attacker)
    print(f"DEBUG: maybe_attacker = {maybe_attacker}")
    attacker_id = maybe_attacker.unwrap()["uuid"]
    print(f"DEBUG: attacker_id = {attacker_id}")

    maybe_event = event_repo.create_event_if_not_exist(event)
    print(f"DEBUG: maybe_event = {maybe_event}")
    event_id = maybe_event.unwrap()["uuid"]
    print(f"DEBUG: event_id = {event_id}")

    maybe_attack_type = attack_type_repo.create_attack_type_if_not_exist(attack_type)
    print(f"DEBUG: maybe_attack_type = {maybe_attack_type}")
    attack_type_id = maybe_attack_type.unwrap()["uuid"]
    print(f"DEBUG: attack_type_id = {attack_type_id}")

    maybe_target_type = target_type_repo.create_target_type_if_not_exist(target_type)
    print(f"DEBUG: maybe_target_type = {maybe_target_type}")
    target_type_id = maybe_target_type.unwrap()["uuid"]
    print(f"DEBUG: target_type_id = {target_type_id}")

    return relation_repo.create_relations_if_not_exist(country_id, region_id, attacker_id, event_id, attack_type_id, target_type_id)