import pandas as pd
import json
from questionary import select
from time import sleep, time # time é usado no arquivo main.py
from datetime import timedelta
from sys import stdout
from threading import Thread

def load():
    for i in range(4):
            stdout.write("   ",)
            x = i % 4
            stdout.write('\r' + "." * x)
            sleep(0.5)
            stdout.flush()

def load_and_listen():
    thread_de_carregamento = Thread(target=load)

    try:
        thread_de_carregamento.start()
        input()
    finally:
        thread_de_carregamento.join()

def menu():
    print('Bem-vindo ao jogo "O Pacto de Sangue"')
    while True:
        ask = select(
            "Você tem algumas alternativas:",
            choices=["Jogar", "Pontuação", "Sair"])
        response = ask.ask()
        if response == 'Jogar':
            break
        elif response == 'Pontuação':
            tempo_media()
            placar()
        elif response == 'Sair':
            exit()
            
def datilografa(texto, delay=0.1):
    for letter in texto:
        print(letter, end='', flush=True)
        sleep(delay)
    print()

def tempo_para_segundos(tempo):
    h, m, s = map(int, tempo.split(':'))
    return h * 3600 + m * 60 + s

def tempo_media():
    placar = "placar.json"

    try:
        with open(placar, "r") as arquivo_json:
            dados_antigos = json.load(arquivo_json)
    except FileNotFoundError:
        dados_antigos = []

    df = pd.DataFrame(dados_antigos)

    df['tempo_decorrido_segundos'] = df['Tempo'].apply(tempo_para_segundos)

    tempo_medio = df['tempo_decorrido_segundos'].mean()

    tempo_medio_formatado = str(timedelta(seconds=int(tempo_medio)))

    print(f"Tempo médio dos jogadores: {tempo_medio_formatado}")
    
def placar():
    placar = "placar.json"

    try:
        with open(placar, "r") as arquivo_json:
            dados_antigos = json.load(arquivo_json)
    except FileNotFoundError:
        dados_antigos = []

    df = pd.DataFrame(dados_antigos)

    df = df.sort_values(by=["Tempo"])

    df = df.reset_index(drop=True)
    df.index +=1

    print(df.to_string(index=True))
