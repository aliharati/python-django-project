import random

def take_input():
    guess = input("what is your guess?")
    while len(guess)!=3 or not guess.isnumeric():
        print("only 3 digit numeric values are accepted")
        guess = input("what is your guess?")
    return guess

def start_game():
    print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")
    win= False
    digit = generate_digit()
    print("Code has been generated, please guess a 3 digit number")
    # print(digit)
    while not win:

        guess = take_input()
        win = evaluate_guess(digit, guess)
    
    

def generate_digit():
    d1 = random.randint(0,9)
    d2 = random.randint(0,9)
    while d2 == d1:
        d2 = random.randint(0,9)
    d3 = random.randint(0,9)
    while d3 == d2 or d3==d1:
        d3 = random.randint(0,9)
    
    return str(d1) + str(d2) + str(d3)
    

def evaluate_guess(digit1, digit2):
    if digit1 == digit2:
        print("Correct you Win")
        return True
    clues = []
    for ind,num in enumerate(digit2):
        if num == digit1[ind]:
            clues.append("Match")
        elif num in digit1:
            clues.append("Close")
    if clues == []:
        print("Nope")
        return False
    print(clues)
    return False        
start_game()