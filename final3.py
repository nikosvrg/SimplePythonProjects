import math

def Initiate():
    numbers = raw_input("Insert you Desired Numbers, seperated by whitespaces. \t -> ")
    numsList = [int(n) for n in numbers.split()]
    sum = 0
    s = 0
    size = len(numsList)
    for n in numsList:
        sum = sum + n
    aveg = sum/size
    for n in numsList:
        s = s + (n-aveg)**2
    s = s/size
    print "Standard Deviation of given Numbers: ", math.sqrt(s)




Initiate()