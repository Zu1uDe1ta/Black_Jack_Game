import unittest
import math
import blackjack as bj

class CardTestCase(unittest.TestCase):
        """Unit tests for Blackjack Card class"""
    def test_value_of_card(self):
        """Does card return correct value?"""
        card = Card("5")
        self.assertEqual(card.value(), 5)
        card = Card("A")
        self.assertEqual(card.value(), 11)
        card = Card("J")
        self.assertEqual(card.value(), 10)



class VivaComprehensionsTest(unittest.TestCase):

    def test_gen_list(self):
        test_cases = [
            ([1, 3, 5, 7, 9, 11, 13], (0, 15, vc.Parity.ODD)),
            ([0, 2, 4, 6, 8, 10, 12, 14], (0, 15, vc.Parity.EVEN)),
            ([77, 79, 81], (77, 82, vc.Parity.ODD)),
            ([150, 152, 154, 156], (150, 157, vc.Parity.EVEN))

        ]

        for expected, params in test_cases:
            with self.subTest(f"{params} -> {expected}"):
                actual = vc.gen_list(params[0], params[1], params[2])
                self.assertEqual(expected, actual)

    def test_gen_dict(self):
        test_cases = [
            ({1: 1, 2: 4, 3: 9, 4: 16, 5: 25}, (1, 6, lambda x: x ** 2)),
            ({5: 120, 6: 720, 7: 5040}, (5, 8, lambda x: math.factorial(x))),
        ]

        for expected, params in test_cases:
            with self.subTest(f"{params} -> {expected}"):
                actual = vc.gen_dict(params[0], params[1], params[2])
                self.assertEqual(expected, actual)

    def test_gen_set(self):
        test_cases = [
            ({'A', 'B', 'N'}, 'banana'),
            ({'B', 'N'}, 'bAnAnA'),
            ({'I', 'S', 'P'}, 'Mississippi'),
            (set(), 'MISSISSIPPI'),
        ]

        for expected, param in test_cases:
            with self.subTest(f"{param} -> {expected}"):
                actual = vc.gen_set(param)
                self.assertEqual(expected, actual)
