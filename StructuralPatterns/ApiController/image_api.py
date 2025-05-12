from controller import EntityApiController
from entity import SomeImageEntity


class ImageEntityApi:
    def __init__(self):
        self.controller = EntityApiController()

    def set_image(self, entity_id: int, url: str):
        entity = self.controller.get_one(entity_id)
        if entity:
            image_entity = SomeImageEntity(**entity.__dict__, image_url=url)
            self.controller.update(image_entity)
        else:
            print(f"Entity with id {entity_id} not found")

    def get_image(self, entity_id: int):
        entity = self.controller.get_one(entity_id)
        if entity:
            return getattr(entity, 'image_url', None)
        else:
            print(f"Entity with id {entity_id} not found")
            return None

    def get_entities_by_filter(self, **filters):
        entities = self.controller.get_by_filter(**filters)
        if entities:
            return entities
        else:
            print(f"No entities found")
            return []


