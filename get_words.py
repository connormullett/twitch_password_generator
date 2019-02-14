#!/usr/bin/python3

import requests

response = requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt')

f = open('words.txt', 'w')
# f.writelines(response.text)
for word in response.text.split('\n'):
    if len(word) == 5:
        f.write(f'{word}\n')
f.close()

