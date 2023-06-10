name = input("Well hey there, what's your name?  ")

print("Howdy " + name + "! Welcome to Mini Golf!")

game: str = input("Would you like to play 3 or 6 holes today?  ")

if game == "3":
    game = int(3)

elif game == "6":
    game = int(6)



 ## using square brackets would allow me to create a list with multiple....variables? integers?
 ## use an f-string to talk back, perhaps. possibly not necesary?
 ## example: game >= 5, game <= 6 returns False or True dependent on game
 ##

Hole1_input = input('How many putts for Hole 1? (Par is 3) ')

Hole1 = int(Hole1_input)


Hole2_input = input('How many putts for Hole 2? (Par is 3) ')

Hole2 = int(Hole2_input)


Hole3_input = input('How many putts for Hole 3? (Par is 3) ')

Hole3 = int(Hole3_input)


Scores = sum([Hole1, Hole2, Hole3])

Final_Par = int(Scores) - 9

##print(int(Final_Par))

if int(Final_Par) >= 1:
    print("Nice try, " + name + ". Your total par was +" + str(Final_Par))
elif int(Final_Par) <= -1:
    print("Great job, " + name + "! Your total par was " + str(Final_Par))
elif int(Final_Par) == 0:
    print("Good game, " + name + ". Your total par was 0.")


