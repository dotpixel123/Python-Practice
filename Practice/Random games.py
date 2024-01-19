# # Creating a perfect square
# n = int(input('Enter your number here '))
# def times(n) :
#     return (n*(" ____" ))
# def times_column (n):
#     return ((n+1)*("|" + "    "))
# def times_row (n):
#     return (n)*("|____|\b")
# def times_print(a):
#     for i in range (1,n+1):
#         print (a)
# print(times(n))
# times_print(times_column(n)+"\n"+ times_row(n))

# # Creating a grid
# a = int(input('No of rows: '))
# b = int(input('No of columns: '))
# def grid(a,b):
#     for i in range(1):
#         print(b*' __')
#     for i in range(a):
#         print(b *"|__|\b")
#     print('')
# grid(a,b)

# # Calculator
# result = 0
# a = float(input('Enter value here:\n'))
# def calculator(a):
#     a = float(a)
#     import math
#     oper = input('Enter the operator here:\n')
#     basic_oper = ['+','-','*','/','^']
#     trig_oper = ['sin','cos','tan']
#     more_oper = ['!','log']
#     if oper in basic_oper:
#         b = float(input('Enter you second number here:\n'))
#         if oper == '+':
#             result = a+b
#             print(result)
#         elif oper == '-':
#             result = a-b
#             print(result)
#         elif oper == '*':
#             result = a*b
#             print(result)
#         elif oper == '/':
#             result = a/b
#             print(result)
#         else:
#             result = a**b
#             print(result)
#     elif oper in trig_oper:
#         b = a*math.pi/180
#         if oper == 'sin':
#             result = math.sin(b)
#             print(result)
#         if oper == 'cos':
#             result = math.cos(b)
#             print(result)
#         if oper == 'tan':
#             result = math.tan(b)
#             print(result)
#     elif oper in more_oper:
#         if oper == '!':
#             result = 1
#             for i in range(1,int(a+1)):
#                 result = result*i
#             print(result)
#         if oper == 'log':
#             print(math.log(a))
#     elif oper == 'AC':
#         exit()
#     else:
#         print('Select a proper operator!')
#     calculator(result)
# calculator(a)

# # Guess a random number
# import random
# t = random.randrange(1000)
# for i in range(50):
#     n = int(input(f'Guess a number between 0 and 1000 : '))
#     if n < t :
#         print ('It is smaller')
#         if 0 > n-t >= -5 :
#             print ('You are quite close!')
#     elif n > t:
#         print ('It is bigger')
#         if 0 < n-t <= 5 :
#             print ('You are quite close!')
#     else:
#         print ('Your number is correct! ')
#         break

# # Guess a random number by the user
# import random
# guessed = False
# upper_limit = 100
# lower_limit = 1
# while guessed is False:
#     try:
#         comp_guess = random.randint(lower_limit+1,upper_limit-1)
#         print(comp_guess)
#     except:
#         print('Maybe you have forgotten your own number because you are giving me wrong hints.')
#         quit()
#     user_response = False
#     while not user_response :
#         user_input = input('FEEDBACK -- ')
#         if user_input == 'correct':
#             print('Woohooo!!')
#             user_response = True
#             guessed = True
#         elif user_input == 'higher':
#             lower_limit = comp_guess
#             user_response = True
#         elif user_input == 'lower':
#             upper_limit = comp_guess
#             user_response = True
#         else:
#             print("I don't understand.")

# # Rock, Paper and scissors
# import random
# list = ('rock', 'paper', 'scissors')
# pick = random.choice(list)
# player_pick = input('Choose among rock, paper or scissors\n')
# def tie (a,b):
#     if a==b:
#         print('It is a tie! ')
# def win (a,b):
#     if a == 'rock' and b == 'paper':
#         print (f'{b} wins as paper beats rock')
#     elif a == 'paper' and b == 'scissors':
#         print (f'{b} wins as scissors cuts paper')
#     elif a == 'scissors' and b == 'rock':
#         print (f'{b} wins as rock defeats scissors')
# def result (a,b):
#     if tie (a,b) == True:
#         return (tie(a,b))
#     else :
#         return (win (a,b) ) or (win (b,a))
# print (f'The computer chose {pick} ')
# result(pick,player_pick)

# # Unjumble words
# file = open('/Python/.vscode/Main/All english words.txt','r')
# data = file.read()
# words_list = data.split(', ')
# user_input = input('Enter the jumbled word\n')
# jumbled_letters = user_input.split(',')
# jumbled_letters.sort()
# for i in words_list:
#     word = []
#     for j in i:
#         word.append(j)
#     word.sort()
#     if word == jumbled_letters:
#         print(f'Unjumbled word(s) are -- {i}')
#     else:
#         continue

# # Hangman game
# import random
# file = open('C:\\Users\\KIIT\\Desktop\\Code\\Python\\Main\\List of words for hangman.txt','r')
# data = file.read()
# newdata = data.replace('"','')
# words = newdata.split(',')
# file.close()

# no_of_guesses_list = []
# no_of_hints_list = []
# no_of_lives_list = []
# no_of_rounds = [0]
# def hangman_game():
#     no_of_rounds[0] += 1 #Stack overflow
#     pick = str(random.choice(words))
#     guessed_list = []
#     my_guesses_list = []
#     mylist = []
#     first_blank = len(pick)*("_ ")
#     blank = len(pick)*("_")
#     print(first_blank ,'\n')
#     for char in blank:
#         mylist.append(char)
#     filled = False
#     lives = 10
#     guess_amount = 0
#     hint_amount = 0
#     while filled is False:
#         guess = input('Start guessing! \nYour guess -- ')
#         guess = guess.lower()
#         result = list(set(pick)^set(guessed_list)) # list for the right letters not guessed by the user (Stack overflow)
#         # HINT SYSTEM
#         if guess == '*':
#             hint_amount = hint_amount + 1
#             user_answer = False
#             if hint_amount == 4 :
#                 hint_amount = hint_amount - 1
#                 print('You have used up all of your hints!\n')
#                 continue
#             else :
#                 while user_answer == False:
#                     print("Do you really want a hint?\n")
#                     answer = input("Press y for 'yes' or n for 'no'. \n")
#                     if answer == 'y':
#                         print(f"I think you should go with '{random.choice(result)}'.\nNow, you have {3-hint_amount} hints left.")
#                         user_answer = True
#                     elif answer == 'n':
#                         print('Be sure to use hints whenever necessary!')
#                         hint_amount = hint_amount - 1
#                         user_answer = True
#                         continue
#                     else:
#                         print('Press either y or n only')
#                         user_answer = False
#         # USER WANTS TO QUIT GAME IN BETWEEN
#         elif guess == 'quit':
#             user_answer = False
#             while user_answer is False:
#                 print('Are you sure you wanna quit the game??')
#                 answer = input("Press y for 'yes' or n for 'no'. \n")
#                 if answer == 'y':
#                     print('Alright, have a good day!')
#                     quit()
#                 elif answer == 'n':
#                     print('Continuing the game -')
#                     user_answer = True
#                 else:
#                     print('Press either y or n only')
#                     user_answer == False
#         # IF MORE THAN ONE LETTER IS ENTERED BY USER
#         elif len(guess) >= 2:
#             print('Only one alphabet at a time!')
#         # IF GUESSES NOTHING
#         elif guess == '':
#             print('Guess something!!')
#         # IF USER CORRECTLY GUESSES A LETTER
#         elif guess in pick :
#             # IF USER REPEATES RIGHT LETTERS
#             if guess in guessed_list:
#                 print ('You have already guessed this letter. Try something else!')
#                 continue
#             # IF USER CORRECTLY GUESSES A LETTER
#             else:
#                 guess_amount = guess_amount + 1
#                 guessed_list.append(guess)
#                 a = -1
#                 pos = None
#                 for char in pick:
#                     a = a + 1
#                     if char == guess:
#                         pos = a
#                         mylist.pop(pos)
#                         mylist.insert(pos,guess)
#                         if list(pick) == mylist:
#                             filled = True
#                             print('Congratulations!! You have correctly guessed my word --',pick)
#                             print(f'\n\t**** STATS **** \nIt took you {guess_amount} guesses to guess my word. \nYou had {lives} lives remaining.\nYou used {hint_amount} out of your 3 hints. \n')
#                             break
#         # LIVES AND REPEATED LETTERS SYSTEM
#         else:
#             # USER REPEATES WRONG LETTER
#             guess_amount = guess_amount + 1
#             lives = lives - 1
#             if guess in my_guesses_list:
#                 guess_amount = guess_amount - 1
#                 lives = lives + 1
#                 print ('You have already guessed this letter. Try something else!')
#                 continue
#             # USER CHOOSES WRONG LETTER AND LOSES LIFE
#             else:
#                 my_guesses_list.append(guess)
#                 if lives > 1:
#                     print(lives,'lives left.')
#                 elif lives == 1:
#                     print("Only 1 life left.\nYou could have a hint by pressing '*'.\nBut remember you only have 3 hints total.")
#                 else:
#                     print('Sorry, but you are out of life! Game over. Better luck next time!\nThe word was --', pick,'\n')
#                     break
#         # PRINTS THE BLANKS
#         if filled != True:
#             for elements in mylist:
#                 print(elements ,end=' ')
#             print('\n')
#     # STATISTICS OF ALL GAMES
#     no_of_guesses_list.append(guess_amount)
#     no_of_hints_list.append(hint_amount)
#     no_of_lives_list.append(lives)
#     rounds = no_of_rounds[0]
#     result = None
#     if lives == 0:
#         result = 'You lost :('
#     else:
#         result = 'You won :)'
#     file2 = open('/Python/.vscode/Main/Hangman game score.txt','a')
#     file2.write(f'''ROUND - {rounds}\nThe word was - {pick}\nNumber of guesses -- {no_of_guesses_list[(rounds)-1]}
# Number of hints used -- {no_of_hints_list[(rounds)-1]}\nNumber of lives left -- {no_of_lives_list[(rounds)-1]}\nResult -- {result}\n\n''')
#     file2.close()
#     # ASKS IF YOU WANNA PLAY AGAIN
#     user_response = False
#     while user_response is False:
#         play_again = input("Wanna play more?? \nPress y for 'yes' or n for 'no'. \n")
#         if play_again == 'y':
#             return(hangman_game()) # runs game again
#         elif play_again == 'n':
#             # ASKS FOR STATS FOR CURRENT SESSION
#             user_stats = input("Would you like to have the statistics of your games??\ny for 'yes' or n for 'no'\n")
#             if user_stats == 'y':
#                 print(f'Number of rounds -- {no_of_rounds[0]} \nNumber of guesses each game')
#                 for elements in no_of_guesses_list:
#                     print(elements, end=" ")
#                 print('\nNumber of hints used each game')
#                 for elements in no_of_hints_list:
#                     print(elements, end=' ')
#                 print('\nNumber of lives remaining each game')
#                 for elements in no_of_lives_list:
#                     print(elements, end=' ')
#                 print('\nSee you next time!')
#                 break
#             elif user_stats == 'n':
#                 print('Alright, have a good day!')
#                 break
#         else:
#             print('Press either y or n.')
#             user_response = False
#     file2 = open('/Python/.vscode/Main/Hangman game score.txt','r+')
#     data = file2.read()
#     times = data.count('SESSION')
#     file2.write(f'SESSION {times+1}:\n')
#     file2.close()
# hangman_game()

# Spellathon helper
# user_input = input('Enter words here\n')
# def alphabet_taken(user_input):
#     user_input = user_input.split(',')
#     for length in range(4,6):
#         for y in range(len(user_input)):
#             if len(user_input) >= y+length:
#                 print(user_input[y:y+length])
#             else:
#                 print(user_input[y])

# alphabet_taken(user_input)

# mylist = []
# n = int(input("Enter the value of n\n"))
# for i in range(n):
#     mylist.append(int(input("Enter the values\n")))
# mylist = [235,325,234,552,908,867,372,653]
# mylist.sort()
# print(mylist[-2])
