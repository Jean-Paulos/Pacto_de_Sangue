import pygame
from random import randint
from text import *
from utils import *

pygame.mixer.init()
ambience = pygame.mixer.Sound('ambience.wav')
jogador = input('Por favor, digite o seu nome: ')
menu()
tempo_inicio = time()
ambience_channel = ambience.play(-1)

# Inicio do Capítulo 1
datilografa (c1_text001, delay=0.02)
load_and_listen()

choices = ['Levantar-se', 'Permanecer onde está']
while True:
    ask = select(
        "Você tem algumas alternativas:",
        choices=choices)

    response = ask.ask()
    choices.remove(response) # Remoção da alternativa anterior

    if response == 'Levantar-se':
        datilografa(c1_text004, delay=0.02)
        load_and_listen()
        choices.append('Olhar em volta')
    elif response == 'Olhar em volta':
        datilografa(c1_text005, delay=0.02)
        break # Para o loop
    elif response == ('Permanecer onde está'):
        datilografa(c1_text002, delay=0.02)
        load_and_listen()
        choices.append('Prestar atenção no som')
    elif response == 'Prestar atenção no som':
        datilografa(c1_text003, delay=0.02)
        load_and_listen()

while True:
    ask = select(
    "Você tem algumas alternativas:",
    choices=["Parede", "Câmera", "Sanitario", "Cadeira", "Corda suspensa"]) # 
    response = ask.ask()

    if response == ('Sanitario'):
        datilografa(c1_text006, delay=0.02)
        load_and_listen()
    elif response == ('Câmera'):
        datilografa(c1_text007, delay=0.02)
        load_and_listen() 
    elif response == ('Parede'):
        datilografa (c1_text008, delay=0.02)
        ask = select ('Você tem algumas alternativas:',
        choices=['Bater na porta', 'Olhar em volta'])
        response = ask.ask()
        if response == 'Olhar em volta':
            print ('Você decide continuar analisando ao seu redor')
            load_and_listen()
        elif response == 'Bater na porta':
            datilografa (c1_text011, delay=0.02)
            load_and_listen()
            ask = select (
            "Você tem algumas alternativas:", 
            choices = ["Continuar batendo e gritando por ajuda"])
            response = ask.ask ()
            if response == 'Continuar batendo e gritando por ajuda':
                datilografa (c1_text012, delay=0.02)
                load_and_listen()
            ask = select (
            "Você tem algumas alternativas:", 
            choices = ["Tentar se lembrar onde estava"])
            response = ask.ask ()
            if response == 'Tentar se lembrar onde estava':
                datilografa (c1_text013, delay=0.02)
                load_and_listen()
                break # Para o loop
    elif response == ('Cadeira'):
        datilografa(c1_text009, delay=0.02)
        load_and_listen() 
    elif response == ('Corda suspensa'):
        datilografa (c1_text010, delay=0.02)
        load_and_listen()
