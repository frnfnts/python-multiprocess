from multiprocessing import Pool


def f(i):
    return i * i


if __name__ == '__main__':
    # 最大4つまで同時にプロセスを実行
    result1 = []
    p = Pool(4)
    for i in range(5):  # 5回実行
        result1.append(p.apply(f, args=(i,)))
    p.close()
    p.join()
    print(result1)

    # with を使ってもかける
    result2 = []
    with Pool(4) as pool:
        for i in range(5):  # 5回実行
            result2.append(pool.apply(f, args=(i,)))
    print(result2)
