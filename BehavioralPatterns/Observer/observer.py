from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, subj, event: str, details: dict):
        pass


class ConsoleObserver(Observer):
    def update(self, subj, event: str, details: dict):
        if event == "car_added":
            print(f"[Added] {subj.__class__.__name__} added to container")
        elif event == "car_updated":
            prop = details['property']
            old = details['old']
            new = details['new']
            print(f"[Updated] {subj.__class__.__name__}: '{prop}' changed from {old} to {new}")
