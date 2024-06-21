from multiprocessing import Process, Pipe, freeze_support


def f(conn):
    conn.send([42, None, 'hello'])
    print(conn.recv())
    conn.close()


if __name__ == '__main__':
    freeze_support()
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    parent_conn.send('hello from main')
    p.join()
