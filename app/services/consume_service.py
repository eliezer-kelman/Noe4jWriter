import app.utils.convert_utils as convert_utils
import app.services.event_service as event_service

def handle_consume(data):
    country, region, attack_type, target_type, attackers, event = convert_utils.convert_event_to_classes(data)
    return event_service.create_relations_between(country, region, attackers, event, attack_type, target_type)