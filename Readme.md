TDE — Concorrência: Impasses, Threads e Semáforos
Grupo: TDE1
Integrante: Giovane Renato Trevisan

Linguagem
Python 3
Não há dependências externas, então não é preciso pip install nem ambiente virtual.

Vídeo de apresentação
#Link do video#

Estrutura do projeto
TDE1/
├── parte1/   Jantar dos Filósofos
├── parte2/   Threads e Semáforos
└── parte3/   Deadlock
Cada pasta tem seu próprio README com o detalhamento daquela parte.

Relatório técnico
O detalhamento completo (logs, pseudocódigo e explicações) está no README de cada pasta.

Parte 1 — Jantar dos Filósofos
Cinco filósofos disputam garfos compartilhados. Na versão ingênua, cada um pega o
garfo da esquerda e depois o da direita; se todos pegarem o esquerdo ao mesmo
tempo, formam um ciclo de espera e travam. A correção usa hierarquia de recursos
(pegar sempre o garfo de menor índice primeiro), quebrando a espera circular.

Parte 2 — Threads e Semáforos
Oito threads incrementam um contador compartilhado. Sem sincronização, elas mexem
no contador ao mesmo tempo e uma apaga o trabalho da outra, perdendo incrementos.
Com um semáforo binário, só uma thread por vez mexe no contador, o resultado fica
correto, mas a execução fica mais lenta por causa da serialização.

Parte 3 — Deadlock
Duas threads pegam dois locks em ordens opostas (uma A→B, outra B→A) e travam
esperando uma à outra. A correção impõe ordem global (sempre A antes de B),
quebrando a espera circular.