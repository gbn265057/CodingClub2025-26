import json
import random
import string
from dataclasses import dataclass

with open("words.json", "r") as words_file:
    words = json.load(words_file)

GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[0m'

@dataclass
class Result:
    won: bool
    guesses_used: int

def play_game() -> Result:
    word = random.choice(words)

    guesses_used = 0
    while (guesses_used < 6):
        guesses_used += 1
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
            if colors[i] == 0: #if grey
                print(guess[i], end = ' ')
            elif colors[i] == 1: #if yellow
                print(f'{YELLOW}{guess[i].upper()}{RESET}', end = ' ')
            else: #if green
                print(f'{GREEN}{guess[i].upper()}{RESET}', end = ' ')
        print()

        if guess == word:
            print('Good job!')
            return Result(True, guesses_used)
    
    print('Nice try. The word was', word + '.')
    return Result(False, 6)

if __name__ == "__main__":
    play_game()

__all__ = ["play_game", "Result"]
