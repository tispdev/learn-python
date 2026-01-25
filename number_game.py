import random

def get_guess(attempt):
    return int(input("Attempt " + str(attempt) + ": "))

def play_round():
    number = random.randint(1, 10)

    print("\nNew round! Guess the number (1-10).")

    for attempt in range(3):
        guess = get_guess(attempt)

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Correct! You win this round!")
            return "Win"

    print("Game over! The number was", number)
    return "Lose"



print("=== GUESS MASTER ===")
print("Can you guess the number in 3 tries?")

score = []

while True:
    result = play_round()
    score.append(result)

    print("\nScore:", score)
    again = input("Play again? (yes/no): ").lower()

    if again != "yes":
        break

print("\nThanks for playing! Final score:", score)
