import itertools
import random
from collections import deque

# 0 is the bottom of the deck and the end is the top
NEW_DECK = deque(['AS','2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS','AC','2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC','AH','2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH','AD','2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD',])

class Cards:

    def __init__(self, deck=None):
        self.deck = deck

        if self.deck is None:
            self.open_new_deck()
        elif not isinstance(self.deck, deque):
            try:
                self.deck = deque(deck)
            except TypeError:
                print(f"Invalid deck: {self.deck}\nYou must enter a deque or a list bro")
                print("Opening new deck...")
                self.open_new_deck()

        if not self.validate_deck():
            self.deck = deque(sorted(list(self.deck))) # sorting for easier reading
            print("Invalid deck: " + ", ".join(self.deck))
            print("Opening new deck...")
            self.open_new_deck()

    def validate_deck(self):
        if len(self.deck) == 52:
            valid_deck = deque(sorted(list(NEW_DECK.copy())))
            curr_deck = deque(sorted(list(self.deck)))

            for i in range(52):
                if valid_deck[i] != curr_deck[i]:
                    return False
            return True

        return False

    def swap(self, a, b):
        if a == b or self.validate_deck():
            return

        if 0 <= a < 52 and 0 <= b < 52:
            temp = self.deck[a]
            self.deck[a] = self.deck[b]
            self.deck[b] = temp

    def cut_deck(self, var=0.16):
        offset_amt = int(52 * var)
        cut_point = 26 - offset_amt
        cut_point += random.randint(0, 2 * offset_amt)

        # take 0 and move to top, repeat 26 +/- var
        # use : res.append(deque(itertools.islice(self.deck, idx, None)))
        for a in range(cut_point):
            temp = self.deck.popleft()
            self.deck.append(temp)

    def scramble_shuffle(self):
        temp = deque()
        for i in range(52):
            random_index = random.randint(0, len(self.deck) - 1)
            temp.append(self.deck[random_index]) # take a random card from the deck and move to temp
        self.deck = temp.copy()

    # return a set of x random numbers between [lower_bound, upper_bound]
    @staticmethod
    def randints(lower_bound, upper_bound, x):
        res = set()
        options = list(range(lower_bound, upper_bound + 1))
        for a in range(x):
            temp = random.randint(0, len(options) - 1) # pick a random option
            options[temp], options[-1] = options[-1], options[temp] # swap with last element for constant time delete
            res.add(options[-1])
            options.pop()
        return res

    # WIP WIP WIP
    def box_shuffle(self, var=0.08):
        # 3 cuts w variance
        # .25 idx then .33 idx then .5 idx all +- variance
        res = deque()
        cards_left = 52

        idx = int(cards_left * (.75 + var))
        res.append(deque(itertools.islice(self.deck, idx, None)))
        cards_left -= idx # FIX

        idx = int(cards_left * (.66 + var))
        res.append(deque(itertools.islice(self.deck, idx, None)))
        cards_left -= idx # FIX

        idx = int(cards_left * (.5 + var))
        res.append(deque(itertools.islice(self.deck, idx, None)))
        cards_left -= idx # FIX

        return res

    def riffle_shuffle(self, var=0.08):
        left = deque(itertools.islice(self.deck, 0, 26))
        right = deque(itertools.islice(self.deck, 26, 52))
        res = deque()

        errors = self.randints(0, 25, int(52 * var)) # consistent error
        for i in range(26):
            # if random.randint(1, 100) < int(100 * var): # normal error
            if i in errors:
                res.append(right.popleft())
                res.append(left.popleft())
            else:
                res.append(left.popleft())
                res.append(right.popleft())

        self.deck = res.copy()

    def real_shuffle(self, var=0.08):
        if not self.deck:
            self.open_new_deck()

        # washing machine
        self.scramble_shuffle()
        self.scramble_shuffle()
        self.scramble_shuffle()

        self.riffle_shuffle(var)
        self.riffle_shuffle(var)
        self.box_shuffle(var)
        self.riffle_shuffle(var)

        # one cut and done
        self.cut_deck(var*2)

    def deal_top(self):
        return self.deck.pop()

    def open_new_deck(self):
        self.deck = NEW_DECK.copy()

    def __str__(self):
        return ", ".join(self.deck)