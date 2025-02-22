import copy, math

# texas holdem simulator

NEW_DECK = ['AS','2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS','AC','2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC','AH','2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH','AD','2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD',]
MAX_PLAYERS = 10


def validate_deck(deck):
    if len(deck) == 52:
        valid_deck = sorted(copy.deepcopy(NEW_DECK))
        curr_deck = sorted(deck)

        for i in range(52):
            if valid_deck[i] != curr_deck[i]:
                return False
        return True

    return False


class Table:

    def __init__(self, table_size = 8):
        if table_size <= MAX_PLAYERS:
            self.table_size = table_size
        else:
            raise Exception(f'Player limit exceeded! Maximum players: {MAX_PLAYERS}')
        self.deck = []
        self.players = [] # list of player objects
        self.shared_cards = [] # aka community cards
        self.burnt_cards = []
        self.small_blind = 1
        self.big_blind = 2
        self.pot = 0
        self.button = 0 # index of player with button
        self.action = 1 # index of player with action (defaults to button + 1 at start of hand)

    def add_player(self, player):
        if len(self.players) < self.table_size:
            self.players.append(player)
        else:
            raise Exception(f'Table full buddy...')

    # WIP WIP WIP
    def shuffle(self):
        if not self.deck:
            self.open_new_deck()

        # scramble
        # 3 rounds of randomness

        # riffle x 2
        # cut in half then pharoah
        # add slight variance into pharoah so it isnt perfect all the time

        # box cuts
        # cut into four or five stacks and reverse order of stacks

        # riffle
        # cut in half then pharoah
        # add slight variance into pharoah so it isnt perfect all the time

        pass

    def open_new_deck(self):
        self.deck = copy.deepcopy(NEW_DECK)

    # WIP WIP WIP
    def update_equities(self):
        # update hand equities of all players given current shared cards
        pass

    # WIP WIP WIP
    def betting_round(self):
        self.update_equities()
        # get action from all players starting from action index
        pass

    '''
    table layout
    
        1   2   3   
    0               4
        7   6   5
        
    0 starts with the button and it moves clockwise
    cards are dealt starting from button + 1 and clockwise
    
    '''

    def deal_hole_cards(self):
        # beginning from button + 1 deal a card
        player_count = len(self.players)
        curr_player = (self.button + 1) % player_count
        for i in range(player_count * 2):
            self.players[curr_player].hand.append(self.deck.pop()) # deal a card
            curr_player = (curr_player + 1) % player_count # next player index

        self.betting_round()

    # deal n cards to the shared cards and run a round of betting
    def deal_shared(self, n):
        self.burnt_cards.append(self.deck.pop()) # burn one card
        for i in range(n):
            self.shared_cards.append(self.deck.pop()) # deal a card

        self.betting_round()

    def cleanup(self):
        # award pot
        for player in self.players:
            player.bankroll += math.floor(self.pot * player.equity)
            player.equity = 0
        self.pot = 0

        # return all cards to the deck
        self.deck.extend(self.shared_cards)
        self.shared_cards.clear()
        self.deck.extend(self.burnt_cards)
        self.burnt_cards.clear()
        for player in self.players:
            if player.hand:
                self.deck.extend(player.hand)
                player.hand.clear()

        # remove broke bois and make remaining players active
        curr_player = 0
        player_count = len(self.players)
        while curr_player < player_count:
            if self.players[curr_player].bankroll == 0:
                self.players.pop(curr_player)
            else:
                self.players[curr_player].active = 1
                curr_player += 1

        # update button
        self.button = (self.button + 1) % len(self.players)

    def play_one_hand(self, deck):
        if validate_deck(deck):
            self.deck = deck
        self.shuffle()
        self.deal_hole_cards() # pre-flop betting
        self.deal_shared(3) # deal flop
        self.deal_shared(1) # deal turn
        self.deal_shared(1) # deal river
        self.cleanup()
        return self.deck # nobody got time to open a new deck every hand

    # play n hands
    def play_hands(self, deck, n):
        if validate_deck(deck):
            self.deck = deck
        for i in range(n):
            self.play_one_hand()
        return self.deck

    # WIP WIP WIP
    # print table to console (mainly for debugging)
    # every time a game is run you do not want to blow up the console
    def print_table(self):
        pass

    # WIP WIP WIP
    # creates a new log file of the game for x rounds with timestamps
    # flop turn and river are shown with betting in between
    # this log will  be used to create visualizations
    # csv file
    def create_game_log(self):
        pass
