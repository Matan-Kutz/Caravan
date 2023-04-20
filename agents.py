import caravan_game as cg

moves = ("play_card", "discard")

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

def human_agent(game, agent_id, time_limit):
    legal_move = False
    if agent_id == 0:
        player = game.players[0]
    elif agent_id == 1:
        player = game.players[1]
    else:
        return
    
    player.print_hand()
    action_str = str(input("Play or discard (p/d): "))
    if action_str == "p":
        action = moves[0]
    elif action_str == "d":
        action = moves[1]
    else:
        return
    if action == moves[1]:
        card_index = int(input("Choose card: "))
        while card_index < 0 or card_index > len(player.hand):
            card_index = int(input("Choose card: "))
        player.hand.pop(card_index)
        legal_move = True
        return

    card_index = int(input("Choose card: "))
    while card_index < 0 or card_index > len(player.hand):
        card_index = int(input("Choose card: "))
    caravan_num = int(input("Choose caravan: "))
    while caravan_num < 0 or caravan_num > 2:
        caravan_num = int(input("Choose caravan: "))
    card = player.hand[card_index]
    if card.is_number_card():
        legal_move = game.is_legal_move(card, player.caravans[caravan_num])
        if legal_move:
            player.caravans[caravan_num].add_card(card)
        else:
            return
    else:
        index = int(input("Choose index in caravan: "))
        while index < 0 or index >= len(player.caravans[caravan_num]):
            index = int(input("Choose index in caravan: "))
            legal_move = game.is_legal_move(card, player.caravans[caravan_num], index)
        player.caravans[caravan_num].add_card(card, index)
    player.hand.pop(card_index)

def greedy_agent(game, agent_id, time_limit):
    return 0 #TODO