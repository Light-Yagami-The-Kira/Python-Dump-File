from functools import reduce

def greater(n,m):
    if n>m:
        return n
    else:
        return m

list = [45,96,87,54]

print(reduce(greater,list))