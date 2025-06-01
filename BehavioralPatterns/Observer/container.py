from typing import List
from .observer import Observer


class Container:
    def __init__(self):
        self._cars = []
        self._observers: List[Observer] = []
        self._watched_attrs = {}

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, subj, event: str, details: dict = None):
        for observer in self._observers:
            observer.update(subj, event, details or {})

    def add_car(self, car):
        self._cars.append(car)
        self._watched_attrs[car] = car.__dict__.copy()
        self.notify(car, "car_added")

    def check_changes(self):
        for car in self._cars:
            old_attrs = self._watched_attrs[car]
            current_attrs = car.__dict__
            for key, old_val in old_attrs.items():
                new_val = current_attrs.get(key)
                if old_val != new_val:
                    self._watched_attrs[car][key] = new_val
                    self.notify(car, "car_updated", {
                        "property": key,
                        "old": old_val,
                        "new": new_val
                    })
