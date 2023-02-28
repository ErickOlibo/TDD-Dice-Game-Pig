import time
import random


class DiceGame:
    def __init__(self, winning_score=100):
        self.players = {}
        self.current_player = None
        self.current_round = 1
        self.winning_score = winning_score
        self.high_scores = {}

    def add_player(self, name):
        self.players[name] = 0
        if len(self.players) == 1:
            self.players["Computer"] = 0

    def remove_player(self, name):
        del self.players[name]

    def change_player_name(self, old_name, new_name):
        self.players[new_name] = self.players.pop(old_name)

    def roll_dice(self):
        print("Rolling the dice...")
        roll = random.randint(1, 6)
        for i in range(6):
            time.sleep(0.2)
            print(random.randint(1, 6), end="\r")
        print(f"The dice rolled: {roll}")
        return roll


    def play_round(self):
        if len(self.players) == 1:
            self.current_player = list(self.players.keys())[0]
            self.players[self.current_player] += self.play_turn(self.current_player)
            computer_score = self.play_turn("Computer")
            self.players["Computer"] += computer_score
            print("\nScores:")
            print(f"{self.current_player}: {self.players[self.current_player]}")
            print(f"Computer: {self.players['Computer']}")
        else:
            for player in self.players:
                self.current_player = player
                self.players[player] += self.play_turn(player)
                print(f"\nScores:")
                for p, s in self.players.items():
                    print(f"{p}: {s}")
                if self.players[player] >= self.winning_score:
                    return player
        self.current_round += 1
        return None

    def play_turn(self, player):
        score = 0
        while True:
            if player == "Computer":
                roll = self.roll_dice()
                if roll == 1:
                    print(f"{player} rolled a 1 and lost their turn!")
                    return 0
                elif score + roll >= 20:
                    print(f"{player} ends their turn with {score} points.")
                    return score
                else:
                    score += roll
                    print(f"{player} rolled a {roll}.")
            else:
                print(f"\n{player}'s turn:")
                input("Press enter to roll the dice...")
                roll = self.roll_dice()
                if roll == 1:
                    print(f"{player} rolled a 1 and lost their turn!")
                    return 0
                else:
                    print(f"{player} rolled a {roll}.")
                    choice = input(f"{player}, would you like to roll again? (y/n)")
                    if choice.lower() == 'n':
                        if "Computer" in self.players:
                            computer_score = self.players["Computer"]
                            if score - computer_score <= -20:
                                add_points = input(f"{player}, the computer is ahead by more than 20 points. Do you want to add 20 points to your score? (y/n)")
                                if add_points.lower() == 'y':
                                    score += 20
                                    print(f"{player} adds 20 points to their score.")
                        print(f"{player} ends their turn with {score} points.")
                        return score
                    else:
                        score += roll

    def play_game(self):
        print("Welcome to the Dice Game!")
        print("Here are the rules: [insert rules here]")
        num_players = int(input("How many players?"))
        for i in range(num_players):
            name = input(f"Enter the name for player {i+1}: ")
            self.add_player(name)

        while True:
            winner = self.play_round()
           

game = DiceGame()
game.play_game()
