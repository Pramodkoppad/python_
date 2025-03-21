import random
number_to_guess=random.randint(1,100)
while True:
    try:
        guess=int(input("Guess the number: "))
        if guess < number_to_guess:
            print('Too Low')
        elif guess > number_to_guess:
            print('Too High')
        else:
            print('Congratulations! You guessed the number.')
            break
    except ValueError:
        print('Please Enter the Valid Number')