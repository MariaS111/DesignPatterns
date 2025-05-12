from controller import EntityApiController
from facade import EntityApiClient
from entity import SomeEntity, SomeImageEntity
from image_api import ImageEntityApi


def client_facade(facade: EntityApiClient) -> None:
    facade.create_entity(SomeEntity(id=1, name="Entity 1", description="Description 1", status="active"))
    facade.create_entity(SomeEntity(id=2, name="Entity 2", description="Description 2", status="inactive"))
    facade.get_all()
    facade.get_entity(2)
    facade.update_entity(SomeEntity(id=1, name="Entity 123", description="Description 123", status="active"))
    facade.get_all()
    facade.delete_entity(2)
    facade.get_all()


def client_image(image_api: ImageEntityApi) -> None:
    image_api.controller.create(SomeEntity(id=1, name="Entity 1", description="Description 1", status="active"))
    image_api.controller.create(SomeEntity(id=2, name="Entity 2", description="Description 2", status="inactive"))

    image_api.set_image(entity_id=1, url="https://example.com/image.png")

    image_url = image_api.get_image(entity_id=1)
    print(f"Image url for entity 1: {image_url}")

    entities = image_api.get_entities_by_filter(status="active")
    print(f"Entities with active status: {entities}")

    entity = image_api.controller.get_one(2)
    print(f"Entity with id 2: {entity}")


if __name__ == "__main__":
    # api_client = EntityApiClient()
    # client_facade(api_client)
    image_api_client = ImageEntityApi()
    client_image(image_api_client)
