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
Tic Tac Toe is a game that requires two players. One will be X and one will be O.
The objective is draw a line, either horizontal, vertical, or diagonally in a 3x3 before the other player does. X will be starting first in this game \n"""
)


# Dictionaries for each line
line1 = {"A1": "A1", "A2": "A2", "A3": "A3"}
line2 = {"B1": "B1", "B2": "B2", "B3": "B3"}
line3 = {"C1": "C1", "C2": "C2", "C3": "C3"}

# Board Visual Representation
print (line1["A1"] + " | " + line1["A2"] + " | " + line1["A3"])
print("———|————|————")
print (line2["B1"] + " | " + line2["B2"] + " | " + line2["B3"])
print("———|————|————")
print (line3["C1"] + " | " + line3["C2"] + " | " + line3["C3"])
