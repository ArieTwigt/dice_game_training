import random


class Dice:

    sides = 6
    score = None

    def __init__(self, name: str, color: str="white"):
        self.name = name
        self.color = color


    # method to throw the dice
    def throw(self):
        # define the choices
        sides_choices = range(1, self.sides + 1)

        # select a random number
        score = random.choice(sides_choices)

        # print the score
        print(f"🎲 {score}")

        # add to the self
        self.score = score


    # method to retreive the score
    def retreive_score(self) -> int:

        # only return the score if it is not none
        if self.score is None:
            print("The score is currently None. Use .throw() first.")
        
        return self.score

    # show the class
    def __repr__(self) -> str:
        return f"Dice block name:{self.name} color:{self.color} sides:{self.sides} score:{self.score}"



# class inheritance
class SpecialDice(Dice):
    
    sides = 12