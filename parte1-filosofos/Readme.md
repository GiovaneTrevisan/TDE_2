Jantar dos Filósofos

filosofos_ingenuo_minimo.py — versão ingênua que entra em deadlock.
filosofos_corrigido_minimo.py — versão corrigida, sem deadlock.

Dinâmica do problema
Cinco filósofos sentam-se em uma mesa circular alternando entre pensar e comer. 
Entre cada par de vizinhos há um garfo compartilhado. 
Para comer, o filósofo precisa dos dois garfos ao mesmo tempo: o da esquerda e o da direita.

Por que o impasse surge
No protocolo ingênuo cada filósofo pega primeiro o garfo da esquerda e depois o da direita. 
Se todos pegarem o garfo esquerdo "ao mesmo tempo", cada um fica segurando um garfo e esperando o outro, que está com o vizinho.
Ninguém solta o que tem, ninguém progride.

Condição de Coffman negada na solução
A solução usa hierarquia de recursos, os garfos recebem índices e todo filósofo adquire primeiro o garfo de menor índice e depois o de maior.
Isso nega a espera circular, um ciclo de espera exigiria que algum filósofo segurasse um garfo de índice maior enquanto aguarda um de índice menor, o que a regra proíbe.
Sem possibilidade de ciclo, não há deadlock.
