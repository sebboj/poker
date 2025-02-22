import poker_table, poker_player

if __name__ == '__main__':
    cool_table = poker_table.Table()

    player1 = poker_player.Player('Al', 300)
    player2 = poker_player.Player('Beth', 300)
    player3 = poker_player.Player('Cris', 300)
    player4 = poker_player.Player('Don', 300)
    player5 = poker_player.Player('Ed', 300)
    player6 = poker_player.Player('Finn', 300)
    player7 = poker_player.Player('G', 300)
    cool_table.add_player(player1)
    cool_table.add_player(player2)
    cool_table.add_player(player3)
    cool_table.add_player(player4)
    cool_table.add_player(player5)
    cool_table.add_player(player6)
    cool_table.add_player(player7)

    cool_table.print_table()

    deck = cool_table.play_one_hand([]) # pass with empty list to open a new deck
    print(deck)
    deck = cool_table.play_hands([], 100)
    print(deck)



