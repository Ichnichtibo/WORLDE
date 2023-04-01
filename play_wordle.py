from wordle import Wordle
from colorama import Fore
from letter_state import LetterState
import random

def main():

    word_set = load_word_set("wordle_words.txt")
    word = random.choice(list(word_set))

    wordle = Wordle(word)
    
    while wordle.can_attempt:
        x = input("\nType your guess : ")

        if len(x) != wordle.WORD_LENGHT:
            print(Fore.RED +f"Word must be {wordle.WORD_LENGHT} character long" + Fore.RESET)
            continue


        wordle.attempt(x)
        result = wordle.guess(x)
        display_Results(wordle)

       
    if wordle.is_Solved:
        print("You Won!!")
    else:
        print("You Are LOSE!!")
        print(f"Secret word is {wordle.secret}")

def display_Results(wordle: Wordle):
    print("\nYour results so far")
    print(f"\nYou have {wordle.remaining_attemps} attempt remaining.\n")

    lines = []

    for word in wordle.attemps:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        lines.append(colored_result_str)
    
    

    for _ in range(wordle.remaining_attemps):
        lines.append(" ".join(["_"] * wordle.WORD_LENGHT))

    draw_border_around(lines)

def convert_result_to_color(result: list[LetterState]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        colored_letter = color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)

    return " ".join(result_with_color)

def draw_border_around(lines: list[str], size: int= 9, pad: int=1):
    content_length = size + pad *2 
    top_border = "┌" + "─" * content_length + "┐"
    bottom_border = "└" + "─" * content_length + "┘"
    space = " " * pad 
    print(top_border)
    for line in lines:
        print("│" + space + line + space+"│")

    print(bottom_border)

def load_word_set(path: str):
    word_set = set()
    with open(path,"r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)

    return word_set

if __name__ == "__main__":
    main()