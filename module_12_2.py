import runandtour as rnt
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.r1 = rnt.Runner('Усейн', 10)
        self.r2 = rnt.Runner('Андрей', 9)
        self.r3 = rnt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print({key: str(runner) for key, runner in result.items()})

    def test_1(self):
        t1 = rnt.Tournament(90, self.r1, self.r3)
        result = t1.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results['test_1'] = result

    def test_2(self):
        t2 = rnt.Tournament(90, self.r2, self.r3)
        result1 = t2.start()
        last_runner1 = list(result1.values())
        self.assertTrue(last_runner1[-1] == 'Ник')
        self.all_results['test_2'] = result1

    def test_3(self):
        t3 = rnt.Tournament(90, self.r1, self.r2, self.r3)
        result2 = t3.start()
        last_runner2 = list(result2.values())
        self.assertTrue(last_runner2[-1] == 'Ник')
        self.all_results['test_3'] = result2

if __name__ == "__main__":
    unittest.main()
