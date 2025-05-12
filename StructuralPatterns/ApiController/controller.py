from typing import List, Dict
from entity import SomeEntity


class EntityApiController:
    def __init__(self):
        self._entities: Dict[int, SomeEntity] = {}

    def create(self, entity: SomeEntity):
        self._entities[entity.id] = entity
        print(f"Created entity: {entity}")

    def update(self, entity: SomeEntity):
        if entity.id in self._entities:
            self._entities[entity.id] = entity
            print(f"Updated entity: {entity}")
        else:
            print(f"Entity with id {entity.id} not found")

    def get_one(self, entity_id: int) -> SomeEntity | None:
        print(f"Entity by id {entity_id}:")
        return self._entities.get(entity_id)

    def get_many(self) -> List[SomeEntity]:
        print(f"All entities:")
        return list(self._entities.values())

    def get_by_filter(self, **filters) -> List[SomeEntity]:
        print(f"Filtering by: {filters}")
        result = []
        for entity in self._entities.values():
            if all(getattr(entity, k, None) == v for k, v in filters.items()):
                result.append(entity)
        return result

    def delete(self, entity_id: int):
        if entity_id in self._entities:
            del self._entities[entity_id]
            print(f"Deleted entity with id {entity_id}")
        else:
            print(f"Entity with id {entity_id} not found")

    def delete_many(self, ids: List[int]):
        for id in ids:
            self.delete(id)
        print(f"Deleted multiple entities: {ids}")

    def print(self, entity_id: int):
        entity = self.get_one(entity_id)
        if entity:
            print(f"{entity}")
        else:
            print(f"Entity with id {entity_id} not found")

    def print_many(self):
        # print("All entities:")
        for entity in self.get_many():
            print(f"  - {entity}")

    def set_status(self, entity_id: int, status: str):
        entity = self.get_one(entity_id)
        if entity:
            entity.status = status
            print(f"Set status '{status}' for entity id {entity_id}")
        else:
            print(f"Entity with id {entity_id} not found")

    def deactivate(self, entity_id: int):
        self.set_status(entity_id, "inactive")

    def activate(self, entity_id: int):
        self.set_status(entity_id, "active")
