# KEILOGGER-Fume-Knight
O que torna Fume Knight um dos chefes mais desafiadores do jogo é seu grande conjunto de movimentos e as difíceis dicas para suas animações e padrões de ataque. Podemos comparar com esse keylogger que tem padroes a mais.

Segue a explicaçao do codigo:


Esse código em Python usa uma biblioteca pynputpara capturar e registrar as teclas digitadas pelo usuário. Vamos explicar parte por parte:

Importações :

from pynput.keyboard import Listener, Key: Importar o Listener(para escutar as teclas pressionadas) e Key(para identificar teclas especiais, como "Esc").
import sys: Importa o módulo syspara encerrar o programa ( sys.exit()).
import random: Importe uma biblioteca randompara gerar números aleatórios.
Funções :

encerrar_progranma(): Esta função imprime "Programa encerrado!" e usa sys.exit()para fechar o programa.

escreve_key(key): Função chamada sempre que uma tecla é pressionada. Ela tenta:

Abra um arquivo de log com nome gerado aleatoriamente.
Escrever uma tecla pressionada no arquivo de log.
Se houver qualquer exceção ao capturar ou gravar uma tecla, ela imprimirá uma mensagem de erro e encerrará o programa.
Se a tecla "Esc" for pressionada, o programa é encerrado.
Variávellog :

log = f'yek{random.randint(0,1000)}.txt': Gera um nome de arquivo aleatório para armazenar as teclas digitadas, usando o prefixo yekseguido de um número aleatório entre 0 e 1000.
Ouvinte :

O programa inicia a captura das teclas com o Listener, chamando a função escreve_keysempre que uma tecla for pressionada.
logs.join()é usado para manter o Listenerem execução até que ocorra um erro ou o programa seja encerrado.
Se houver algum erro durante a execução do Listener, uma mensagem de erro será exibida e o programa será finalizado.
Resumo : O código é um keylogger simples que registra todas as teclas pressionadas em um arquivo de log. Ele é finalizado automaticamente quando a tecla "Esc" é pressionada ou ocorre algum erro.
