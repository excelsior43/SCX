import unittest
import SequentialConsecutiveCrossover
class TestSequentialConsequtiveCrossoverAlgorithm(unittest.TestCase):

    def setUp(self):
        self.costMatrix = [
            [999,75, 99, 9, 35, 63, 8],
            [51, 999, 86, 46, 88, 29, 20],
            [100, 5, 999, 16, 28, 35, 28],
            [20, 45, 11, 999, 59, 53, 49],
            [86, 63, 33, 65, 999, 76, 72],
            [36, 53, 89, 31, 21, 999, 52],
            [58, 31, 43, 67, 52, 60, 999]
        ]
        self.P1=(0, 4, 6, 2, 5, 3, 1)
        self.P2=(0, 5, 1, 3, 2, 4, 6)
        self.expectedResult=[1, 5, 7, 2, 4, 3, 6]

    def test_scx(self):
        a = SequentialConsecutiveCrossover(self.costMatrix, self.P1,self.P2)
        a.createSCX()
        result= a.getResult()
        print result
        print self.expectedResult
        # should raise an exception for an unequal values
        self.assertEqual(result, self.expectedResult, "The result is matching")
        print "Done ... "        
        

if __name__ == '__main__':
    unittest.main()
