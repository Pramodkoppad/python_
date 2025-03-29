import random
emoji={'r':'🪨','p':'📃','s':'✂️'}
choices=('r','p','s')
while True:
    user_choice=input('Rock,Paper, or Scissor? (r/p/s): ').lower()
    if user_choice not in choices:
        print('Invaild Choice!')
        continue
    computer_choice=random.choice(choices)

    print(f'you chose {emoji[user_choice]}')
    print(f'Computer Chose {emoji[computer_choice]}')
    if user_choice==computer_choice:
        print("Tie!")
    elif (
        (user_choice=='r' and computer_choice=='p') or 
        (user_choice=='p' and computer_choice=='r') or 
        (user_choice=='s' and computer_choice=='p')):
        print("You Win")
    else:
        print("You Lose")
    should_continue = input('Continue? (y/n): ').lower()   
    if should_continue =='n':
        break