list = [6545,58,85,57]

newList = iter(list)

print(newList)

while True:
    try:
        print(next(newList))

    except:
        break
