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

# Editado por Jean

datilografa(c1_text001, delay=0.02)
input(' ➤ ')
datilografa(c1_text002, delay=0.02)

ask = select(
    "Você tem algumas alternativas:",
    choices=["Levantar-se", "Ficar deitado"])

response = ask.ask()

if response == 'Levantar-se':    
    datilografa(c1_text003, delay=0.02)

elif response == 'Ficar deitado':
    datilografa(c1_text004, delay=0.02)

    ask = select(
    "Você tem algumas alternativas:",
    choices=["Levantar-se", "Ouvir atentamente"])

    response = ask.ask()

    if response == 'Levantar-se':
        datilografa(c1_text003, delay=0.02)

    elif response == 'Ouvir atentamente':
        datilografa(c1_text005, delay=0.02)

        ask = select(
        "Você tem algumas alternativas:",
        choices=["Levantar-se"])

        response = ask.ask()

    if response == 'Levantar-se':
        datilografa(c1_text003, delay=0.02)

# FIM editado por Jean
