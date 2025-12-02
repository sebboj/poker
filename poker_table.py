import subprocess, sys, math, cards


# texas holdem simulator

MAX_PLAYERS = 10


class Table:

    def __init__(self, table_size = 8):
        if table_size <= MAX_PLAYERS:
            self.table_size = table_size
        else:
            raise Exception(f'Player limit exceeded! Maximum players: {MAX_PLAYERS}')

        self.deck = cards.Cards()
        self.players = [] # list of player objects
        self.shared_cards = [] # aka community cards
        self.burnt_cards = []
        self.pot = 0
        self.button = 0  # index of player with button
        self.small_blind = 1
        self.big_blind = 2
        self.action = 1 # index of player with action (defaults to button + 1 at start of hand)

    def add_player(self, player):
        if len(self.players) < self.table_size:
            self.players.append(player)
        else:
            print(f"Hey {player.name}, the table is full bud...")

    # WIP WIP WIP
    def update_equities(self):
        # update hand equities and ranges of all players given current shared cards
        pass

    # WIP WIP WIP
    def betting_round(self):
        self.update_equities()
        # get action from all players starting from action index
        # loop thru everyone starting w the action index
        # skip anyine that folded or is out
        for player in self.players:
            if player.active:
                action = player.act(self.players)
                if action[0] == "fold":
                    # remove player from round, make them inactive
                    player.active = 0


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
        if deck.validate_deck():
            self.deck = deck
        self.deck.shuffle()
        self.deal_hole_cards() # pre-flop betting
        self.deal_shared(3) # deal flop
        self.deal_shared(1) # deal turn
        self.deal_shared(1) # deal river
        self.cleanup()
        return self.deck # nobody got time to open a new deck every hand

    # play n hands
    def play_hands(self, deck, n):
        for i in range(n):
            self.play_one_hand(deck)
        return self.deck

    '''
            table layout
        
            1   2   3   
        0               4
            7   6   5
            
    '''

    # WIP WIP WIP
    # print table to console (mainly for debugging)
    # every time a game is run you do not want to blow up the console
    def print_table(self):
        with open("logs/game-0/shared_info.txt", "w") as output_file:
            for a in range(100):
                try:
                    figlet_cmd = f"figlet \"Round {a}\""
                    figlet_res = subprocess.run(figlet_cmd, shell=True, capture_output=True, text=True, check=True)
                    output_file.write(figlet_res.stdout)
                    if figlet_res.stderr:
                        output_file.write("\nError Output:\n")
                        output_file.write(figlet_res.stderr)

                except Exception as e:
                    print(f"An unexpected error ocurred: {e}")


        pass

    # WIP WIP WIP
    # creates a new log file of the game for x rounds with timestamps
    # flop turn and river are shown with betting in between
    # this log will be used to create visualizations
    # csv file
    def create_game_log(self):
        # each file be a game?
        #
        # each game contains these two csvs and will have 1:1 row correspondence for each round
        # shared-info
        # pot, community cards, deck
        # each row will be a round
        # player-info
        # money, decicsion each round, cards, range, equity
        # each row will be a round
        pass
