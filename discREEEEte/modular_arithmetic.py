def mod_operation_concise(n, rem, multiplier):
    for i in list(range(0,n)):
        if (multiplier*i) % n == rem:
            print (i)


def mod_operation(n, rem, multiplier):
    print ("-----------")
    for i in list(range(0,n)):
        print (str(multiplier) + "*" + str(i) + " mod " + str(n) + " = " + str((multiplier*i) % n))
    print ("-----------")
       
print ("part a")
mod_operation (10,4,2)
print ("part b")
mod_operation (10,3,2)
print ("part c")
mod_operation (12,4,9)
print ("part d")
mod_operation (12,6,9)
