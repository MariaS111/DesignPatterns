from Producer import BirdProducer
from Interfaces import IFly, IProduceEgg, IDefendEgg, ISing, IDance, ISearchForSpouse, IWalk


class BirdHandler:
    def __init__(self):
        self._bird_producer = BirdProducer()

    def do_bird_action(self):
        sparrow = self._bird_producer.produce_sparrow()
        penguin = self._bird_producer.produce_penguin()

        for bird in [sparrow, penguin]:
            self.handle_bird_moves(bird)
            self.handle_bird_multiplies(bird)
            self.handle_bird_grows_a_child(bird)

    @staticmethod
    def handle_bird_moves(bird):
        if isinstance(bird, IWalk):
            bird.walk()
        if isinstance(bird, IFly):
            bird.fly()

    @staticmethod
    def handle_bird_multiplies(bird):
        if isinstance(bird, ISearchForSpouse):
            bird.search_for_spouse()
        if isinstance(bird, ISing):
            bird.sing()
        if isinstance(bird, IDance):
            bird.dance()

    @staticmethod
    def handle_bird_grows_a_child(bird):
        if isinstance(bird, IProduceEgg):
            bird.produce_egg()
        if isinstance(bird, IDefendEgg):
            bird.defend_egg()


if __name__ == "__main__":
    handler = BirdHandler()
    handler.do_bird_action()
