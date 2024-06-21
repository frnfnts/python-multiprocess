from multiprocessing import Manager, Pool


def f(i):
    return i * i


if __name__ == '__main__':
    p = Pool(4)
    res = p.map(f, range(10))
    res_async = p.map_async(f, range(10))
    p.close()
    p.join()
    print(res)
    print(res_async.get())
