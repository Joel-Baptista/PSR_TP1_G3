#!/usr/bin/python3
import argparse

def main():
    parser = argparse.ArgumentParser(description='Escolha do modo de jogo.')
    parser.add_argument('-utm', '--use_time_mode', action='store_true', help='')
    parser.add_argument('-mv', '--maximum_value', type=int, required=True, help='')
    args = vars(parser.parse_args())

    #print(args)

    if args['use_time_mode'] is False:
        print('Type all ' + str(args['maximum_value']) + ' characters to finish the test.')
    else:
        print('You have ' + str(args['maximum_value']) + ' seconds to finish the test.')

if __name__ == '__main__':
    main()