# Student Name/Author : Mohak Wathare
# Student ID : 29525756
# Start Date : 4th August 2018
# Last Modified Date : 17th August 2018

# Matrix for identifying the winner of battles.
advantageMatrix = [[0, 1, 2], [2, 0, 1], [1, 2, 0]]
unitList = ["Archer", "Soldier", "Knight"]
# List storing the max healths of each unit.
maxHealthList = [1, 2, 3]
# Damage dealt in each case. Advantage unit/Weaker unit/No Advantage units.
advantageDamage = 3
weakerDamage = 1
noAdvDamage = 2

# Function for selecting/recruiting units.
# Out : playerUnitList - player unit list selected by the player. playerUnitHealth - player unit health list.
def unit_Selection_Funtion():
    standardUnitCost = 1
    playerUnitList = []
    playerUnitHealth = []
    exitFlag = False
    totalMoney = 10

    # Loop runs till the user enters the "finish selection" option or if he runs out of money.
    while (not exitFlag):
        correctOption = False
        print("Remaining money left :", totalMoney)
        # Loop runs till user selects a correct option for a unit or selects "finish selection".
        while (not correctOption):
            try:
                selectedUnit = int(input("Unit selection menu (Enter corresponding index/number): \n1. Archer\n2. Soldier\n3. Knight\n4. Finish selection\n"))
                # If user selects 1-4, they can proceed or else they are prompted to select an option again.
                if (selectedUnit < 5 and selectedUnit > 0):
                    correctOption = True
                else:
                    print("Wrong option entered! Please enter again.")
            except(RuntimeError, TypeError, ValueError):
                print("Wrong option entered! Please enter again.")

        # If correct option is selected, unit is inserted in player unit list. Health list is appended with max health for that unit.
        if (selectedUnit > 0 and selectedUnit < 4):
            playerUnitList.append(selectedUnit)
            playerUnitHealth.append(maxHealthList[selectedUnit-1])
            totalMoney -= standardUnitCost
        # Player selects 4 for exiting player selection menu.
        elif (selectedUnit == 4):
            exitFlag = True

        if (totalMoney == 0):
            exitFlag = True
            print("All your money has been spent! Your army is ready to battle!")

    return playerUnitList, playerUnitHealth

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

# Function for displaying units health list.
# In : teamHealthList - unit health list for player. counter - from which index to start displaying units.
# Out : returns the unit health list for displaying in format.
def display_Health(teamHealthList, counter):
    displayList = "["
    while (counter != len(teamHealthList)):
        if (counter == len(teamHealthList) - 1):
            displayList += str(teamHealthList[counter])
        else :
            displayList += str(teamHealthList[counter]) + ", "
        counter = counter + 1
    return displayList + "]"


# Function for calculating match winner from "advantageMatrix".
# In : unitForPlayer1 - unit competing for player 1. unitForPlayer2 - unit competing for player 2.
# Out : returns the match winner. 1 for player 1. 2 for player 2. 0 for draw.
def match_Winner_Calc(unitForPlayer1, unitForPlayer2):
    matchWinner = advantageMatrix[unitForPlayer1 - 1][unitForPlayer2 - 1]
    return matchWinner

# Function for displaying which unit died in battle.
# In : unitForPlayer - unit competing for player. playerNumber - unit belonging to which player.
# Out : returns which unit died in battle and for which player.
def player_Unit_Dies_Battle(unitForPlayer, playerNumber):
    return "PLayer " + str(playerNumber) + " unit " + unitList[unitForPlayer - 1] + " dies in fight!"

# Function for reviving a unit. Adds revived player at end of list. Adds max health of unit at end of health list.
# In : unitForPlayer - unit competing for player. playerUnitList - unit list for player. unitHealthList - unit health list for player.
def revive_Unit(unitForPlayer, playerUnitList, unitHealthList):
    playerUnitList.append(unitForPlayer)
    unitHealthList.append(maxHealthList[unitForPlayer - 1])

# Function for displaying medic used for player.
# In : unit - unit competing for player. player - player number.
def medic_Used(unit, player):
    return "Medic used to revive " + unitList[unit - 1] + " for Player " + str(player) + "."


mainMenuFlag = True

# Loop runs till the user specifies that they don't want to battle anymore.
while (mainMenuFlag):
    # Lists for player units and health.
    player1UnitList = []
    player1UnitHealth = []
    player2UnitList = []
    player2UnitHealth = []
    army1Counter = 0
    army2Counter = 0
    fightExitFlag = False

    # Army selection for Player 1. Leftover money is spent to buy medics.
    print("Player 1 turn:")
    player1UnitList, player1UnitHealth = unit_Selection_Funtion()
    print("Player 1 army list - " + display_Units(player1UnitList, 0))
    medicCountPlayer1 = 10 - len(player1UnitList)
    print("Remaining money spent to buy ", medicCountPlayer1, "medics.")

    # Army selection for Player 2. Leftover money is spent to buy medics.
    print("Player 2 turn:")
    player2UnitList, player2UnitHealth = unit_Selection_Funtion()
    print("Player 2 army list - " + display_Units(player2UnitList, 0))
    medicCountPlayer2 = 10 - len(player2UnitList)
    print("Remaining money spent to buy ", medicCountPlayer2, "medics.")

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

            # Extracting health of units from their respective lists with index counters.
            healthForPlayer1CurrUnit = player1UnitHealth[army1Counter]
            healthForPlayer2CurrUnit = player2UnitHealth[army2Counter]

            print("\nFight",fightCounter,":", unitList[unitForPlayer1-1], "vs", unitList[unitForPlayer2-1])

            # Calculates the match winner from "advantageMatrix".
            matchWinner = match_Winner_Calc(unitForPlayer1, unitForPlayer2)

            # Same unit fight. Unit health is adjusted accordingly (no advantage fight).
            if (matchWinner == 0):
                player1UnitHealth[army1Counter] = player1UnitHealth[army1Counter] - noAdvDamage
                player2UnitHealth[army2Counter] = player2UnitHealth[army2Counter] - noAdvDamage
            # Player 1 unit wins. Unit health is adjusted accordingly (player 1 unit has advantage over player 2 unit).
            elif (matchWinner == 1):
                player1UnitHealth[army1Counter] = player1UnitHealth[army1Counter] - weakerDamage
                player2UnitHealth[army2Counter] = player2UnitHealth[army2Counter] - advantageDamage
            # Player 2 unit wins. Unit health is adjusted accordingly (player 2 unit has advantage over player 1 unit).
            else:
                player1UnitHealth[army1Counter] = player1UnitHealth[army1Counter] - advantageDamage
                player2UnitHealth[army2Counter] = player2UnitHealth[army2Counter] - weakerDamage

            # If player 1's unit health is less than 0, then it's dead and the index counter increases.
            if (player1UnitHealth[army1Counter] <= 0):
                army1Counter += 1
                print(player_Unit_Dies_Battle(unitForPlayer1, 1))
                # If medic is available for player 1, it is used. Unit and health are put at end of respective lists.
                if (medicCountPlayer1 != 0):
                    medicCountPlayer1 -= 1
                    # Medic revives unit placing it at end of list. Adds unit max health at the end of health list.
                    revive_Unit(unitForPlayer1, player1UnitList, player1UnitHealth)
                    print(medic_Used(unitForPlayer1, 1))

            # If player 2's unit health is less than 0, then it's dead and the index counter increases.
            if (player2UnitHealth[army2Counter] <= 0):
                army2Counter += 1
                print(player_Unit_Dies_Battle(unitForPlayer2, 2))
                # If medic is available for player 2, it is used. Unit and health are put at end of respective lists.
                if (medicCountPlayer2 != 0):
                    medicCountPlayer2 -= 1
                    # Medic revives unit placing it at end of list. Adds unit max health at the end of health list.
                    revive_Unit(unitForPlayer2, player2UnitList, player2UnitHealth)
                    print(medic_Used(unitForPlayer2, 2))

            # Post fight summary.
            print("Post Fight Summary :")
            print("Player 1 army list - " + display_Units(player1UnitList, army1Counter))
            print("Player 1 army's health list - " + display_Health(player1UnitHealth, army1Counter))
            print("Medic count for Player 1 : ", medicCountPlayer1)
            print("\nPlayer 2 army list - " + display_Units(player2UnitList, army2Counter))
            print("Player 2 army's health list - " + display_Health(player2UnitHealth, army2Counter))
            print("Medic count for Player 2 : ", medicCountPlayer2)

            fightCounter += 1

            # Player 1 and Player 2 are out of battle as they both are out of units - Draw.
            if ((army1Counter == len(player1UnitList)) and (army2Counter == len(player2UnitList))):
                print("\nIt's a draw. Both players are out of units to fight with.")
                fightExitFlag = True
            # Player 1 wins as Player 2 is out of units.
            elif (army2Counter == len(player2UnitList)):
                print("\nPlayer 1 wins. Player 2 is out of units to fight with.")
                fightExitFlag = True
            # Player 2 wins as Player 1 is out of units.
            elif (army1Counter == len(player1UnitList)):
                print("\nPlayer 2 wins. Player 1 is out of units to fight with.")
                fightExitFlag = True


    while (True):
        try:
            newGame = int(input("Want to play another game?\n1.Yes\t2.No\n"))
            if (newGame == 2):
                mainMenuFlag = False
            break
        except(RuntimeError, TypeError, ValueError):
            print("Wrong option entered! Please enter again.")