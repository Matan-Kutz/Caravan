import caravan as cr
import caravan_game as cg

if __name__ == '__main__':
    print("Starting game")
    game = cg.Game()
    game.init_game()
    for i in range(0, 10):
        game.turn(i%2)
    game.print_game()