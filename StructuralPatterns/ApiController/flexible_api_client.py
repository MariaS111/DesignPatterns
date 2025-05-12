from controller import EntityApiController


class FlexibleEntityApiClient:
    def __init__(self):
        self.controller = EntityApiController()

    def get_entity_fields(self, entity_id: int, *fields) -> dict:
        entity = self.controller.get_one(entity_id)
        if entity:
            return {field: getattr(entity, field, None) for field in fields}
        return {}

    def get_entities_by_filter(self, **filters):
        return self.controller.get_by_filter(**filters)

    def get_entity_with_custom_logic(self, entity_id: int, custom_logic):
        entity = self.controller.get_one(entity_id)
        if entity:
            return custom_logic(entity)
        return None
