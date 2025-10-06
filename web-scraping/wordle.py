import requests
from bs4 import BeautifulSoup
import random
import string

url = 'https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words_alpha.txt'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

all_words = soup.text.split()
words = []
for word in all_words:
    if len(word) == 5:
        words.append(word)
word = random.choice(words)


GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[0m'
guesses = 6
while (guesses > 0):
    guesses -= 1
    guess = input('Enter a 5 letter word: ')
    while (guess not in words):
        guess = input('Try again: ')
    
    colors = [0] * 5
    seen = {}
    
    for l in string.ascii_lowercase:
        seen[l] = 0
    
    for i in range(5):
        if (guess[i] == word[i]):
            colors[i] = 2 #green
            seen[guess[i]] += 1
        elif guess[i] in word and seen[guess[i]] < word.count(guess[i]):
            colors[i] = 1 #yellow
            seen[guess[i]] += 1

    for i in range(5):
        if colors[i] == 0:#if grey
            print(guess[i], end = ' ')
        elif colors[i] == 1:#if yellow
            print(f'{YELLOW}{guess[i].upper()}{RESET}', end = ' ')
        else: #if green
            print(f'{GREEN}{guess[i]}{RESET}', end = ' ')
    print()

    if guess == word:
        print('Good job!')
        guesses = 0
    elif guesses == 0:
        print('Nice try. The word was', word + '.')
