import unittest
import player


class TestPlayer(unittest.TestCase):
    def test_initialisedlayer(self):
        newPlayer = player.Player("Robert")              #Intantiate player and give it a name of Robert
        newPlayer.name = "Robert"
        nameP = newPlayer.name
        self.assertEqual(newPlayer.get_name(), "Robert") #Assert that the name instantiated inside is Robert
        newPlayer.set_name("Marco")                      #Set a new name to the player
        self.assertEqual(newPlayer.get_name(), "Marco")  #Assert that the name is Marco


    