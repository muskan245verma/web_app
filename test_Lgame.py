import unittest
import Lgame

class Test_Listgame(unittest.TestCase):
    def test_commmon_member(self):
        l1=[1,2,3,4]
        l2=[4,3,2,1]
        self.assertEqual(Lgame.common_member(l1,l2),'-----------ELEMENTS OF LIST ARE AS FOLLOWS----------- List 1  : {1, 2, 3, 4} List 2  : {1, 2, 3, 4} Common element in lists  : {1, 2, 3, 4}')
        l1=[1,2,3,4]
        l2=[5,6,7,8]
        self.assertEqual(Lgame.common_member(l1,l2),'No common elements')
    def test_equal(self):
        l1=[1,2,3,4]
        l2=[4,3,2,1]
        self.assertEqual(Lgame.equal(l1,l2),'Lists are of equal length and can be multiplied element wise')
        l1=[1,2,3,4]
        l2=[5,6,7,8,6]
        self.assertEqual(Lgame.equal(l1,l2),'Lists are not of equal length')

if __name__ == '__main__':
    unittest.main()
