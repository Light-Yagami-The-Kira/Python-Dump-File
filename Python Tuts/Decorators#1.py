import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, *kwargs)
        end = time.time()
        print(f"{func.__name__} took {(end-start)*1000} milliseconds.")
        return result
    return wrapper


@time_it
def square(*numbers):
    return [number * number for number in numbers]


@time_it
def cube(*numbers):
    return [number * number * number for number in numbers]


if __name__ == '__main__':
    print(square(1, 2, 3, 4))
    print(cube(1, 2, 3, 4))
