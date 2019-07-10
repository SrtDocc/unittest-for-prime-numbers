import unittest


def ifprime(number):
    if number==0:
        return number, "not a prime number!"
    elif number>1:
        for i in range(2,number):
            if number%i==0:
                return False

        return True




class testit(unittest.TestCase):
    def test(self):
        self.assertEqual(ifprime(11), True)





if __name__=='__main__':
    unittest.main()

