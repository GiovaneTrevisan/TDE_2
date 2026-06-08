Resultados (3 execuções de cada)

Versão	            Esperado	Obtido	    Tempo (s)
Sem sincronização	1.600.000	237.149	    1,1956
Sem sincronização	1.600.000	233.545	    1,1584
Sem sincronização	1.600.000	242.024	    1,2507
Com semáforo	    1.600.000	1.600.000	22,4188
Com semáforo	    1.600.000	1.600.000	19,7420
Com semáforo	    1.600.000	1.600.000	26,1388

Resumo: 
sem trava → errado e rápido (85% perdidos, 1,2 s); 
com trava → correto e lento (23 s). 

Discussão:
Sem sync perde incrementos pois as threads mexem no contador ao mesmo tempo sem ordem, como somar 1 é "ler, somar e escrever", duas threads leem o mesmo número e uma apaga trabalho da outra.

Com semáforo dá certo pois o semáforo deixa só uma thread por vez mexer no contador. As outras esperam a vez. Assim ninguém atropela ninguém e nenhum incremento se perde, o resultado é sempre 1.600.000.

Ficou mais lento pois como agora as threads fazem fila e esperam a vez, elas param de trabalhar em paralelo nessa parte. Fica certo, mas demora mais.

Visibilidade/ordenação: no Python, o GIL deixa só uma thread rodar por vez, o que funciona como uma "barreira" que mantém a memória organizada entre elas.
Para a corrida ficar visível, cada operação faz um pequeno trabalho extra (alargando a janela entre ler e escrever) usando o  sys.setswitchinterval(1e-5).