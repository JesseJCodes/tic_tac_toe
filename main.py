reset = True
while reset:
    print(f"Welcome to My Tic Tac Toe Game! ®Rene Zance")
    player1mark = ""
    done = False
    game_done = False
    while done is False:
        multiplayer_choice = input('Would you like to play a friend or computer?\n')
        if 'f' in multiplayer_choice.lower():
            multiplayer = True
        elif 'c' in multiplayer_choice.lower():
            multiplayer = False
        else:
            print("Invalid input.")
        player_choice = input('Would you like to be "X" or "O"? ').upper()
        if player_choice == 'X':
            player1mark = "X"
            player2mark = "O"
            print(f"You are {player1mark}")
            done = True
        elif player_choice == 'O':
            player1mark = "O"
            player2mark = "X"
            print(f"You are {player1mark}")
            done = True
        else:
            print(f"Sorry you entered {player_choice}, an invalid input.")

    gameboard = ("   | |   \n"
                 " -------\n"
                 "   | |  \n"
                 " -------\n"
                 "   | | ")

    game_done = False
    def p1move(mark):
        invalid_input = True
        #controls players move and marks it and updates gameboard
        #positon indexes for player marks = [2, 4, 6, 21, 23, 25, 39, 41, 43]
        global gameboard
        while invalid_input is True:
            position_choice = input("The Rows are 'A-B' Columns '1-2'\n"
                                    "Player 1. Where would you like to go? ").lower()
            if position_choice == 'a1':
                gameboard = list(gameboard)
                gameboard[2] = gameboard[2].replace(" ", f"{mark}")
                gameboard = "".join(gameboard)
                return gameboard
            elif position_choice == 'a2':
                gameboard = list(gameboard)
                gameboard[4] = gameboard[4].replace(" ", f"{mark}")
                gameboard = "".join(gameboard)
                return gameboard
            elif position_choice == 'a3':
                gameboard = list(gameboard)
                gameboard[6] = gameboard[6].replace(" ", f"{mark}")
                gameboard = "".join(gameboard)
                return gameboard
            elif position_choice == 'b1':
                gameboard = list(gameboard)
                gameboard[21] = gameboard[21].replace(" ", f"{mark}")
                gameboard = "".join(gameboard)
                return gameboard
            elif position_choice == 'b2':
                gameboard = list(gameboard)
                gameboard[23] = gameboard[23].replace(" ", f"{mark}")
                gameboard = "".join(gameboard)
                return gameboard
            elif position_choice == 'b3':
                gameboard = list(gameboard)
                gameboard[25] = gameboard[25].replace(" ", f"{mark}")
                gameboard = "".join(gameboard)
                return gameboard
            elif position_choice == 'c1':
                gameboard = list(gameboard)
                gameboard[39] = gameboard[39].replace(" ", f"{mark}")
                gameboard = "".join(gameboard)
                return gameboard
            elif position_choice == 'c2':
                gameboard = list(gameboard)
                gameboard[41] = gameboard[41].replace(" ", f"{mark}")
                gameboard = "".join(gameboard)
                return gameboard
            elif position_choice == 'c3':
                gameboard = list(gameboard)
                gameboard[43] = gameboard[43].replace(" ", f"{mark}")
                gameboard = "".join(gameboard)
                return gameboard
            else:
                print(f"Sorry you entered {position_choice}, an invalid input.")
                invalid_input = True


    def p2move(mark):
        invalid_input = True
        #controls players move and marks it and updates gameboard
        #positon indexes for player marks = [2, 4, 6, 21, 23, 25, 39, 41, 43]
        global gameboard
        while invalid_input is True:
            position_choice = input("The Rows are 'A-B' Columns '1-2'\n"
                                    "Player 2. Where would you like to go? ").lower()
            if position_choice == 'a1':
                gameboard = list(gameboard)
                gameboard[2] = gameboard[2].replace(" ", f"{mark}")
                gameboard = "".join(gameboard)
                return gameboard
            elif position_choice == 'a2':
                gameboard = list(gameboard)
                gameboard[4] = gameboard[4].replace(" ", f"{mark}")
                gameboard = "".join(gameboard)
                return gameboard
            elif position_choice == 'a3':
                gameboard = list(gameboard)
                gameboard[6] = gameboard[6].replace(" ", f"{mark}")
                gameboard = "".join(gameboard)
                return gameboard
            elif position_choice == 'b1':
                gameboard = list(gameboard)
                gameboard[21] = gameboard[21].replace(" ", f"{mark}")
                gameboard = "".join(gameboard)
                return gameboard
            elif position_choice == 'b2':
                gameboard = list(gameboard)
                gameboard[23] = gameboard[23].replace(" ", f"{mark}")
                gameboard = "".join(gameboard)
                return gameboard
            elif position_choice == 'b3':
                gameboard = list(gameboard)
                gameboard[25] = gameboard[25].replace(" ", f"{mark}")
                gameboard = "".join(gameboard)
                return gameboard
            elif position_choice == 'c1':
                gameboard = list(gameboard)
                gameboard[39] = gameboard[39].replace(" ", f"{mark}")
                gameboard = "".join(gameboard)
                return gameboard
            elif position_choice == 'c2':
                gameboard = list(gameboard)
                gameboard[41] = gameboard[41].replace(" ", f"{mark}")
                gameboard = "".join(gameboard)
                return gameboard
            elif position_choice == 'c3':
                gameboard = list(gameboard)
                gameboard[43] = gameboard[43].replace(" ", f"{mark}")
                gameboard = "".join(gameboard)
                return gameboard
            else:
                print(f"Sorry you entered {position_choice}, an invalid input.")
                invalid_input = True


    def score(board):
        global game_done
        #positon indexes for player marks = [2, 4, 6, 21, 23, 25, 39, 41, 43]
        p1score = 0
        p2score = 0
        for mark in list(board):
            if player1mark in board[2] and player1mark in board[4] and player1mark in board[6]:
                print("Player1 Wins!")
                print(board)

                game_done = True
                return game_done



        return game_done


    print("Now it's time to play!")
    print(f"{gameboard}\n"
          f"Pick a column and row.")

    while game_done is False:
        p1move(player1mark)
        if " " not in list(gameboard)[2:6:2] and " " not in list(gameboard)[21:25:2] and " " not in list(gameboard)[39:43:2]:
            print("It's a Tie")
            print(f"{gameboard}")
            game_done = True
        elif player1mark in gameboard[2] and player1mark in gameboard[4] and player1mark in gameboard[6]:
            print("Player1 Wins!")
            print(gameboard)
            game_done = True
        elif player1mark in gameboard[2] and player1mark in gameboard[21] and player1mark in gameboard[39]:
            print("Player1 Wins!")
            print(gameboard)
            game_done = True
        elif player1mark in gameboard[21] and player1mark in gameboard[23] and player1mark in gameboard[25]:
            print("Player1 Wins!")
            print(gameboard)
            game_done = True
        elif player1mark in gameboard[4] and player1mark in gameboard[23] and player1mark in gameboard[41]:
            print("Player1 Wins!")
            print(gameboard)
            game_done = True
        elif player1mark in gameboard[6] and player1mark in gameboard[25] and player1mark in gameboard[43]:
            print("Player1 Wins!")
            print(gameboard)
            game_done = True
        elif player1mark in gameboard[39] and player1mark in gameboard[41] and player1mark in gameboard[43]:
            print("Player1 Wins!")
            print(gameboard)
            game_done = True
        elif player1mark in gameboard[2] and player1mark in gameboard[23] and player1mark in gameboard[43]:
            print("Player1 Wins!")
            print(gameboard)
            game_done = True
        else:
            print(gameboard)
            p2move(player2mark)
            if " " not in gameboard[2:6:2] and " " not in gameboard[21:25:2] and " " not in gameboard[39:43:2]:
                print("It's a Tie")
                print(f"{gameboard}")
                game_done = True
            elif player2mark in gameboard[2] and player2mark in gameboard[4] and player2mark in gameboard[6]:
                print("Player2 Wins!")
                print(gameboard)
                game_done = True
            elif player2mark in gameboard[2] and player2mark in gameboard[21] and player2mark in gameboard[39]:
                print("Player2 Wins!")
                print(gameboard)
                game_done = True
            elif player2mark in gameboard[21] and player2mark in gameboard[23] and player2mark in gameboard[25]:
                print("Player2 Wins!")
                print(gameboard)
                game_done = True
            elif player2mark in gameboard[4] and player2mark in gameboard[23] and player2mark in gameboard[41]:
                print("Player2 Wins!")
                print(gameboard)
                game_done = True
            elif player2mark in gameboard[6] and player2mark in gameboard[25] and player2mark in gameboard[43]:
                print("Player2 Wins!")
                print(gameboard)
                game_done = True
            elif player2mark in gameboard[39] and player2mark in gameboard[41] and player2mark in gameboard[43]:
                print("Player2 Wins!")
                print(gameboard)
                game_done = True
            elif player2mark in gameboard[2] and player2mark in gameboard[23] and player2mark in gameboard[43]:
                print("Player2 Wins!")
                print(gameboard)
                game_done = True
            else:

                print(gameboard)
                game_done = False


    restart = input("Thanks for playing would you like to restart? ").lower()
    if "y" in restart:
        reset = True
    else:
        reset = False
        print("Have a good day!")