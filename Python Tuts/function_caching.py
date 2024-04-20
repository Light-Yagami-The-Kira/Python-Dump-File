import time
from functools import lru_cache

@lru_cache(maxsize=2)  ## PICHLI 2 VALUE KO CACHE KAREGA
def work(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    print(work(2))
    print(work(3))
    print(work(4))
    print(work(3))
    print(work(2))