import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!")
random3 = random.randint(1, 20)
attempts = 0
best_score = None
while True:
        random1 = int(input("Take a guess: "))
        attempts += 1

        if  random1 < random3:
            print("Your guess is too low.")
        elif  random1 > random3:
            print("Your guess is too high.")
        else:
            print(f"Good job! You guessed my number in {attempts} guesses.")
            if best_score is None or attempts < best_score:
                best_score = attempts
                print(f"New best score: {best_score} guesses!")
            break

guess_the_number()