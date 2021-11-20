#!/usr/bin/python3
import argparse
import readchar
import random
import string
from time import time, ctime, sleep
from collections import namedtuple
from colorama import Fore, Back, Style
from pprint import pprint


def main():
#Criação de um conjunto de argmentos que viabiliza ao utilizador selecionar o modo de jogo que pretende.

    parser = argparse.ArgumentParser(description='Choose game mode.')
    parser.add_argument('-utm', '--use_time_mode', action='store_true', help='Max number of secs for time mode or maximum number of inputs for number of inputs mode')
    #O utilizador deverá inserir '-utm' caso queira o modo de jogo com cronometro. Se não for chamado, o valor deste argumento será False.
    parser.add_argument('-mv', '--maximum_value', type=int, required=True, help='Max number of seconds for time mode or maximum number of inputs for number of inputs mode.')
    #O utilizador deverá inserir '-mv' de modo a inserir um argumento que especifique o numero máximo, sendo este de presença obrigatória.
    args = vars(parser.parse_args())

    if args['use_time_mode'] is False:
        print('Type all ' + str(args['maximum_value']) + ' characters to finish the test.')
        my_dict = withoutTime(args)
        #Caso o argumento -utm nao seja chamado pelo utlizador o modo selecionado é o sem cronometro

    else:
        print('You have ' + str(args['maximum_value']) + ' seconds to finish the test.')
        my_dict = withTime(args)
        #Caso o argumento -utm seja chamado, juntamente com o valor max_value, então o modo selecionado é com cronometro

    pprint(my_dict)


def start():
    print('Press a key to start the test')
    readchar.readkey()


def leave():
# Caso o utlizador não pressione nenhuma tecla, é mostrada uma mensagem a dizer que o jogador desistiu e o programa pára.
    print('The player quit the game. Statistics will not be shown!')
    exit()


def withoutTime(args):
#Inicialização das variaveis e do dicionário com as estatisticas do jogo

    Input = namedtuple('Input', ['requested', 'received', 'duration'])
    inputs = []
    start()
    test_start = ctime()
    time_c = 0
    time_w = 0
    number_of_hits = 0
    number_of_types = 0
    number_of_misses = 0
    
#Ciclo For, que vai de 1 até ao "Max_value" inserido pelo utilizador.
    #Em primeiro lugar, é Gerada uma letra aleatoria através da função random.randint, que retorna um valor inteiro de 97 a 122. Esse mesmo valor será posteriormente convertido à sua letra equivalente na tabela ASCII através da função chr.
    #De seguida, é verificado a condição para averiguar se o jogador pressionou a tecla certa ou não.
    #Por fim, são calculados todos os outros dados estatisticos que farão parte do dicionário apresentado no final.
    
    for i in range(args['maximum_value']):
        random_char = chr(random.randint(97, 122))
        print(Fore.CYAN + '\nType ' + str(random_char) + Style.RESET_ALL)
        duration = time()
        pressed_char = readchar.readkey()
        duration = time() - duration
        
        if random_char == pressed_char:
            print('\nYou typed ' + Fore.GREEN + pressed_char + Style.RESET_ALL + '. ' + 'Correct!')
            number_of_hits += 1
            number_of_types += 1
            time_c += duration
            #sumatório do tempo que o utlizador demorou a responder corretamente a todas as perguntas.
        elif pressed_char == ' ':
            leave()
        else:
            print('\nYou typed ' + Fore.RED + pressed_char + Style.RESET_ALL + '. ' + 'Wrong!')
            number_of_misses += 1
            number_of_types += 1
            time_w += duration

        inputs.append(Input(random_char, pressed_char, duration))
        #Atualização progressiva da lista

#Calculo de outros parametros a serem mostrados ao utlizador posteriormente.
    accuracy = (float(number_of_hits) / float(number_of_types)) * 100

    test_duration = time_c + time_w

    type_average_duration = test_duration / number_of_types

    if number_of_hits == 0:
        type_hit_average_duration = None
    else:
        type_hit_average_duration = time_c / number_of_hits
    if number_of_misses == 0:
        type_miss_average_duration = None
    else:
        type_miss_average_duration = time_w / number_of_misses

    test_end = ctime()

    print('\n {} Your test has ended, here are the results: {}'.format(Fore.CYAN, Style.RESET_ALL))
    
#Criação do dicionário com as estatisticas
    my_dict = {'accuracy in %': accuracy,
                'inputs': inputs,
                'number of hits': number_of_hits,
                'number_of_types': number_of_types,
                'test duration': test_duration,
                'test_end': test_end,
                'test_start': test_start,
                'type_average_duration': type_average_duration,
                'type_hit_average_duration': type_hit_average_duration,
                'type_miss_average_duration': type_miss_average_duration}

    return my_dict
    #return do dicionário criado para a função main


def withTime(args):
    Input = namedtuple('Input', ['requested', 'received', 'duration'])
    inputs = []
    start()
    test_start = time()
    time_c = 0
    time_w = 0
    number_of_hits = 0
    number_of_types = 0
    number_of_misses = 0
    
#Ciclo While. Este corre até ao momento em que o tempo atual seja superior ao tempo de inicio do jogo mais o tempo maximo(time() >= test_start + args['maximum_value'])
#Por outras palavras, o utilizador "informa" o programa que o tempo máximo de jogo é 5,por exemplo. Após 5 segundos o jogo acaba.
    #Em primeiro lugar, é Gerada uma letra aleatoria através da função random.randint, que retorna um valor inteiro de 97 a 122. Esse mesmo valor será posteriormente convertido à sua letra equivalente na tabela ASCII através da função chr.
    #De seguida, é verificado a condição para averiguar se o jogador pressionou a tecla certa ou não.
    #Por fim, são calculados todos os outros dados estatisticos que farão parte do dicionário apresentado no final.
    
    while True:
        random_char = chr(random.randint(97, 122))
        print(Fore.CYAN + '\nType ' + str(random_char) + Style.RESET_ALL)
        duration = time()
        pressed_char = readchar.readkey()
        duration = time() - duration
        if time() >= test_start + args['maximum_value']:
            time_w += duration
            break
        if random_char == pressed_char:
            print('\nYou typed ' + Fore.GREEN + pressed_char + Style.RESET_ALL + '. ' + 'Correct!')
            number_of_hits += 1
            number_of_types += 1
            time_c += duration
        elif pressed_char == ' ':
            leave()
        else:
            print('\nYou typed ' + Fore.RED + pressed_char + Style.RESET_ALL + '. ' + 'Wrong!')
            number_of_misses += 1
            number_of_types += 1
            time_w += duration

        inputs.append(Input(random_char, pressed_char, duration))

    test_duration = time_w + time_c
    print('\nCurrent test duration {} exceeds maximum of {} seconds'.format(test_duration, args['maximum_value']))

    accuracy = (float(number_of_hits) / float(number_of_types)) * 100

    type_average_duration = test_duration / number_of_types

    if number_of_hits == 0:
        type_hit_average_duration = None
    else:
        type_hit_average_duration = time_c / number_of_hits
    if number_of_misses == 0:
        type_miss_average_duration = None
    else:
        type_miss_average_duration = time_w / number_of_misses

    test_end = ctime()
    test_start = ctime(test_start)

    print('\n {} Your test has ended, here are the results: {} '.format(Fore.CYAN, Style.RESET_ALL))

    my_dict = {'accuracy in %': accuracy,
               'inputs': inputs,
               'number of hits': number_of_hits,
               'number_of_types': number_of_types,
               'test duration': test_duration,
               'test_end': test_end,
               'test_start': test_start,
               'type_average_duration': type_average_duration,
               'type_hit_average_duration': type_hit_average_duration,
               'type_miss_average_duration': type_miss_average_duration}

    return my_dict


if __name__ == '__main__':
    main()
