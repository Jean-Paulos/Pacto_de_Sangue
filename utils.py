from time import sleep

def datilografa(texto, delay=0.1):
    for letter in texto:
        print(letter, end='', flush=True)
        sleep(delay)
    print()