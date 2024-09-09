import runner as r
import runandtour as rnt
import unittest

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(not is_frozen,'Тесты в этом кейсе заморожены')
    def test_walk(self):
        obj = r.Runner('Vasya')
        for i in range(10):
            obj.walk()

        self.assertEqual(obj.distance,50)

    @unittest.skipIf(not is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        obj2 = r.Runner('Kolya')
        for i in range(10):
            obj2.run()

        self.assertEqual(obj2.distance, 100)

    @unittest.skipIf(not is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        obj3 = r.Runner('Tanya')
        obj4 = r.Runner('Kris')

        for i in range(10):
            obj3.run()
            obj4.walk()

        self.assertNotEqual(obj3.distance, obj4.distance)

class TournamentTest(unittest.TestCase):

    is_frozen = True

    def setUp(self):
        self.r1 = rnt.Runner('Усейн', 10)
        self.r2 = rnt.Runner('Андрей', 9)
        self.r3 = rnt.Runner('Ник', 3)

    @unittest.skipIf(not is_frozen, 'Тесты в этом кейсе заморожены')
    def test_first_tournament(self):
        t1 = rnt.Tournament(90, self.r1, self.r3)
        result = t1.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        # self.all_results['test_1'] = result

    @unittest.skipIf(not is_frozen, 'Тесты в этом кейсе заморожены')
    def test_second_tournament(self):
        t2 = rnt.Tournament(90, self.r2, self.r3)
        result1 = t2.start()
        last_runner1 = list(result1.values())
        self.assertTrue(last_runner1[-1] == 'Ник')

    @unittest.skipIf(not is_frozen, 'Тесты в этом кейсе заморожены')
    def test_third_tournament(self):
        t3 = rnt.Tournament(90, self.r1, self.r2, self.r3)
        result2 = t3.start()
        last_runner2 = list(result2.values())
        self.assertTrue(last_runner2[-1] == 'Ник')