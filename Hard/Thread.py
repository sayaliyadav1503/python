from threading import Thread
import time

def task(name):
    print(f"Task {name} started")
    time.sleep(2)
    print(f"Task {name} finished")

t1 = Thread(target=task, args=("A",))
t2 = Thread(target=task, args=("B",))

t1.start()
t2.start()

t1.join()
t2.join()
