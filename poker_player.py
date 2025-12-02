# texas holdem game engine

STRATS = ["default", "p_t", "p_l", "a_t", "a_l", "micky", "phil"]

class Player:

    def __init__(self, name, money, strat="default"):
        self.name = name
        self.bankroll = money
        self.hand = []
        self.active = 1 # if they are in the game
        self.equity = 0 # determine % odds given a hand from a spectator's view
        self.range = [0, 1] # from the player's perspective
        self.strat = strat

        # basic strat parameters
        self.passive_aggressive = 0.5 # 0 being the most passive and 1 being the most aggressive
        self.tight_loose = 0.5 # 0 being the most tight and 1 being the most loose

    # WIP WIP WIP
    # this is the player brain
    def act(self, players):
        action = "fold"
        chips = 0
        # raise
        # call
        # check
        # fold
        return [action, chips]




