# texas holdem game engine

class Player:

    def __init__(self, name, money):
        self.name = name
        self.bankroll = money
        self.hand = []
        self.active = 1
        self.equity = 0

        # personality parameters
        self.passive_aggressive = 0.5
        self.tight_loose = 0.5



