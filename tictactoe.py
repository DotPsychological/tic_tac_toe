# Game title and Rules

print(""" 
  _______ _        _______           _______         
 |__   __(_)      |__   __|         |__   __|        
    | |   _  ___     | | __ _  ___     | | ___   ___ 
    | |  | |/ __|    | |/ _` |/ __|    | |/ _ \ / _ \\
    | |  | | (__     | | (_| | (__     | | (_) |  __/
    |_|  |_|\___|    |_|\__,_|\___|    |_|\___/ \___|
                                                                                                         
""")

print("""Game Overview
Tic Tac Toe is a game that requires two players. One will be X == "X " and one will be O.
The objective is draw a line, either horizontal, vertical, or diagonally in a 3x3 before the other player does. X will be starting first in this game and O will then play after x\n"""
)


# Dictionaries for each line
line = {"A1": "A1", "A2": "A2", "A3": "A3","B1": "B1", "B2": "B2", "B3": "B3", "C1": "C1", "C2": "C2", "C3": "C3"}

# Board Visual Representation
print (line["A1"] + " | " + line["A2"] + " | " + line["A3"])
print("———|————|————")
print (line["B1"] + " | " + line["B2"] + " | " + line["B3"])
print("———|————|————")
print (line["C1"] + " | " + line["C2"] + " | " + line["C3"] + "\n")


# Loop for determining the winner of the game
rerun = 0
while True:
  def GameCondition():
    won = False
    if line["A1"] == "X " and line["A2"] == "X " and line["A3"] == "X " or line["A1"] == "O " and line["A2"] == "O " and line["A3"] == "O " :
      if line["A1"] == "X ":
        print("X has won the game")
        won = True
      else:
        print("O has won the game")
        won = True
    elif line["B1"] == "X " and line["B2"] == "X " and line["B3"] == "X " or line["B1"] == "O " and line["B2"] == "O " and line["B3"] == "O ":
      if line["B1"] == "X ":
        print("X has won the game")
        won = True
      else:
        print("O has won the game")
        won = True
    elif line["C1"] == "X " and line["C2"] == "X " and line["C3"] == "X "  or line["C1"] == "O " and line["C2"] == "O " and line["C3"] == "O ":
      if line["C1"] == "X ":
        print("X has won the game")
        won = True
      else:
        print("O has won the game")
        won = True
    elif line["A1"] == "X " and line["B1"] == "X " and line["C1"] == "X " or line["A1"] == "O " and line["B1"] == "O " and line["C1"] == "O ":
      if line["A1"] == "X ":
        print("X has won the game")
        won = True
      else:
        print("O has won the game")
        won = True
    elif line["A2"] == "X " and line["B2"] == "X " and line["C2"] == "X " or line["A2"] == "O " and line["B2"] == "O " and line["C2"] == "O ":
      if line["A2"] == "X ":
        print("X has won the game")
        won = True
      else:
        print("O has won the game")
        won = True
    elif line["A3"] == "X " and line["B3"] == "X " and line["C3"] == "X " or line["A3"] == "O " and line["B3"] == "O " and line["C3"] == "O ":
      if line["A3"] == "X ":
        print("X has won the game")
        won = True
      else:
        print("O has won the game")
        won = True
    elif line["A1"] == "X " and line["B2"] == "X " and line["C3"] == "X " or line["A1"] == "O " and line["B2"] == "O " and line["C3"] == "O ":
      if line["A1"] == "X ":
        print("X has won the game")
        won = True
      else:
        print("O has won the game")
        won = True
    elif line["A3"] == "X " and line["B2"] == "X " and line["C1"] == "X " or line["A3"] == "O"  and line["B2"] == "O " and line["C1"] == "O ":
      if line["A3"] == "X ":
        print("X has won the game")
        won = True
      else:
        print("O has won the game")
        won = True
    return won

  # Inputing the answer  
  answer = str(input("Please enter a box number")).upper()


  # Counting the number of turns 
  if rerun % 2 == 0:
    line[answer] = "X "
    rerun += 1
  else:
    line[answer] = "O "
    rerun += 1
  
  # Determining if there is already a winner
  if GameCondition() == False:
    print (line["A1"] + " | " + line["A2"] + " | " + line["A3"])
    print("———|————|————")
    print (line["B1"] + " | " + line["B2"] + " | " + line["B3"])
    print("———|————|————")
    print (line["C1"] + " | " + line["C2"] + " | " + line["C3"] + "\n")
    continue
  else:    
    print (line["A1"] + " | " + line["A2"] + " | " + line["A3"])
    print("———|————|————")
    print (line["B1"] + " | " + line["B2"] + " | " + line["B3"])
    print("———|————|————")
    print (line["C1"] + " | " + line["C2"] + " | " + line["C3"]+ "\n")
    break
