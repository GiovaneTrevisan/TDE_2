Log do deadlock.py:

T1: tentando pegar A
T2: tentando pegar B
T1: pegou A
T2: pegou B
T1: tentando pegar B
T2: tentando pegar A

=== DEADLOCK DETECTADO ===
Threads bloqueadas: ['Thread-1', 'Thread-2']

As duas threads param em "tentando pegar" e nunca chegam em "concluiu". Sem o monitor threading.enumerate, o programa ficaria travado.

Log do deadlock_corrigido.py:

T1 : tentando pegar A
T2 : tentando pegar A
T1 : pegou A
T1 : tentando pegar B
T1 : pegou B
T1 concluiu
T2 : pegou A
T2 : tentando pegar B
T2 : pegou B
T2 concluiu
Ambas as threads concluiram. Sem deadlock.

A correção impõe uma ordem global: todas as threads pegam sempre A antes de B. 
Com isso, nunca acontece de uma segurar B e esperar A.
A condição de Coffman quebrada é a espera circular.