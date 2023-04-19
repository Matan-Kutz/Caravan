import caravan as cr

cards_in_hand = 5
moves = ("play_card", "discard")
winning_min = 21
winning_max = 26

class Player:
    def __init__(self):
        self.deck = cr.Deck()
        self.caravans = []
        for i in range(1,4):
            caravan = cr.Caravan()
            self.caravans.append(caravan)
        self.hand = []
    
    def print_hand(self):
        myList = []
        for card in self.hand:
            myList.append(str(card))
        print("Hand: ", str('[%s]' % ', '.join(map(str, myList))).strip('[]'))
            

class Game:
    def __init__(self):
        self.win = False
        player1 = Player()
        player2 = Player()
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
            legal_move = self.is_legal_move(card, player.caravans[caravan_num])
            if legal_move:
                player.caravans[caravan_num].add_card(card)
            else:
                return
        else:
            index = int(input("Choose index in caravan: "))
            while index < 0 or index >= len(player.caravans[caravan_num]):
                index = int(input("Choose index in caravan: "))
                legal_move = self.is_legal_move(card, player.caravans[caravan_num], index)
            player.caravans[caravan_num].add_card(card, index)
        player.hand.pop(card_index)
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