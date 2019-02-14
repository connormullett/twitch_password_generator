
import random

'''
This module will create random passwords at user command
'''

# make random passwords that vary in 'strength'
# python3 generator.py weak/medium/strong
# easy password - rand_word + 1-5 random digits

# most passwords can only be 8 to 16 characters

class PasswordMaker:

    def __init__(self, strength: str):
        '''strength is the password's strength'''
        # if strength is easy, medium, or hard, execute the right method
        self.strength = strength
        self.strength_mapper = {
                    'easy': self.create_easy_password,
                    'medium': self.create_medium_password
                }

    def __call__(self):
        '''when object is called, route to correct method based on strength'''
        run = self.strength_mapper[self.strength]
        password = run()
        return password

    def create_easy_password(self):
        '''returns an easy password'''
        word = self.get_word()  # get word from get_word()
        # add a random number of random digits
        for i in range(random.randint(3, 5)):  # use a random range between 1 and 5
            x = random.randint(0, 9)  # get a random integer to append on the next line
            word += str(x)  # add the str version of the number to the random word
        return word  # give the password back to the thing that called the method

    def create_medium_password(self):
        '''a medium is a password that has 2 words and 5 digits at the end'''
        words = [self.get_word() for a in range(2)]  # words is a list now
        # line 21 is called 'list comprehension', google it if you want
        digits = ''
        for i in range(random.randint(0, 6)):  # create random digits to smush to word
            x = random.randint(0, 9)
            digits += str(x)
        words.append(digits)  # words now has the numbers, all we need is to smush em together
        password = ''
        for word in words:
            password += word
        return password

    def create_hard_password(self):
        pass

    def get_word(self):
        '''get a random word from the txt file'''
        with open('words.txt', 'r') as f:  # opens file for reading ONLY ('r')
            # with is a CONTEXT manager, google it
            word = random.choice(f.readlines()).rstrip()  # get random word from file
            return word  # give back the word

    def save_password(self, website, password):
        '''this method will write the website and the password to a file'''
        try:
            with open('passwords.txt', 'a') as f:
                f.writelines(f'\n{website},{password}\n')
        except FileNotFoundError:
            with open('password.txt', 'w') as f:
                f.writelines(f'\n{website},{password}\n')

