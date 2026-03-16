import math

#Newtons Method to solve section 10.4 exercise 33.c for time to empty

def f1(x): #f(x)
    return 20*math.log(1+x) - 5*x + 100

def f2(x): # derivative of f(x), f'(x)
    return 20*(1/(1+x)) - 5

epsilon = 0.0001
xn = 5
count = 0
t = True
while t == True and count < 10000:
    prev = xn
    xn = xn - f1(xn)/f2(xn)
    if abs(prev - xn) < epsilon:
        t = False
    count = count + 1


print("iterations: ")
print(count)
print(xn)