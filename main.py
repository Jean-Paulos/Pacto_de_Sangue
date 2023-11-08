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

#Texto inicial do segundo capítulo
datilografa(c2_text000, delay=0.02)
load_and_listen()

#Aparece a opção para Analisar a comida
ask=select(
    "Selecione a opção: ",
    choices=["Analisar a comida"])
response = ask.ask()
if response == 'Analisar a comida':
    datilografa(c2_text001, delay=0.02)
load_and_listen()

# Loop para ter que selecionar a opção Comer a comida para que passe para que passe para o próximo texto
choices = ['Comer a comida', 'Pensar melhor']
while True:
    ask = select(
    "Selecione uma alternativa: ",
    choices=choices)
    response = ask.ask()
    choices.remove(response)
    if response == 'Comer a comida':
        datilografa(c2_text003, delay=0.02)
        load_and_listen()
        break
    elif response == 'Pensar melhor':
        datilografa(c2_text002, delay=0.02)
        load_and_listen()

ask=select(
    "Guarde um item",
    choices=["Guardar a faca", "Guardar o osso do bife"])
response = ask.ask()
if response == 'Guardar a faca':
    arma = 'uma faca'
    c2_text004 = c2_text004.format(arma, arma, arma)
    datilografa(c2_text004, delay=0.02)
    load_and_listen()
elif response == 'Guardar o osso do bife':
    arma = 'um osso'
    c2_text004 = c2_text004.format(arma, arma, arma)
    datilografa(c2_text004, delay=0.02)
    load_and_listen()

ask=select(
    "Você tem algumas alternativas:",
    choices=["Terminar de comer"])
response = ask.ask()
if response == 'Terminar de comer':
    datilografa(c2_text005, delay=0.02)
    load_and_listen()

ask=select(
    "Você tem algumas alternativas:",
    choices=["Analisar o caderno"])
response = ask.ask()
if response == 'Analisar o caderno':
    datilografa(c2_text006, delay=0.02)
    load_and_listen()

ask=select(
    "Você tem algumas alternativas:",
    choices=["Ler o diário"])
response = ask.ask()
if response == 'Ler o diário':
    datilografa(c2_text007, delay=0.02)
    load_and_listen()

ask=select(
    "Você tem algumas alternativas:",
    choices=["Virar a página"])
response = ask.ask()
if response == 'Virar a página':
    datilografa(c2_text008, delay=0.02)
    load_and_listen()

ask=select(
    "Você tem algumas alternativas:",
    choices=["Virar a página"])
response = ask.ask()
if response == 'Virar a página':
    datilografa(c2_text009, delay=0.02)
    load_and_listen()

ask=select(
    "Você tem algumas alternativas:",
    choices=["Escrever no diário"])
response = ask.ask()
if response == 'Escrever no diário':
    datilografa(c2_text010, delay=0.02)
    load_and_listen()

ask=select(
    "Você tem algumas alternativas:",
    choices=["Continue"])
response = ask.ask()
if response == 'Continue':
    datilografa(c2_text011, delay=0.02)
    load_and_listen()

ask=select(
    "Selecione uma opção:",
    choices= ["Tentar se controlar!", "Ir até a corda"])
response = ask.ask()

# Caso escolha a opção "Tentar se controlar!" segue para um caminho e se escolher a opção "Ir até a corda" segue para outro.
if response == 'Tentar se controlar!':
    datilografa(c2_text012, delay=0.02)
    ask = select(
    "Você tem algumas algumas alternativas:",
    choices=["Esconder objetos"])
    response = ask.ask()
    c2_text015 = c2_text015.format(arma)
    datilografa(c2_text015, delay=0.02)

#Aqui está a outra opção.
elif response == 'Ir até a corda':
    datilografa(c2_text013, delay=0.02)
    ask = select(
    "Selecione a alternativa: ",
    choices=["..."])
    response = ask.ask()
    datilografa(c2_text014, delay=0.02)
