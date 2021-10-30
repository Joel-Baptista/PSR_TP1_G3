#!/usr/bin/python3
import argparse
import readchar
import random
import string

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

def withoutTime(args):
    number_of_hits = 0
    number_of_types = 0
    for i in range(args['maximum_value']):
        random_char = random.choice(string.ascii_letters)
        print('Type ' + str(random_char))
        pressed_char = readchar.readkey()
        if random_char == pressed_char:
            print('You typed ' + pressed_char + '. ' + 'Correct!')
            number_of_hits += 1
            number_of_types += 1
        else:
            print('You typed ' + pressed_char + '. ' + 'Wrong!')
            number_of_types += 1



if __name__ == '__main__':
    main()
