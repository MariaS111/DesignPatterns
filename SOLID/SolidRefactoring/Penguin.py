from Interfaces import ISing, IDance, IWalk, ISearchForSpouse, IDefendEgg, IProduceEgg


class Penguin(ISing, IDance, IWalk, ISearchForSpouse, IDefendEgg, IProduceEgg):
    def sing(self):
        print("Some Iron Maiden song from 80-th")

    def dance(self):
        print("Shake your body")

    def walk(self):
        print("Walk this way")

    def search_for_spouse(self):
        print("Time to search for the spause")
        self.sing()

    def defend_egg(self):
        print("Hit the enemy")

    def produce_egg(self):
        print("Some magic happens")

