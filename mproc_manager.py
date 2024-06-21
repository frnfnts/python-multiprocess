from multiprocessing import Manager, Pool


def f(d, li, i):
    d[i] = i
    d[str(i)] = str(i)
    li.append(i)
    print(i)


if __name__ == '__main__':
    p = Pool(4)
    with Manager() as manager:
        shared_dict = manager.dict()
        shared_list = manager.list()
        for i in range(5):
            p.apply_async(f, args=(shared_dict, shared_list, i))
        p.close()
        p.join()
        print(shared_dict)
        print(shared_list)
