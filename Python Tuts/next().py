list = [6545,58,85,57]

newList = iter(list)

def gen():
    while True:
        try:
            yield (next(newList))

        except:
            break
    

for item in gen():
    print(item)


if __name__=='__main__':
    pass