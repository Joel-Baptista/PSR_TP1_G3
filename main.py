#!/usr/bin/python3
import argparse
import readchar
import random
import string
from time import time, ctime

def main():

    parser = argparse.ArgumentParser(description='Escolha do modo de jogo.')
    parser.add_argument('-utm', '--use_time_mode', action='store_true', help='')
    parser.add_argument('-mv', '--maximum_value', type=int, required=True, help='')
    args = vars(parser.parse_args())

    #print(args)

    if args['use_time_mode'] is False:
        print('Type all ' + str(args['maximum_value']) + ' characters to finish the test.')
        withoutTime(args)

    else:
        print('You have ' + str(args['maximum_value']) + ' seconds to finish the test.')
        withTime(args)


def start():
    print('Press a key to start the test')
    readchar.readkey()

def withoutTime(args):
    start()
    test_duration = time()
    test_start = ctime()
    time_c = 0
    time_w = 0
    number_of_hits = 0
    number_of_types = 0
    number_of_misses = 0
    for i in range(args['maximum_value']):
        random_char = random.choice(string.ascii_letters)
        print('Type ' + str(random_char))
        duration = time()
        pressed_char = readchar.readkey()
        duration = time() - duration
        if random_char == pressed_char:
            print('You typed ' + pressed_char + '. ' + 'Correct!')
            number_of_hits += 1
            number_of_types += 1
            time_c += duration
        elif pressed_char == ' ':
            print('Thanks for playing!')
            test_duration = time() - test_duration
            break
        else:
            print('You typed ' + pressed_char + '. ' + 'Wrong!')
            number_of_misses += 1
            number_of_types += 1
            time_w += duration


    accuracy = (number_of_hits / number_of_types) * 100
    type_average_duration = duration / number_of_types

    if number_of_hits == 0:
        type_hit_average_duration = None
    else:
        type_hit_average_duration = time_c / number_of_hits
    if number_of_misses == 0:
        type_miss_average_duration = None
    else:
        type_miss_average_duration = time_w / number_of_misses
    test_end = ctime()
    test_duration = time() - test_duration

if __name__ == '__main__':
    main()
