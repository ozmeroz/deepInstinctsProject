import unittest
from FileScan import *

class MyTestCase(unittest.TestCase):

    def test_wrongFormatLine(self):
        with self.assertRaises(Exception):
            FileScan("Report files/shiftReport4.txt")  # please click OK when given the choice to check this test


    def test_noSleepReport(self):
        self.f8 = FileScan("Report files/shiftReport8.txt")
        self.assertTrue(self.f8.sleeper==False)


    def test_invalidGuardNumber(self):
        with self.assertRaises(ValueError):
            self.f9 = FileScan("Report files/shiftReport9.txt")





if __name__ == '__main__':
    unittest.main()

