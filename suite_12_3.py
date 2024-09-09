import unittest
import module_12_3 as m3


checks = unittest.TestSuite()
checks.addTest(unittest.TestLoader().loadTestsFromTestCase(m3.TournamentTest))
checks.addTest(unittest.TestLoader().loadTestsFromTestCase(m3.RunnerTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(checks)