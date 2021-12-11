from FileScan import *
import unittest


class MyTestCase(unittest.TestCase):
    def test__initEmpty_filename(self):
        with self.assertRaises(ValueError):
            FileScan("")

    def test__initNameNotString(self):
        with self.assertRaises(ValueError):
            FileScan(5)

    def test__initNoExtension(self):
        with self.assertRaises(ValueError):
            FileScan("testFile")

    def test__initWrongPath(self):
        with self.assertRaises(FileNotFoundError):
            FileScan("C:/wrong_path/desktop/testfile.txt")




if __name__ == '__main__':
    unittest.main()
