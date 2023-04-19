import caravan_game as cg

def heuristic(game, player_index):
    estimate = 0
    winner = game.check_winner()
    if winner != None:
        if winner - 1 == player_index:
            return float('inf')
        else:
            return float('-inf')
    player1 = game.players[0]
    player2 = game.players[1]
    if player_index == 0:
        modifier = 1
    else:
        modifier = -1
    for i in range(0, len(player1.caravans)):
        caravan_estimate = 0
        caravan1 = player1.caravans[i]
        caravan2 = player2.caravans[i]
        value1 = caravan1.caravan_value()
        value2 = caravan2.caravan_value()

        if game.winning_sum(value1) and game.winning_sum(value2):
            caravan_estimate += (value1 - value2) ^ 2
        elif game.winning_sum(value1):
            caravan_estimate += (game.get_win_min() - value2) + (10 * (value1 - game.get_win_min()))
        elif game.winning_sum(value2):
            caravan_estimate -= (game.get_win_min() - value1) + (10 * (value2 - game.get_win_min()))
        else:
            caravan_estimate += (value1 - value2) ^ 1.5
        estimate += caravan_estimate * modifier