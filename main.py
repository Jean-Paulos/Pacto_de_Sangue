import pygame
from random import randint
from text import *
from utils import *

pygame.mixer.init()
ambience = pygame.mixer.Sound('ambience.mp3')
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
# Editado por Jonathan
datilografa(c3_text001,delay=0.02)
load_and_listen()

ask = select(
    "Você tem algumas alternativas:",
    choices=["Olhar em volta"])
response = ask.ask()
if response == 'Olhar em volta':
    datilografa(c3_text002,delay=0.02)
    load_and_listen()

ask = select(
    "Você tem algumas alternativas:",
    choices=["Ir em direção a mulher"])
response = ask.ask()
if response == 'Ir em direção a mulher':
    datilografa(c3_text003,delay=0.02)
    load_and_listen()

ask = select(
    "Você tem algumas alternativas:",
    choices=["Continuar correndo"])
response = ask.ask()
datilografa(c3_text004,delay=0.02)
load_and_listen()

ask = select(
    "Você tem algumas alternativas:",
    choices=["???"])
response = ask.ask()
if response == '???':
    datilografa(c4_text001,delay=0.02)
    load_and_listen()
ask = select(
    "Você tem algumas alternativas:",
    choices=["Olhar em volta"])
response = ask.ask()
if response == 'Olhar em volta':
    datilografa(c4_text002,delay=0.02)
    load_and_listen()

choices = ["Porta","Câmera","Sanitario","Cadeira","Diário","Corda suspensa","Parede",]
# Inicio de Loop
while True:
    ask = select(
        "Você tem algumas alternativas:",
        choices=choices)
    response = ask.ask()
    if response == 'Porta':    
        datilografa(c4_text027, delay=0.02) #Porta 4-1
        load_and_listen()      
        choices.remove("Porta") #remove texto 4-1
        choices.append("Porta ")
    elif response == "Porta ":
        datilografa(c4_text028,delay=0.02) #texto da porta 4-2
        ask = select(
            "Você tem algumas alternativas:",
            choices=["Verificar o papel","Olhar em volta"])
        response = ask.ask()
    elif response == 'Diário':
        datilografa(c4_text007, delay=0.02)
        load_and_listen()
    elif response == 'Câmera':
        datilografa(c4_text004, delay=0.02)
        load_and_listen()
    elif response == 'Sanitario':
        datilografa(c4_text005, delay=0.02) 
        load_and_listen()
        ask = select(
            "Você tem algumas alternativas:",
            choices=["Cagar"])
        response = ask.ask()
        datilografa(c4_text010,delay=0.02)
        load_and_listen()

    elif response == 'Cadeira':
        datilografa(c4_text006, delay=0.02)
        load_and_listen()

        ask = select(
            "Você tem algumas alternativas:",
            choices=["Sentar-se na cadeira:","Olhar em volta"])
        response = ask.ask()
        if response == "Olhar em volta":
            continue
        elif response == "Sentar-se na cadeira:":# texto ok
            datilografa(c4_text011,delay=0.02) 
            load_and_listen()
            
            ask = select(
            "Você tem algumas alternativas:",
            choices=["Escrever no diário","Olhar em volta"])
            response = ask.ask()
            if response == "Escrever no diário":
                datilografa(c4_text014,delay=0.02)
                c4_text007 = c4_text020 # junta o texto do diario

    if response == "Olhar em volta":
            continue
    elif response == "Escrever no diário":# texto ok
        datilografa(c4_text014,delay=0.02)
        ask = select(
            "Você tem algumas alternativas:",
            choices=["Diário"])
        response = ask.ask()
        datilografa(c4_text007,delay=0.02) 
        load_and_listen()    
    elif response == 'Corda suspensa':
        datilografa(c4_text008, delay=0.02)
        load_and_listen()
        ask = select(
            "Você tem algumas alternativas:",
            choices=["Acabar com tudo","Olhar em volta"])
        response = ask.ask()
    if response == "Olhar em volta":#ok
            continue
    elif response =="Acabar com tudo":
        datilografa(fim,delay=0.02)
        load_and_listen()
        exit()
    #Primeira opção terminar loop
    elif response == 'Parede':
        datilografa(c4_text009, delay=0.02)# Parede 4-1
        load_and_listen()
        ask = select(
            "Você tem algumas alternativas:",
            choices=["Desenhar na parede"])
        response = ask.ask()                   
        datilografa(c4_text017,delay=0.02)
        ask = select(
            "Você tem algumas alternativas:",
            choices=["Analisar parede"])
        response = ask.ask()
        datilografa(c4_text018,delay=0.02)
        load_and_listen()
        ask = select(
            "Você tem algumas alternativas:",
            choices=["Ir até a porta","Olhar em volta"])
        response = ask.ask()
        choices.remove("Parede") #remove texto 4-1
        choices.append("Parede ")# adicionar porta 4-2
    elif response == "Parede ":
        datilografa(c4_text029,delay=0.02) #texto porta 4-2      
    if response == "Olhar em volta":
        continue
    elif response =="Ir até a porta":
        datilografa(c4_text021,delay=0.02) # Porta 4-2
        load_and_listen()
        ask = select(
            "Você tem algumas alternativas:",
            choices=["Comer a comida","Olhar em volta"])
        response = ask.ask()
    if response == "Olhar em volta":
        continue        
    elif response == 'Comer a comida':
        datilografa(c4_text022, delay=0.02)
        load_and_listen()
        ask = select(
        "Você tem algumas alternativas:",
        choices=["Guardar o osso do bife", "Guardar a faca", "Terminar de comer"])
        response = ask.ask()        
    if response == "Guardar o osso do bife":
        datilografa(c4_text023, delay=0.02)
        load_and_listen()
        ask = select(
            "Você tem algumas alternativas:",
            choices=["Terminar de comer"])
        response = ask.ask()
    elif response == "Guardar a faca":
        datilografa(c4_text024, delay=0.02)
        load_and_listen()
        ask = select(
            "Você tem algumas alternativas:",
            choices=["Terminar de comer"])
        response = ask.ask()
    elif response == "Terminar de comer":
        datilografa(c4_text025, delay=0.02)
        load_and_listen()
    elif response =='Verificar o papel':
        datilografa(c4_text030,delay=0.02)
        load_and_listen()
        break

# Inicio capitulo 5
#[[Destruir bilhete]]

datilografa(c5_text001,delay=0.02)
datilografa(c5_text002,delay=0.02)
datilografa(c5_text002_1,delay=0.02)
datilografa(c5_text002_2,delay=0.02)
load_and_listen()

ask = select(
    "Você tem algumas alternativas:",
    choices= ["Olhar em volta"])
response = ask.ask()

if response == "Olhar em volta":
    datilografa(c5_text003,delay=0.02)

choices= ["Porta","Câmera","Sanitario","Cadeira","Parede","Corda suspensa","Diário",""]
while True: #Regra criada para alterar o texto e "choises" da "Cadeira c5" e "Diário c5"

    ask = select(
        "Você tem algumas alternativas:",
        choices=choices)
    
    response = ask.ask()
    #Porta c5
    if response == 'Porta':
        datilografa(c5_text004, delay=0.02)
        load_and_listen()
    #Câmera c5
    elif response == 'Câmera':
        datilografa(c5_text005, delay=0.02)
        load_and_listen()
    #Sanitario c5
    elif response == 'Sanitario':
        datilografa(c5_text006, delay=0.02)
        load_and_listen()
        ask = select(
            "Você tem algumas alternativas:",
            choices= ["Cagar","Olhar em volta"]) #Cagar c5 ou Voltar ao Menu (Olhar em volta)
        response = ask.ask()
        if response == "Cagar":
            datilografa(c5_text007, delay=0.02)
            load_and_listen()
    #Cadeira c5
    elif response == 'Cadeira':
        datilografa(c5_text008, delay=0.02)
        load_and_listen()
        ask = select(
            "Você tem algumas alternativas:",
            choices=["Sentar-se na cadeira","Olhar em volta"])
        response = ask.ask()
        #Sentar-se na cadeira c5
        if response == 'Sentar-se na cadeira':
            datilografa(c5_text009, delay=0.02)
            ask = select(
                "Você tem algumas alternativas:",
                choices=["Diário"])
            response = ask.ask()
            if response == 'Diário':
                datilografa(c5_text010,delay=0.01)
                ask = select(
                    "Você tem algumas alternativas:",
                    choices=["Escrever no diário"])
                response = ask.ask()
                choices.remove("Diário") #remove texto 4-1
                choices.append("Diário ")
                if response == 'Escrever no diário':
                    c5_text010 = c5_text024
                    datilografa(c5_text011,delay=0.02)
                    load_and_listen()
                    ask = select(
                    "Você tem algumas alternativas:",
                    choices=["Continuar escrevendo"])
                    response = ask.ask()
                    if response == 'Continuar escrevendo':
                        datilografa(c5_text012,delay=0.02)
                        datilografa(c5_text013,delay=0.02)
                        datilografa(c5_text014,delay=0.02)
                        datilografa(c5_text015,delay=0.02)
                        datilografa(c5_text016,delay=0.02)
                        load_and_listen()

                        ask = select(
                            "Você tem algumas alternativas:",
                            choices= ["Refletir"])
                        response = ask.ask()
                        if response == 'Refletir':
                            datilografa(c5_text017,delay=0.02)
                            datilografa(c5_text018,delay=0.02)
                            datilografa(c5_text019,delay=0.02)
                            datilografa(c5_text020,delay=0.02)
                            datilografa(c5_text021,delay=0.02)
                            load_and_listen()
                            choices.remove("")
                            choices.append("Por plano em prática")
        
    #Parede c5
    elif response == 'Parede':
        datilografa(c5_text022,delay=0.02)
        load_and_listen()
    #Corda suspensa c5
    elif response == 'Corda suspensa':
        datilografa(c5_text023,delay=0.02)
        load_and_listen()
    #Diário c5
    elif response == 'Diário':
        datilografa(c5_text010,delay=0.02)
        load_and_listen()
    elif response == 'Diário ':
        datilografa(c5_text024,delay=0.02)
        load_and_listen()
    elif response == '':
        print('')
    #Por plano em prática c5
    elif response == 'Por plano em prática':
        datilografa(c5_text025,delay=0.02)
        datilografa(c5_text026,delay=0.02)
        load_and_listen()
        ask = select(
            "O que você fará a seguir?",
            choices=['Aguardar o momento certo'])
        response = ask.ask()
        datilografa(c5_text028,delay=0.02)
        datilografa(c5_text029,delay=0.02)
        load_and_listen()
        ask = select(
            "O que acontecerá a seguir?",
            choices=["Atacar agora!","Esperar"])
        response = ask.ask()

        if response == 'Atacar agora!':
            datilografa(c5_text030,delay=0.02)
            datilografa(c5_text031,delay=0.02)
            datilografa(c5_text068,delay=0.02)
            load_and_listen()
            print('''Parabéns, você encontrou uma das nossas rotas exclusivas para a morte! Infelizmente, sua pontuação não será salva desta vez. Se quiser deixar sua marca no nosso ranking, talvez na próxima vez tente não morrer. Boa sorte!''')
            exit()
            #Sistema de ataque
            
        elif response == 'Esperar':
            datilografa(c5_text032,delay=0.02)
            datilografa(c5_text033,delay=0.02)
            datilografa(c5_text034,delay=0.02)
            datilografa(c5_text035,delay=0.02)
            load_and_listen()
            ask = select(
                "Pode ser a grande chance!",
                choices=["Atacar","Esperar por mais..."])
            response = ask.ask()

            if response == 'Atacar':
                datilografa(c5_text036,delay=0.02)
                datilografa(c5_text037,delay=0.02)
                datilografa(c5_text038,delay=0.02)
                load_and_listen()
                #Sistema de ataque
                ataque = randint(1, 20)#<------ Estima a regra p/ gerar um numero de "sorte" de forma aleatória p/ o persongaem com as chances do ataque de 1 a 20 ser efetivo
                if ataque in range(1, 5):#<------ Quando o numero gerado estiver entre 1 a 5 ele não será efetivo e vai cair direto no fim do jogo.
                    datilografa(c5_text030,delay=0.02)                    
                    datilografa(c5_text031,delay=0.02)                    
                    datilografa(c5_text068,delay=0.02)
                    load_and_listen()
                    datilografa(fim,delay=0.02)
                    exit() #<------ Fim do jogo
                elif ataque in range(6, 15):# <------ Gera uma nova chance de ataque.
                    datilografa(c5_text039,delay=0.02)
                    load_and_listen()
                    ataque = randint(1, 20)# <------ Cria a regra para a "sorte" ser gerada entre 5 a 20 de forma aleatória
                    if ataque in range(1, 3):# <------ Se o numero gerado estiver entre 5 a 15 o jogo se encerra.
                        datilografa(c5_text031,delay=0.02)
                        datilografa(c5_text068,delay=0.02)
                        load_and_listen()
                        datilografa(fim,delay=0.02)
                        exit()
                    elif ataque in range(4, 20):# <------ Se estiver entre 16 a 20 o numero gerado fim do ataque de forma efetiva e a história continua
                        datilografa(c5_text069,delay=0.02)
                        datilografa(c5_text070,delay=0.02)
                        datilografa(c5_text071,delay=0.02)
                        datilografa(c5_text072,delay=0.02)
                        datilografa(c5_text073,delay=0.02)
                        load_and_listen()
                        datilografa(c5_text074,delay=0.02)
                        datilografa(c5_text075,delay=0.02)
                        datilografa(c5_text050,delay=0.02)
                        datilografa(c5_text051,delay=0.02)
                        load_and_listen()
                        datilografa(c5_text052,delay=0.02)
                        datilografa(c5_text053,delay=0.02)
                        datilografa(c5_text065,delay=0.02)
                        datilografa(c5_text066,delay=0.02)
                        datilografa(c5_text067,delay=0.02)
                        load_and_listen()
                        datilografa(fim,delay=0.02)
                        exit()
                
                elif ataque in range(16, 20):# <------ Se estiver entre 16 a 20 o numero gerado fim do ataque de forma efetiva e a história continua
                    datilografa(c5_text069,delay=0.02)
                    datilografa(c5_text070,delay=0.02)
                    datilografa(c5_text071,delay=0.02)
                    datilografa(c5_text072,delay=0.02)
                    datilografa(c5_text073,delay=0.02)
                    load_and_listen()
                    datilografa(c5_text074,delay=0.02)
                    datilografa(c5_text075,delay=0.02)
                    datilografa(c5_text050,delay=0.02)
                    datilografa(c5_text051,delay=0.02)
                    datilografa(c5_text052,delay=0.02)
                    load_and_listen()
                    datilografa(c5_text053,delay=0.02)
                    datilografa(c5_text065,delay=0.02)
                    datilografa(c5_text066,delay=0.02)
                    datilografa(c5_text067,delay=0.02)
                    load_and_listen()
                    datilografa(fim,delay=0.02)
                    exit()

            elif response == 'Esperar por mais...':
                datilografa(c5_text040,delay=0.02)
                datilografa(c5_text041,delay=0.02)
                load_and_listen()
                ask = select(
                    "Faça valer a pena.",
                    choices=["Atacar!"])
                response = ask.ask()
                datilografa(c5_text042,delay=0.02)
                datilografa(c5_text043,delay=0.02)
                datilografa(c5_text044,delay=0.02)
                datilografa(c5_text045,delay=0.02)
                load_and_listen()
                datilografa(c5_text046,delay=0.02)
                datilografa(c5_text047,delay=0.02)
                datilografa(c5_text048,delay=0.02)
                datilografa(c5_text049,delay=0.02)
                load_and_listen()

        datilografa(c5_text054,delay=0.02)
        load_and_listen()
        datilografa(c5_text055,delay=0.02)
        load_and_listen()
        datilografa(c5_text056,delay=0.02)
        load_and_listen()
        datilografa(c5_text057,delay=0.02)
        load_and_listen()
        datilografa(c5_text058,delay=0.02)
        load_and_listen()
        datilografa(c5_text059,delay=0.02)
        load_and_listen()
        datilografa(c5_text060,delay=0.02)
        load_and_listen()
        datilografa(c5_text061,delay=0.02)
        load_and_listen()
        datilografa(c5_text062,delay=0.02)
        load_and_listen()
        datilografa(c5_text063,delay=0.02)
        load_and_listen()
        datilografa(c5_text064,delay=0.02)
        load_and_listen()
        tempo_fim = time() 
        tempo_decorrido = tempo_fim - tempo_inicio
        tempo_legivel = str(timedelta(seconds=tempo_decorrido))
        tempo_formatado = tempo_legivel.split('.')[0]

        dados = {
        "Jogador": jogador,
        "Tempo": tempo_formatado
        }

        placar = "placar.json" 

        try:
            with open(placar, "r") as arquivo_json:
                dados_antigos = json.load(arquivo_json)
        except FileNotFoundError:
            dados_antigos = []
        dados_antigos.append(dados)
        with open(placar, "w") as arquivo_json:
            json.dump(dados_antigos, arquivo_json)

        if response == 'A corda':
            datilografa(c5_text065,delay=0.02)
            datilografa(c5_text066,delay=0.02)
            datilografa(c5_text067,delay=0.02)
            load_and_listen()
            fim2 = fim2.format(tempo_formatado)
            datilografa(fim2, delay=0.02)
            exit()

