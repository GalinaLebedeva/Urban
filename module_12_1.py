import runner as r
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        obj = r.Runner('Vasya')
        for i in range(10):
            obj.walk()

        self.assertEqual(obj.distance,50)

    def test_run(self):
        obj2 = r.Runner('Kolya')
        for i in range(10):
            obj2.run()

        self.assertEqual(obj2.distance, 100)

    def test_challenge(self):
        obj3 = r.Runner('Tanya')
        obj4 = r.Runner('Kris')

        for i in range(10):
            obj3.run()
            obj4.walk()

        self.assertNotEqual(obj3.distance, obj4.distance)


if __name__ == "__main__":
    unittest.main()