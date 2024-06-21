import threading
import time

event = threading.Event()


def lighter():
    '''
    flag=True: 青信号
    flag=False: 赤信号
    '''
    t = 0
    count = 0
    event.set()  # 初期値は青信号

    while True:
        if count > 3:
            break
        if 5 < t <= 10:
            event.clear()  # 赤信号にする
            print("\33[41;1m赤信号...\033[0m")
        elif t > 10:
            event.set()  # 青信号にする
            t = 0
            count += 1
        else:
            print("\33[42;1m青信号...\033[0m")

        time.sleep(0.1)
        t += 1


def car(name):
    distance = 0
    while True:
        if distance > 20:
            break
        if event.is_set():  # 青信号がどうかをチェック
            print("[{}] 前進する...".format(name))
            time.sleep(0.1)
            distance += 1
        else:
            print("[{}] 赤信号のため、信号を待つ...".format(name))
            event.wait()
            # flag=Trueになるまでここでブロッキングする
            print("[{}] 青信号のため、前進開始...".format(name))


light = threading.Thread(target=lighter,)
light.start()

car = threading.Thread(target=car, args=("MINI",))
car.start()

light.join()
car.join()
