from TTT import *
import unittest


class Test(unittest.TestCase):
    def setup_method(self):
        self.p1 = Ui_MainWindow()

    def teardown_method(self):
        del self.p1

    def test_checkWin(self):
        self.A1.setText('X')
        self.A2.setText('X')
        self.A3.setText('x')
        assert self.label.text() == 'Person Wins!'







if __name__ == '__main__':
        unittest.main()