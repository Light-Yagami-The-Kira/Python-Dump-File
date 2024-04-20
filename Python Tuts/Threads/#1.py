import threading


def print_square(*args):
    for arg in args:
        print(arg**2)


def print_cube(*args):
    for arg in args:
        print(arg**3)


t1 = threading.Thread(target=print_square, args=(1, 2, 3, 4, 5))
t2 = threading.Thread(target=print_cube, args=(1, 2, 3, 4, 5))
t1.start()
t2.start()
t1.join()
t2.join()
