from multiprocessing import Pool

def f(n):
    import time
    # time.sleep(1) 
    return str(n*n)

if __name__ == '__main__':
    array = [1,2,3,4,5]
    p = Pool(processes=5)
    result = p.map(f, array)
    # result = p.map(f, range(10000))

    print("\n".join(result))