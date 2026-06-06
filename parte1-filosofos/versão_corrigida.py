import threading
import time

N = 5
garfos = [threading.Lock() for _ in range(N)]

def filosofo(i):
    esq = i
    dir = (i + 1) % N
    primeiro = min(esq, dir)   # sempre o garfo de MENOR índice
    segundo = max(esq, dir)    # depois o de MAIOR índice
    while True:
        print(f"Filósofo {i}: pensando")
        time.sleep(0.1)

        print(f"Filósofo {i}: com fome")
        garfos[primeiro].acquire()   # pega primeiro o de menor índice
        time.sleep(0.1)              # mesma janela da versão ingênua
        garfos[segundo].acquire()    # depois o de maior índice

        print(f"Filósofo {i}: comendo")
        time.sleep(0.1)
        garfos[segundo].release()
        garfos[primeiro].release()

# cria e inicia uma thread para cada filósofo
for i in range(N):
    t = threading.Thread(target=filosofo, args=(i,), daemon=True)
    t.start()

time.sleep(5)
print("Fim.")