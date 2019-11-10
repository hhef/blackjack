import unittest
from blackjack import hand_score


class TestHandScore(unittest.TestCase):
    def test_if_jqk_gives_10_score(self):
        self.assertEqual(hand_score(["J"]), 10)
        self.assertEqual(hand_score(["Q"]), 10)
        self.assertEqual(hand_score(["K"]), 10)

    def test_if_card_gives_score(self):
        self.assertEqual(hand_score(["3"]), 3)
        self.assertEqual(hand_score(["10"]), 10)

    def test_if_ace_gives_10_score_if_score_is_lt_11(self):
        self.assertEqual(hand_score(["A"]), 11)

    def test_if_ace_gives_1_score_if_score_is_gt_11(self):
        self.assertEqual(hand_score(["A", "K", "K"]), 21)


