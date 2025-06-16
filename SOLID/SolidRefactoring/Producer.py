from enum import Enum
from Sparrow import Sparrow
from Penguin import Penguin


class BirdProducer:
    @staticmethod
    def produce_sparrow() -> Sparrow:
        return Sparrow()

    @staticmethod
    def produce_penguin() -> Penguin:
        return Penguin()
