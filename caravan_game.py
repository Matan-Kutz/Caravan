import caravan as cr
import agents

cards_in_hand = 5
moves = ("play_card", "discard")
winning_min = 21
winning_max = 26
time_limit = 10

agents = {
    "human": agents.human_agent,
    "greedy": agents.greedy_agent,
}

class Player:
    def __init__(self, agent_str):
        self.deck = cr.Deck()
        self.caravans = []
        for i in range(1,4):
            caravan = cr.Caravan()
            self.caravans.append(caravan)
        self.hand = []
        self.turn_func = agents[agent_str]
    
    def print_hand(self):
        myList = []
        for card in self.hand:
            myList.append(str(card))
        print("Hand: ", str('[%s]' % ', '.join(map(str, myList))).strip('[]'))
            

class Game:
    def __init__(self, agent_1_str, agent_2_str):
        self.win = False
        player1 = Player(agent_1_str)
        player2 = Player(agent_2_str)
        self.players = []
        self.players.append(player1)
        self.players.append(player2)

    def init_game(self):
        for player in self.players:
            player.deck.shuffle()
            for i in range(1,cards_in_hand + 4):
                new_card = player.deck.deal()
                player.hand.append(new_card)
    
    def game_loop(self):
        #TODO write rest of function
        self.init_game()
        

    def turn(self, player_num):
        legal_move = False
        if player_num == 0:
            player = self.players[0]
        elif player_num == 1:
            player = self.players[1]
        else:
            return
        print("Player ", player_num + 1)
        player.turn_func(self, player_num, time_limit)

        return self.check_winner()
    
    def is_legal_move(self, card, caravan, index = None):
        if card == None or caravan == None:
            return False
        if not card.is_number_card():
            if index != None and (index >= 0 and index < len(caravan)):
                return True
            else:
                return False
        if index == None:
            index = len(caravan)
        dir = caravan.direction
        if dir == None:
            return True
        if isinstance(caravan[len(caravan - 1)], tuple):
            last_card = caravan[len(caravan - 1)][0]
        else:
            last_card = caravan[len(caravan - 1)]
        if (dir == "Up" and card.rank > last_card.rank) or (dir == "Down" and card.rank < last_card.rank):
            return True
        else:
            return False
    
    def winning_sum(self, sum):
        return (sum >= winning_min and sum <= winning_max)
    
    def check_winner(self): # 1 or 2 if game is over, None if not
        player1 = self.players[0]
        player2 = self.players[1]
        points1 = 0
        points2 = 0
        for i in range(0, 3):
            sum1 = player1.caravans[i].caravan_value()
            sum2 = player2.caravans[i].caravan_value()
            win1 = self.winning_sum(sum1)
            win2 = self.winning_sum(sum2)
            if (not win1) and (not win2):
                return False
            if win1 and not win2:
                points1 += 1
            elif win2 and not win1:
                points2 += 1
            elif sum1 > sum2:
                points1 += 1
            elif sum2 > sum1:
                points2 += 1
        if points1 > points2:
            return 1
        elif points2 > points1:
            return 2
        return None
    
    def print_game(self):
        for player in self.players:
            player_index = self.players.index(player)
            f'Player {player_index}:\n'
            for i in range(1,4):
                caravan = player.caravans[i-1]
                f'Caravan {i}: '
                caravan.print_caravan()
                caravan_value = caravan.caravan_value()
                f'Value: {caravan_value}'
                print("\n")
            print("\n")
        return
    
    def get_win_min():
        return winning_min
    
    def get_win_max():
        return winning_max