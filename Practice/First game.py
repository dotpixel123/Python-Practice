#Snake, Water and Gun game

#1st attempt 
 
option = ["snake", "water", "gun"]

a = input('Choose among snake, water or gun ')
b = input('Choose among snake, water or gun ')

def order(a,b):
    if a == "snake":
        if  b == "water"  :
            print (a + "wins as snake drinks water!")
    else :
        print ('no')

(order(a, b))
# print (order(player_2, player_1))











    # if player_1 == option[0] and player_2 == option[1]:
    #     print (player_1 + " wins as snake drinks water!")
    # if player_1 == "water" and player_2 == "gun":
    #     print (f"{player_1} wins as gun has no effect on water! ")
    # if player_1 == "gun" and player_2 == "snake":
    #     print (f"{player_1} wins as gun shoots and kills snake! ")
    # else :
    #     print ('no')