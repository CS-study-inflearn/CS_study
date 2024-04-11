from multiprocessing import Process, Pipe

def f(conn):
    conn.send(['hello', 42, None])
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # ['hello', 42, None]
    p.join()
