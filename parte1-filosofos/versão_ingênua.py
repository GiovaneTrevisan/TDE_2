import threading
import time

N = 5
garfos = [threading.Lock() for _ in range(N)]

def filosofo(i):
    esq = i
    dir = (i + 1) % N
    while True:
        print(f"Filósofo {i}: pensando")
        time.sleep(0.1)

        print(f"Filósofo {i}: com fome")
        garfos[esq].acquire()      # pega o garfo da esquerda
        time.sleep(0.1)            # janela que torna o deadlock quase certo
        garfos[dir].acquire()      # tenta o da direita (aqui pode travar)

        print(f"Filósofo {i}: comendo")
        time.sleep(0.1)
        garfos[dir].release()
        garfos[esq].release()

# cria e inicia uma thread para cada filósofo
for i in range(N):
    t = threading.Thread(target=filosofo, args=(i,), daemon=True)
    t.start()

time.sleep(5)
print("Fim (se ninguém comeu, houve deadlock).")