import threading
import time


def run(n):
    semaphore.acquire()
    time.sleep(0.1)
    print("current thread: {}\n".format(n))
    semaphore.release()


semaphore = threading.BoundedSemaphore(5)  # 5個のスレッドの同時処理を許容する

ts = []
for i in range(22):
    t = threading.Thread(target=run, args=("t-{}".format(i),))
    t.start()
    ts.append(t)

for t in ts:
    t.join()
print('-----全てのスレッドが終了した-----')

# while threading.active_count() != 1:
#     pass  # print(threading.active_count())
# else:
#     print('-----全てのスレッドが終了した-----')
