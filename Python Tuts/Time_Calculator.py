import time


def work():
    print("Some Work")
    time.sleep(3)


start_time = time.time()
work()
end_time = time.time()

elapsed_time = end_time - start_time

print("Elapsed time:", elapsed_time, "seconds")
