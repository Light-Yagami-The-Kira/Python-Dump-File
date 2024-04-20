evens = (i for i in range(101) if i%2 == 0)
print(type(evens))
print(evens)
while True:
    try:
        print(evens.__next__())
    except:
        break