

def hcfnaive(a,b):
    if(b==0):
        return a
    else:
        return hcfnaive(b,a%b)

def generate_list (mod_num):
    list_of_rel_prime = []
    for i in range (1, mod_num):
        if hcfnaive(i, mod_num) == 1:
            list_of_rel_prime.append(i)
    return (list_of_rel_prime)

def test(invertible_list, mod_num):
    op = []
    for e in invertible_list:
        if ((e**3) % mod_num) ==  ((e**5) % mod_num):
    
            op.append(e)
    
    print (len(op) == len(invertible_list))
    print (op)
    print (invertible_list)


# num = 8 
# the_list = generate_list(num)
# print (test(the_list, num))
import math

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
def testing():

    for i in range(18,30):
        print ("-----")
        num = 2*(i**2) + 11
        print (is_prime(num))
        print (i, num)


from sympy.ntheory.factor_ import totient

def totient_calc(num):
    return_list = []
    invertible_list = generate_list(num)
    x = totient(num+1)
    for element in invertible_list:
        if ((element**x) % num) in invertible_list:
            return_list.append(element)
    print (len(invertible_list) == len(return_list))


def new_func():
    for i in range (200,500):
        one = totient(i)
        two = totient(i**2)
        if (one < two):
            print (i)
    print ("done!")


def fib(n):
    if n<= 0:
        print("Incorrect input")
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1)+ fib(n-2)
 
def test(n):
    first = fib(n)
    second = 2 * fib(n+1)
    third = fib(n+2)

    target = fib(n+4)

    exp = first + second + third 
    print (first, second,third, target)
    print (target == exp)

# test(4)


# new_func()


# def map(n):
#     new_set = [] 
#     for i in range(1, 2*n + 1):
#         new_set.append(i)
#     new_list = [(num % n) for num in new_set]
#     print (new_set, new_list)

# map(10)


def ew():
    primes = [2,3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    for x in primes:
        print ((x**40) % 100)

def blah2():
    x = 2
    for i in range(1,201):
        print(x,i, (x**i)%100) 

   
ew()
