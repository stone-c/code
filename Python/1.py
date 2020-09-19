import matplotlib as mpl
import matplotlib.pyplot as plt

#store = []
#def mutl(num, zs):
#        if store[zs] == null:
#            store.append( (num * mut(num, zs - 1)) % 10000000033)
#    return store[zs]

a = int(input("a:"))
b = int(input("b:"))
n = int(input("n:"))

key = {0:1,1:n}

def mutl(num, zs):
    if key[zs] == 0:
        key[zs] = (mutl(num, zs / 2) * mutl(num, zs - zs / 2)) % 10000000033
    return key[zs]

def main(): 

    a = int(input("a:"))
    b = int(input("b:"))
    n = int(input("n:"))

    if n % 10000000033 == 0:
        print(0)

    if n > 10000000033:
        n = n % 10000000033
    
    a1 = n

    for i in range(1,a):
        a1 = a1 * n
        if a1 > 10000000033:
                a1 = a1 % 10000000033
    
    sum = a1

    for i in range(a,b):
        a1 = a1 * n
        if a1 > 10000000033:
            a1 = a1 % 10000000033
            
        sum += a1
            
        if sum > 10000000033:
            sum = sum % 10000000033

    print(sum)