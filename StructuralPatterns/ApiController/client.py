from controller import EntityApiController
from entity_api_client import EntityApiClient
from entity import SomeEntity, SomeImageEntity
from image_api import ImageEntityApi
from flexible_api_client import FlexibleEntityApiClient


def client_api(facade: EntityApiClient) -> None:
    facade.create_entity(SomeEntity(id=3, name="Entity 3", description="Description 3", status="active"))
    facade.create_entity(SomeEntity(id=4, name="Entity 4", description="Description 4", status="inactive"))
    print(facade.get_all())
    print(facade.get_entity(2))
    facade.update_entity(SomeEntity(id=3, name="Entity 123", description="Description 123", status="active"))
    print(facade.get_all())
    facade.delete_entity(2)
    print(facade.get_all())


def client_image(image_api: ImageEntityApi) -> None:
    image_api.controller.create(SomeEntity(id=3, name="Entity 3", description="Description 1", status="active"))
    image_api.controller.create(SomeEntity(id=4, name="Entity 34", description="Description 2", status="inactive"))

    image_api.set_image(entity_id=3, url="https://example.com/image.png")

    image_url = image_api.get_image(entity_id=3)
    print(f"Image url for entity 1: {image_url}")

    entities = image_api.get_entities_by_filter(status="active")
    print(f"Entities with active status: {entities}")

    entity = image_api.controller.get_one(2)
    print(f"Entity with id 2: {entity}")


def flexible_client(facade: FlexibleEntityApiClient) -> None:
    fields = facade.get_entity_fields(1, 'name', 'status')
    print(f"Entity fields: {fields}")

    filtered_entities = facade.get_entities_by_filter(status="active")
    print(f"Filtered entities: {filtered_entities}")

    custom_entity = facade.get_entity_with_custom_logic(1, lambda entity: entity.name.upper())
    print(f"Custom logic applied: {custom_entity}")


if __name__ == "__main__":
    api_client = EntityApiClient()
    client_api(api_client)
    print()

    image_api_client = ImageEntityApi()
    client_image(image_api_client)
    print()

    flex_api_client = FlexibleEntityApiClient()
    flexible_client(flex_api_client)

