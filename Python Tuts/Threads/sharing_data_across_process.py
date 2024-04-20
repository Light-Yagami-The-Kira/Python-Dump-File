import multiprocessing
global_result = []


# def calcSquare(args):
#     global global_result
#     for i in args:
#         print(i**2)
#         global_result.append(i**2)


def calcSquare(args, result, seed):
    seed.value += 10
    for idx, n in enumerate(args):
        result[idx] = n**2


if __name__ == '__main__':
    numbers = (1, 2, 4)
    global_result = multiprocessing.Array('i', 3)
    v = multiprocessing.Value('d', 0.1)
    p = multiprocessing.Process(target=calcSquare, args=(numbers, global_result, v))
    p.start()
    p.join()
    # print("GLOBAL RESULT: ", global_result)
    print("GLOBAL RESULT: ", global_result[:])
    print("V: ", v.value)
