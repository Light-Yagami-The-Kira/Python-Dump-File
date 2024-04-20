import multiprocessing
global_result = []

def calcSquare(numbers, queue):
    
    for n in numbers:
        queue.put(n*n)

if __name__ == '__main__':
    numbers = (1, 2, 4)
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=calcSquare, args=(numbers, q))
    p.start()
    p.join()

    while q.empty() is False:
        print(q.get())
