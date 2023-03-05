import time
from .player import Player
from .dice import Dice


class DiceGame:
    def __init__(self, winning_score=100):
        self.players = []
        self.current_player = None
        self.current_round = 1
        self.winning_score = winning_score
        self.high_scores = {}

    def add_player(self, name):
        self.players.append(Player(name))
        if len(self.players) == 1:
            self.players.append(Player("Computer"))

    def remove_player(self, name):
        for player in self.players:
            if player.name == name:
                self.players.remove(player)

    def change_player_name(self, old_name, new_name):
        for player in self.players:
            if player.name == old_name:
                player.name = new_name

    def roll_dice(self):
        print("Rolling the dice...")
        dice = Dice()
        roll = dice.roll()
        for i in range(6):
            time.sleep(0.2)
            print(random.randint(1, 6), end="\r")
        print(f"The dice rolled: {roll}")
        return roll

    def play_round(self):
        if len(self.players) == 1:
            self.current_player = self.players[0].name
            self.players[0].add_score(self.play_turn(self.current_player))
            computer_score = self.play_turn("Computer")
            for player in self.players:
                if player.name == "Computer":
                    player.add_score(computer_score)
            print("\nScores:")
            for player in self.players:
                print(f"{player.name}: {player.score}")
        else:
            for player in self.players:
                self.current_player = player
                player.add_score(self.play_turn(player))
                print(f"\nScores:")
                for p in self.players:
                    print(f"{p.name}: {p.score}")
                if player.score >= self.winning_score:
                    return player
        self.current_round += 1
        return None

    def play_turn(self, player):
        score = 0
        while True:
            if player.name == "Computer":
                roll = self.roll_dice()
                if roll == 1:
                    print(f"{player.name} rolled a 1 and lost their turn!")
                    return 0
                elif score + roll >= 20:
                    print(f"{player.name} ends their turn with {score} points.")
                    return score
                else:
                    score += roll
                    print(f"{player.name} rolled a {roll}.")
            else:
                print(f"\n{player.name}'s turn:")
                input("Press enter to roll the dice...")
                roll = self.roll_dice()
                if roll == 1:
                    print(f"{player.name} rolled a 1 and lost their turn!")
                    return 0
                else:
                    print(f"{player.name} rolled a {roll}.")
                    if player.name == "Computer" and player.score + score >= 20:
                        print(f"{player.name} ends their turn with {score} points.")
                        return score
                    else:
                        choice = input(f"{player.name}, would you like to roll again (y/n)? ")
                        if choice.lower() == "n":
                            print(f"{player.name} ends their turn with {score} points.")
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