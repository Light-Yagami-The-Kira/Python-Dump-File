import math
import multiprocessing


def calcSquare(args):
    for i in args:
        print(i**2)


def calcCube(args):
    for i in args:
        print(i**3)


if __name__ == '__main__':
    t = (1, 2, 3, 4)
    p1 = multiprocessing.Process(target=calcSquare, args=(t, ))
    p2 = multiprocessing.Process(target=calcCube, args=(t, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Done")
