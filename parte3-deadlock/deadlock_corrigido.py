import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()


def tarefa(nome):
    print(nome, ": tentando pegar A")
    lock_a.acquire()
    print(nome, ": pegou A")
    time.sleep(0.05)
    print(nome, ": tentando pegar B")
    lock_b.acquire()
    print(nome, ": pegou B")
    print(nome, "concluiu")
    lock_b.release()
    lock_a.release()

t1 = threading.Thread(target=tarefa, args=("T1",))
t2 = threading.Thread(target=tarefa, args=("T2",))
t1.start()
t2.start()
t1.join()
t2.join()
print("Ambas as threads concluiram. Sem deadlock.")