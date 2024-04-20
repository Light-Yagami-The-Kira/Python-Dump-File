import queue
import threading

def sq(number, q):
    for i in number:
        q.put(i*i)

q = queue.Queue()
t1 = threading.Thread(target=sq, args=([1,2,3], q))
t1.start()
t1.join()
while not q.empty():
    print(q.get())
