import threading
import time


def run(n):
    print(f"task {n} started.{threading.current_thread().name}")
    time.sleep(0.3)
    print("done")


t1 = threading.Thread(target=run, args=("t1",))
t2 = threading.Thread(target=run, args=("t2",), name='Thread T2') # ここではsetName()が呼び出される
t1.start()
t2.start()
print(threading.active_count())
t1.join()
t2.join()
print(threading.current_thread().name)  # MainThread
