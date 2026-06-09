import threading
import time
import os

lock_a = threading.Lock()
lock_b = threading.Lock()

def thread_1():
    print("T1: tentando pegar A")
    lock_a.acquire()
    print("T1: pegou A")
    time.sleep(0.05)            
    print("T1: tentando pegar B")
    lock_b.acquire()            
    print("T1: pegou B")
    print("T1 concluiu")
    lock_b.release()
    lock_a.release()

def thread_2():
    print("T2: tentando pegar B")
    lock_b.acquire()
    print("T2: pegou B")
    time.sleep(0.05)
    print("T2: tentando pegar A")
    lock_a.acquire()            
    print("T2: pegou A")
    print("T2 concluiu")
    lock_a.release()
    lock_b.release()

t1 = threading.Thread(target=thread_1, name="Thread-1")
t2 = threading.Thread(target=thread_2, name="Thread-2")
t1.start()
t2.start()


time.sleep(2)
bloqueadas = [t.name for t in threading.enumerate() if t.name in ("Thread-1", "Thread-2")]
if bloqueadas:
    print()
    print("=== DEADLOCK DETECTADO ===")
    print("Threads bloqueadas:", bloqueadas)
    os._exit(1)