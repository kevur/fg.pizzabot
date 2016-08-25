import unittest
import pizzaparser

class ParserTests(unittest.TestCase):
    def test_non_vote(self):
        self.assertEqual([0, 0, 0, 0, 0], pizzaparser.parsePizzaVote(["none"]))

    def test_range(self):
        self.assertEqual([1, 1, 1, 1, 1], pizzaparser.parsePizzaVote(["Mon-Fri"]))
        self.assertEqual([1, 1, 0, 0, 0], pizzaparser.parsePizzaVote(["Mon-Tue"]))
        self.assertEqual([0, 0, 1, 1, 1], pizzaparser.parsePizzaVote(["Wed-Fri"]))

    def test_single(self):
        self.assertEqual([1, 0, 0, 0, 0], pizzaparser.parsePizzaVote(["Mon"]))
        self.assertEqual([1, 1, 0, 0, 0], pizzaparser.parsePizzaVote(["Mon","Tue"]))
        self.assertEqual([1, 0, 0, 0, 1], pizzaparser.parsePizzaVote(["Mon","Fri"]))

    def test_ifneeded(self):
        self.assertEqual([0.5, 0, 0, 0, 0], pizzaparser.parsePizzaVote(["(Mon)"]))
        self.assertEqual([0.5, 0.5, 0, 0, 0], pizzaparser.parsePizzaVote(["(Mon)","(Tue)"]))
        self.assertEqual([0.5, 1, 0, 0, 0], pizzaparser.parsePizzaVote(["(Mon)", "Tue"]))
        self.assertEqual([0.5, 0.5, 0.5, 0, 0], pizzaparser.parsePizzaVote(["(Mon-Wed)"]))

    def test_cheater(self):
        self.assertEqual([1, 0, 0, 0, 0], pizzaparser.parsePizzaVote(["Mon","Mon"]))
        self.assertEqual([1, 0, 0, 0, 0], pizzaparser.parsePizzaVote(["(Mon)","(Mon)"]))
        self.assertEqual([1, 1, 0, 0, 0], pizzaparser.parsePizzaVote(["(Mon)","Mon-Tue"]))
        self.assertEqual([1, 1, 0, 0, 0], pizzaparser.parsePizzaVote(["Mon", "Mon-Tue"]))
        self.assertEqual([1, 0.5, 0, 0, 0], pizzaparser.parsePizzaVote(["Mon", "(Mon-Tue)"]))

    def test_parse_sep(self):
        self.assertEqual([1, 1, 0, 0, 0], pizzaparser.parsePizzaVote(["Mon,", "Tue"]))
        self.assertEqual([1, 1, 0, 0, 0], pizzaparser.parsePizzaVote(["Mon,Tue"]))
        self.assertEqual([1, 1, 0, 0, 0], pizzaparser.parsePizzaVote(["Mon", "Tue"]))

    def test_parse_lan(self):
        self.assertEqual([1, 1, 1, 1, 1], pizzaparser.parsePizzaVote(["mon", "tue", "wed", "thu", "fri"]))
        self.assertEqual([1, 1, 1, 1, 1], pizzaparser.parsePizzaVote(["Mon", "Tue", "Wed", "Thu", "Fri"]))
        self.assertEqual([1, 1, 1, 1, 1], pizzaparser.parsePizzaVote(["mo", "di", "mi", "do", "fr"]))
        self.assertEqual([1, 1, 1, 1, 1], pizzaparser.parsePizzaVote(["Mo", "Di", "Mi", "Do", "Fr"]))

class IssueTests(unittest.TestCase):
    def test_issue1_empty_vote(self):
        self.assertEqual([0, 0, 0, 0, 0], pizzaparser.parsePizzaVote(["null"]))
        self.assertEqual([0, 0, 0, 0, 0], pizzaparser.parsePizzaVote(["{}"]))

    def test_issue2_ifneedbe(self):
        self.assertEqual([1, 0.5, 1, 0.5, 0.5], pizzaparser.parsePizzaVote(["mo,", "(di),", "mi,", "(do-fr)"]))

if __name__ == '__main__':
    unittest.main()