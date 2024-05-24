from utils.dice import Dice, SpecialDice
from typing import Union


class Game:


    def __init__(self, 
                 name: str,
                 dice_block: Union[Dice, SpecialDice],
                 max_turns: int = 5):
        self.name = name
        self.dice_block = dice_block
        self.throws = []
        self.score = 0
        self.max_turns = max_turns
        self.turn = 0

    def throw_dice(self):

        if self.turn < self.max_turns:
            # throw the dice
            self.dice_block.throw()

            # get the score
            result = self.dice_block.retreive_score()

            # add the result to the throws
            self.throws.append(result)

            # change the score
            self.score += result

            # add a turn
            self.turn += 1
        else:
            print("You reached the max turns")

    
    # throw all turns
    def throw_all_turns(self):
        for turn in range(self.max_turns):
            self.throw_dice()

        print("Done")
        
    def __repr__(self) -> str:
        return f"Name: {self.name} throws: {self.throws} - Score: {self.score}"


    