

import math

def gcd(num1,b):
    r = num1 % b
    if r!= 0:
        print ("---> gcd(" + str(b) + "," + str(r) + ")")
        gcd(b,r)
    else:
        print ("gcd is: " + str(b))


#linear combinations woot
def lc(num1,b):
    r = num1 % b
    if r!= 0:
        print (str(num1) + " = " + str(math.floor(num1/b)) + " * " + str(b) + " + " + str(r))
        lc(b,r)
    else:
        print (str(num1) + " = " + str(math.floor(num1/b)) + " * " + str(b) + " + " + str(r))


        

