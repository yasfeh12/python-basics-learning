secret_word = "glasses"
guess = ""
guess_count = 0
guess_limit = 3

while guess != secret_word and guess_count < guess_limit:
    guess = input("Enter your guess: ")
    guess_count += 1
    remaining_guesses = guess_limit - guess_count

    if guess == secret_word:
        print("Good guess! You win!")
        break
    elif remaining_guesses > 0:
        print(f"Incorrect. You have {remaining_guesses} guesses remaining.")
    else:
        print("Incorrect. No guesses remaining.")

if guess != secret_word:
    print("Game over. Better luck next time!")
