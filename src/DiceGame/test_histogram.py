import unittest
import matplotlib.pyplot as plotter
import random
#later import class here...


class HistogramTest(unittest.TestCase):
    def test_init(self):
        num_players = 2
        scores = []
        num_rolls = 20
        for i in range(num_rolls):
            round_scores = [random.randint(1, 6) for j in range(num_players)]
            scores.append(round_scores)
        plotter.hist(scores, bins=range(1,8), rwidth=0.8)
        plotter.xticks(range(1, 7))
        plotter.xlabel('Score')
        plotter.ylabel('Frequency')
        plotter.title('Distribution of Scores in Dice Game')
        plotter.show()


if __name__ == '__main__':
    unittest.main 