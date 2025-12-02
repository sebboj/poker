from cards import Cards
from poker_table import Table

fresh_deck = Cards()
print(fresh_deck)
fresh_deck.riffle_shuffle()
print(fresh_deck)
print(Cards.randints(0, 51, 3))

fresh_table = Table()
fresh_table.print_table()


