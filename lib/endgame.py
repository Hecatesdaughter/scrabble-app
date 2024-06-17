#function to end the game
def game_over(players, tile_bag):
    return all(not player.get_rack_arr() for player in players) or tile_bag.get_remaining_tiles() == 0

def display_final_scores(players):
    print("Game over!")
    for player in players:
        print(f"{player.name}'s final score: {player.score}")

def declare_winner(players):
    if players[0].score > players[1].score:
        print(f"{players[0].name} wins!")
    elif players[0].score < players[1].score:
        print(f"{players[1].name} wins!")
    else:
        print("It's a tie!")

