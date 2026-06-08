import sys
import threading
import time
 
sys.setswitchinterval(1e-5)
 
T = 8          
M = 200000     
 
count = 0      
 
def trabalho_extra():
    s = 0
    for k in range(25):
        s += k
    return s
 
def tarefa():
    global count
    for _ in range(M):
        tmp = count          
        trabalho_extra()    
        count = tmp + 1      

inicio = time.time()
 
threads = []
for _ in range(T):
    t = threading.Thread(target=tarefa)
    threads.append(t)
    t.start()
 
for t in threads:
    t.join()
 
fim = time.time()
 
esperado = T * M
print(f"Esperado: {esperado}")
print(f"Obtido:   {count}")
print(f"Perdidos: {esperado - count}")
print(f"Tempo:    {fim - inicio:.4f} s")