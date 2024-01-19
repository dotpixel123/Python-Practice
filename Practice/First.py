# L1 = [1, 1.33, 'ATIC', 0, 'NO', None, 'G', True]
# vall, val2 = 0, ''

# for x in L1:
#     if (type (x) == int or type (x) == float):
#         vall += x
#     elif (type (x) == str):
#         val2 += x
#     else:
#         break
# print(vall,val2)

# word = "Python Programming"
# n = len(word)
# word1 = word.upper()
# word2 = word.lower()
# converted_word = ''
# for i in range(n):
#     if i % 2 == 0:
#         converted_word += word2[i]
#     else:
#         converted_word += word1[i]
# print(converted_word)

# a = int(input('Enter the number\n'))
# for i in range(1, a):
#     prime = 1
#     for j in range(2, i):
#         if i % j == 0:
#             prime = 0
#             break
#         else:
#             continue
#     if prime == 1:
#         print(i)

# a = int(input("Enter the number\n"))
# for i in range(1, a):
#     div = 0
#     for j in range(2, i):
#         if i%j == 0:
#             div += 1
#     if div == 0:
#         print(i)

# a = 283
# for i in range(1,11):
#     print(f"{a} x {i} = {a*i}")

# n = int(input("Enter the value of n\n"))
# a = 0
# b = 1
# for i in range(n):
#     print(a)
#     sum = a + b
#     a = b
#     b = sum

# def lar_diff(list):
#     list.sort()
#     diff = list[-1] - list[0]
#     print(diff)
# a = [1, 2, 10, 11, 12, 6, 7, 8, 9]
# lar_diff(a)


# def param_count(*args):
#     print(len(args))
# param_count(23,5,32,52,2)

# # Method 1
# def format_number(n):
#     n = list(str(n))
#     n.reverse()
#     no_comma = len(n)/3
#     if no_comma == int(no_comma):
#         no_comma -= 1
#     for i in range(1, int(no_comma)+1):
#         if i == 1:
#             n.insert(3*i, ',')
#         else:
#             n.insert(4*i - 1, ',')
#     n.reverse()
#     return ''.join(n)
# a = format_number(1000)
# print(a)
# # Method 2
# my_num = 235478.875425
# s = "{:,}".format(my_num)
# print(s)
# s = "{:.2f}".format(my_num)
# print(s)

b = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(b):
    find = find_empty(b)  # Check empty box
    if not find:
        return True  # Final state of the board when every box is filled
    else:
        row, col = find

    for i in range(1, 10):
        if valid(b, i, (row, col)):
            b[row][col] = i  # Place the number in the board if its valid

            if solve(b):
                return True  # Continue from that board state onwards

            b[row][col] = 0

    return False


def valid(b, num, pos):

    for i in range(len(b[0])):  # Check row
        # Check element in row if its equal to the number added and if its the current position being added to then ignore it
        if b[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(b)):  # Check column
        # Check element column-wise if it equals the number added and its not the position that the new number was just added into
        if b[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3  # Check 3x3 box
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):  # Loop through the 3x3 boxes
        for j in range(box_x * 3, box_x*3 + 3):
            # Check if same number exits in the 3x3 box and (i, j) was the position the new number was just added to
            if b[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            # Separate sections of the board row-wise (Every 3x3 box)
            print("- - - - - - - - - - - - - ")

        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                # Separate sections of the board column-wise
                print(" | ", end="")

            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end="")


def find_empty(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:  # Check if there is a 0 in each position of the box
                return (i, j)   # Return the  row and column

    return None


print_board(b)
print(" ")
solve(b)
print_board(b)


# import random

# """
# Generate the UNO deck of 108 cards.
# Parameters: None
# Return values: deck->list
# """


# def buildDeck():
#     deck = []
#     # example card: Red 7, Green 8, Blue Skip
#     colours = ["Red", "Green", "Yellow", "Blue"]
#     values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Draw Two", "Skip", "Reverse"]
#     wilds = ["Wild", "Wild Draw Four"]
#     for colour in colours:
#         for value in values:
#             cardVal = "{} {}".format(colour, value)
#             deck.append(cardVal)
#             if value != 0:
#                 deck.append(cardVal)
#     for i in range(4):
#         deck.append(wilds[0])
#         deck.append(wilds[1])
#     return deck


# """
# Shuffles a list of items passed into it
# Parameters: deck->list
# Return values: deck->list
# """


# def shuffleDeck(deck):
#     for cardPos in range(len(deck)):
#         randPos = random.randint(0, 107)
#         deck[cardPos], deck[randPos] = deck[randPos], deck[cardPos]
#     return deck


# """Draw card function that draws a specified number of cards off the top of the deck
# Parameters: numCards -> integer
# Return: cardsDrawn -> list
# """


# def drawCards(numCards):
#     cardsDrawn = []
#     for x in range(numCards):
#         cardsDrawn.append(unoDeck.pop(0))
#     return cardsDrawn


# """
# Print formatted list of player's hand
# Parameter: player->integer, playerHand->list
# Return: None
# """


# def showHand(player, playerHand):
#     print("Player {}'s Turn".format(player+1))
#     print("Your Hand")
#     print("------------------")
#     y = 1
#     for card in playerHand:
#         print("{}) {}".format(y, card))
#         y += 1
#     print("")


# """
# Check whether a player is able to play a card, or not
# Parameters: colour->string, value->string, playerHand->list
# Return: boolean
# """


# def canPlay(colour, value, playerHand):
#     for card in playerHand:
#         if "Wild" in card:
#             return True
#         elif colour in card or value in card:
#             return True
#     return False


# unoDeck = buildDeck()
# unoDeck = shuffleDeck(unoDeck)
# unoDeck = shuffleDeck(unoDeck)
# discards = []

# players = []
# colours = ["Red", "Green", "Yellow", "Blue"]
# numPlayers = int(input("How many players? "))
# while numPlayers < 2 or numPlayers > 4:
#     numPlayers = int(
#         input("Invalid. Please enter a number between 2-4. How many players? "))
# for player in range(numPlayers):
#     players.append(drawCards(5))

# playerTurn = 0
# playDirection = 1
# playing = True
# discards.append(unoDeck.pop(0))
# splitCard = discards[0].split(" ", 1)
# currentColour = splitCard[0]
# if currentColour != "Wild":
#     cardVal = splitCard[1]
# else:
#     cardVal = "Any"

# while playing:
#     showHand(playerTurn, players[playerTurn])
#     print("Card on top of discard pile: {}".format(discards[-1]))
#     if canPlay(currentColour, cardVal, players[playerTurn]):
#         cardChosen = int(input("Which card do you want to play? "))
#         while not canPlay(currentColour, cardVal, [players[playerTurn][cardChosen-1]]):
#             cardChosen = int(
#                 input("Not a valid card. Which card do you want to play? "))
#         print("You played {}".format(players[playerTurn][cardChosen-1]))
#         discards.append(players[playerTurn].pop(cardChosen-1))
#         # Check if player won
#         if len(players[playerTurn]) == 0:
#             playing = False
#             winner = "Player {}".format(playerTurn+1)
#         else:
#             # Check for special cards
#             splitCard = discards[-1].split(" ", 1)
#             currentColour = splitCard[0]
#             if len(splitCard) == 1:
#                 cardVal = "Any"
#             else:
#                 cardVal = splitCard[1]
#             if currentColour == "Wild":
#                 for x in range(len(colours)):
#                     print("{}) {}".format(x+1, colours[x]))
#                 newColour = int(
#                     input("What colour would you like to choose? "))
#                 while newColour < 1 or newColour > 4:
#                     newColour = int(
#                         input("Invalid option. What colour would you like to choose? "))
#                 currentColour = colours[newColour-1]
#             if cardVal == "Reverse":
#                 playDirection = playDirection * -1
#             elif cardVal == "Skip":
#                 playerTurn += playDirection
#                 if playerTurn >= numPlayers:
#                     playerTurn = 0
#                 elif playerTurn < 0:
#                     playerTurn = numPlayers-1
#             elif cardVal == "Draw Two":
#                 playerDraw = playerTurn+playDirection
#                 if playerDraw == numPlayers:
#                     playerDraw = 0
#                 elif playerDraw < 0:
#                     playerDraw = numPlayers-1
#                 players[playerDraw].extend(drawCards(2))
#             elif cardVal == "Draw Four":
#                 playerDraw = playerTurn+playDirection
#                 if playerDraw == numPlayers:
#                     playerDraw = 0
#                 elif playerDraw < 0:
#                     playerDraw = numPlayers-1
#                 players[playerDraw].extend(drawCards(4))
#             print("")
#     else:
#         print("You can't play. You have to draw a card.")
#         players[playerTurn].extend(drawCards(1))

#     playerTurn += playDirection
#     if playerTurn >= numPlayers:
#         playerTurn = 0
#     elif playerTurn < 0:
#         playerTurn = numPlayers-1

# print("Game Over")
# print("{} is the Winner!".format(winner))
