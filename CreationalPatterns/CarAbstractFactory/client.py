from factories import AbstractCarFactory, DefaultCarFactory, FirstClientCarFactory, SecondClientCarFactory


def client(factory: AbstractCarFactory):
    vehicle = factory.create_vehicle()
    cargo = factory.create_cargo()
    tank = factory.create_tank()

    vehicle.drive()
    cargo.drive()
    tank.drive()


if __name__ == "__main__":
    client_number = input("Enter client number (0 - Default, 1 - FirstClient, 2 - SecondClient): \n")

    clients = {
        0: DefaultCarFactory(),
        1: FirstClientCarFactory(),
        2: SecondClientCarFactory()
    }

    if client_number.isdigit() and int(client_number) in clients:
        factory = clients[int(client_number)]
        client(factory)
    else:
        print("Incorrect input")