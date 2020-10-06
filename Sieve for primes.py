def sieve(a): #O(n loglogn) nearly linear
    #all odd mark 1
    for i in range(3,((10**6)+1),2):
        a[i] = 1
    #marking multiples of i form i*i 0. they are nt prime
    for i in range(3,((10**6)+1),2):
        for j in range(i*i,((10**6)+1),i):
            a[j] = 0
    a[2] = 1 #special left case
    return (a)


a = [0]*((10**8)+1)
a = sieve(a)




