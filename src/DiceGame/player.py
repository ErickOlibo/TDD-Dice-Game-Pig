"""This module manages the characteristics of the player object."""
from brain import Brain
from dice import Dice
from helpers import Turn


class Player:
    """A Player is a participant to the game of Pig.

    There are 2 types:
        - user: played by an person through the keyboard input.
        - cpu: played internally by the computer.
    The qualities of the dice and brain differs.

    Attributes:
        name: the name of the player.
        brain (Brain): This brain is available only to the computer to
        similate a sort of intelligent behaviour.
        dice (Dice): each player rolls with their own dice.
        A user has a balanced dice, while the CPU has a weigthed one.
    """

    def __init__(self, name: str, brain: Brain = None, dice: Dice = Dice()):
        """
        Initialize a Player object.

        Description:
        This method initializes a Player object with a name,
        a Brain object (optional) and a Dice object.

        Args:
        - name (str): The name of the player.
        - brain (Brain): The brain of the player, which determines the player's
                         decision making (optional).
        - dice (Dice): The dice used by the player (optional).

        """
        self._name = name
        self._brain = brain
        self._dice = dice
        self._score = 0
        self._rolls = []

    @property
    def name(self) -> str:
        """
        Get player's name.

        Description:
        This method returns the player's name.

        Returns:
        - (str): The player's name.

        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        Set the name of the player.

        Args:
        - name (str): The new name for the player.

        """
        self._name = name

    @property
    def brain(self) -> Brain:
        """
        Get the current player's brain object.

        Description:
        This method returns the current player's brain object.

        Returns:
        - (Brain): The current player's brain object.

        """
        return self._brain

    @brain.setter
    def brain(self, brain: Brain):
        """
        Set the brain of a player.

        Description:
        This method sets the brain of a player to the specified Brain instance.

        Args:
        - brain (Brain): The Brain instance to set as the player's brain.

        """
        if not isinstance(brain, Brain):
            raise TypeError('brain must be of instance Brain!')
        self._brain = brain

    @property
    def score(self) -> int:
        """
        Get the score of the player.

        Description:
        This method returns the score of the player.

        Returns:
        - int: The score of the player.

        """
        return self._score

    @property
    def rolls(self) -> list[int]:
        """
        Get the rolls that the player has made.

        Returns:
        - list[int]: A list of integers representing the
                     rolls made by the player.

        """
        return self._rolls

    def playing_choice(self, score, turn_points) -> Turn:
        """
        Determine a player's choice during their turn.

        Description:
        This method takes the player's current score and turn points as inputs,
        and returns the player's chosen action during their turn.
        If the player has a brain, it uses the brain's action method
        to determine the choice, otherwise it returns None.

        Args:
        - score (int): The player's current score.
        - turn_points (int): The points accumulated during the current turn.

        Returns:
        - A Turn object representing the player's chosen action.

        """
        if self._brain is not None:
            return self._brain.action(score, turn_points)
        else:
            return None

    def add_points_to_score(self, points: int):
        """
        Add points to player's score.

        Description:
        This method takes an integer as input and adds it to the
        player's current score.

        Args:
        - points (int): The number of points to be added to the player's score.
        """
        self._score += points

    def roll_dice(self) -> int:
        """
        Roll a dice and update the list of rolls.

        Description:
            This method simulates rolling a dice, using the `_dice` attribute
            of the current instance to generate a random integer.
            The value of the roll is added to the `_rolls` list,
            which keeps track of all the rolls that have
            been made. Finally, the method returns the value of the roll.

        Args:
            None

        Returns:
            int: The value of the rolled dice.
        """
        roll = self._dice.roll()
        self._rolls.append(roll)
        return roll

    def reset_rolls(self):
        """
        Reset the list of rolls to an empty list.

        Description:
            This method resets the `_rolls` attribute of the current instance
            to an empty list. This is useful for starting a new game or round,
            where you want to clear out the old rolls and start fresh.

        """
        self._rolls = []
