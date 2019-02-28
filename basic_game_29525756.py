# Student Name/Author : Mohak Wathare
# Student ID : 29525756
# Start Date : 4th August 2018
# Last Modified Date : 17th August 2018

# Matrix for identifying the winner of battles.
advantageMatrix = [[0, 1, 2], [2, 0, 1], [1, 2, 0]]
unitList = ["Archer", "Soldier", "Knight"]

# Function for selecting/recruiting units.
# Out : player unit list for that player selected by the player.
def unit_Selection_Funtion():
    standardUnitCost = 1
    playerUnitList = []
    exitFlag = False
    totalMoney = 10

    # Loop runs till the user enters the "finish selection" option or if he runs out of money.
    while (not exitFlag):
        correctOption = False
        print("Remaining money left :", totalMoney)
        # Loop runs till user selects a correct option for a unit or selects "finish selection".
        while (not correctOption):
            try:
                selectedUnit = int(input("Unit selection menu (Type corresponding index/number): \n1. Archer\n2. Soldier\n3. Knight\n4. Finish selection\n"))
                # If user selects 1-4, they can proceed or else they are prompted to select an option again.
                if (selectedUnit < 5 and selectedUnit > 0):
                    correctOption = True
                else:
                    print("Wrong option entered! Please enter again.")
            except(RuntimeError, TypeError, ValueError):
                print("Wrong option entered! Please enter again.")

        # If correct option is selected, then unit is inserted in player unit list.
        if (selectedUnit > 0 and selectedUnit < 4):
            playerUnitList.append(selectedUnit)
            totalMoney -= standardUnitCost
        # Player selects 4 for exiting player selection menu.
        elif (selectedUnit == 4):
            exitFlag = True

        if (totalMoney == 0):
            exitFlag = True
            print("All your money has been spent! Your army is ready to battle!")

    return playerUnitList

# Function for displaying units list.
# In : teamUnitList - unit list for player. counter - from which index to start displaying units.
# Out : returns the unit list for displaying in format.
def display_Units(teamUnitList, counter):
    displayList = "["
    while (counter != len(teamUnitList)):
        if (counter == len(teamUnitList) - 1):
            displayList += unitList[teamUnitList[counter] - 1]
        else :
            displayList += unitList[teamUnitList[counter] - 1] + ", "
        counter += 1
    return displayList + "]"

# Function for calculating match winner from "advantageMatrix".
# In : unitForPlayer1 - unit competing for player 1. unitForPlayer2 - unit competing for player 2.
# Out : returns the match winner. 1 for player 1. 2 for player 2. 0 for draw.
def match_Winner_Calc(unitForPlayer1, unitForPlayer2):
    matchWinner = advantageMatrix[unitForPlayer1 - 1][unitForPlayer2 - 1]
    return matchWinner

# Function for printing the winner of the battle between units.
# Out : string which says which player won the battle.
def player_Wins_Battle(playerNumber):
    return "Player " + str(playerNumber) + " wins fight!"


mainMenuFlag = True

# Loop runs till the user specifies that they don't want to battle anymore.
while (mainMenuFlag):
    player1UnitList = []
    player2UnitList = []
    army1Counter = 0
    army2Counter = 0
    fightExitFlag = False

    # Army selection for Player 1 and 2.
    print("Player 1 turn:")
    player1UnitList = unit_Selection_Funtion()
    print("Player 1 army list - " + display_Units(player1UnitList, 0))

    print("Player 2 turn:")
    player2UnitList = unit_Selection_Funtion()
    print("Player 2 army list - " + display_Units(player2UnitList, 0))

    # Checks if there are empty armies selected by either or both the players. If not then battle commences in else.
    if (len(player1UnitList) > 0 and (not player2UnitList)):
        print("Player 2 has no army! Player 1 wins by default! Easy win.")
    elif ((not player1UnitList) and len(player2UnitList) > 0):
        print("Player 1 has no army! Player 2 wins by default! Easy win.")
    elif ((not player1UnitList) and (not player2UnitList)):
        print("Both armies have no army! It's a draw/both are disqualified! ")
    else:
        print("Let's Battle!!!")
        # Counter for the number of fights.
        fightCounter = 1

        # Loop runs till all the fights are over and a winner is declared.
        while (not fightExitFlag):
            # Extracting the units for both the players from their respective lists with index counters.
            unitForPlayer1 = player1UnitList[army1Counter]
            unitForPlayer2 = player2UnitList[army2Counter]

            print("Fight",fightCounter,":", unitList[unitForPlayer1-1], "vs", unitList[unitForPlayer2-1])

            # Calculates the match winner from "advantageMatrix".
            matchWinner = match_Winner_Calc(unitForPlayer1, unitForPlayer2)

            # Same unit fight. Both index counters are increased by one for next battle.
            if (matchWinner == 0):
                army1Counter += 1
                army2Counter += 1
                print("Fight tied! Both combatants loose.")
            # Player 1 unit wins. Index counter for player 2 is increased as player 1's unit stays in battle.
            elif (matchWinner == 1):
                army2Counter += 1
                print(player_Wins_Battle(1))
            # Player 2 unit wins. Index counter for player 2 is increased as player 2's unit stays in battle.
            else:
                army1Counter += 1
                print(player_Wins_Battle(2))

            print("Player 1 army list - " + display_Units(player1UnitList, army1Counter))
            print("Player 2 army list - " + display_Units(player2UnitList, army2Counter))

            fightCounter += 1

            # Player 1 wins as Player 2 is out of units.
            if ((army1Counter != len(player1UnitList)) and (army2Counter == len(player2UnitList))):
                print("\nPlayer 1 wins. Player 2 is out of units to fight with.")
                fightExitFlag = True
            # Player 2 wins as Player 1 is out of units.
            elif ((army1Counter == len(player1UnitList)) and (army2Counter != len(player2UnitList))):
                print("\nPlayer 2 wins. Player 1 is out of units to fight with.")
                fightExitFlag = True
            # Player 1 and Player 2 are out of battle as they both are out of units - Draw.
            elif ((army1Counter == len(player1UnitList)) and (army2Counter == len(player2UnitList))):
                print("\nIt's a draw. Both players are out of units to fight with.")
                fightExitFlag = True

    while (True):
        try:
            newGame = int(input("Want to play another game?\n1.Yes\t2.No\n"))
            if (newGame == 2):
                mainMenuFlag = False
            break
        except(RuntimeError, TypeError, ValueError):
            print("Wrong option entered! Please enter again.")