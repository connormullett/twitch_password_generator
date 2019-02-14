#!/usr/bin/python3

import sys
from generator import PasswordMaker


'''This module will be the ui to create passwords'''

def main(strength):
    pw = PasswordMaker(strength)
    password = pw()  # use the __call__ method

    print(password)

    should_save = input('Do you want to save the password? (y/n)\n')

    if should_save == 'y':
        website = input('What website does it go to: ')
        pw.save_password(website, password)
    else:
        exit(0)


if __name__ == '__main__':
    strength = sys.argv[1]
    if len(sys.argv) < 2:
        print('give a strength | easy, medium, or hard')
        exit(0)
    main(strength)

