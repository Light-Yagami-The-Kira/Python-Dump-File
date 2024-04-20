'''
ITERABLE -> __ITER__() OR __GETITEM__()
ITERATOR -> __NEXT__()

GENERATOR -> ONE TIME ITERATOR
'''

def gen(n):
    for i in range(n):
        yield i

g = gen(100)
print(g)

print(g.__next__())
print(g.__next__())
print(g.__next__())


h = "Harry"
for char in h:
    print(char)

H = iter(h)
print(H.__next__())
print(H.__next__())
print(H.__next__())