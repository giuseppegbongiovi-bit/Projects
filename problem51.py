import math

#problem 51 Rogawski, section 9.1
#going to use simpsons rule to integrate the problem

b = math.pi/2 #integration point 1
a = (-1)*math.pi/2 #integration point 2
N = 50 #number of partitions
dx = (b-a)/N #delta x

def f(z):
    return 2*math.sqrt(1 - (3/4)*math.sin(z)**2)

total = f(a) + f(b)

for i in range(1,N): #start at step 1, we already have y0 in the total and yN
    if i%2 == 1: #odd numbers need to have a factor of 4
        total = total + 4*f(a + i*dx)
    else: #even numbers have a factor of 2
        total = total + 2*f(a + i*dx)
total = total*dx*(1/3)

print(total)