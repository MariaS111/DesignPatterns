from entity import SomeEntity
from controller import EntityApiController


class EntityApiClient:
    def __init__(self):
        self.controller = EntityApiController()

    def create_entity(self, entity: SomeEntity):
        self.controller.create(entity)

    def update_entity(self, entity: SomeEntity):
        self.controller.update(entity)

    def get_entity(self, entity_id: int):
        return self.controller.get_one(entity_id)

    def delete_entity(self, entity_id: int):
        self.controller.delete(entity_id)

    def get_all(self):
        return self.controller.get_many()
