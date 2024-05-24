from utils.dice import Dice, SpecialDice
from utils.game import Game


# play the game
if __name__ == "__main__":
    # define the dice block
    my_dice = Dice("Nice dice", "red")
    my_dice_2 = SpecialDice("Nice dice", "red")
    

    # define the game
    my_game = Game("My Game", my_dice, max_turns=10)
    my_game_2 = Game("My Game 2", my_dice_2, max_turns=10)

    # throw all turns
    my_game.throw_all_turns()
    my_game_2.throw_all_turns()

    # print the results
    print(my_game)
    print(my_game_2)

