import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_variables(self) :
        self.assertTrue( filter in globals(), "there is no variable called filter in your program )
        d, nn = np.loadtxt("mydata.dat"), 0 
        for i in range(len(data)) :
            if d[i] == 5 : nn = nn + 1
        self.asserTrue( filter==nn, "the variable called filter has the wrong value" )
