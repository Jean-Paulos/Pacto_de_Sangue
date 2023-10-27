import pandas as pd
import json
from questionary import select
from time import sleep, time
from datetime import timedelta

def datilografa(texto, delay=0.1):
    for letter in texto:
        print(letter, end='', flush=True)
        sleep(delay)
    print()

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
