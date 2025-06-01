from .container import Container
from .observer import ConsoleObserver
from CreationalPatterns.CarAbstractFactory.cargo import Volvo
from CreationalPatterns.CarAbstractFactory.tank import Tiger


def main():
    container = Container()
    logger = ConsoleObserver()
    container.attach(logger)

    v = Volvo()
    t = Tiger()
    container.add_car(v)
    container.add_car(t)
    v.tonnage = 25
    t.max_speed = 55
    print("\nChecking for updates...")
    container.check_changes()
