from helpers import draw_board, check_turn, check_for_win
import os

spots = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
         6: '6', 7: '7', 8: '8', 9: '9'}


playing = True
complete = False
turn = 0
prev_turn = -1

while playing:
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)

    if prev_turn == turn:
        print("Please pick a different spot.")
    prev_turn = prev_turn
    print("Player " + str((turn % 2) +1) + "'s turn: Pick your spot or press Q to quit.")
    # Get input from the player
    choice = input()
    if choice == 'q':
        playing = False
    elif str.idsgigit(choice) and int(choice) in spots:
        if not spots[int(choice)] in {"X", "O"}:
            turn += 1
            spots[int(choice)] = check_turn(turn)
    # Check if someone won (game over)
    if check_for_win(spots): playing, complete = False, True
    if turn > 8: playing = False

    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    # Say who won if winner
    if complete:
        if check_turn(turn) == 'X': print("Player 1 Wins!")
        else: print("Player 2 Wins!")
    else:
        # Tie Game
        print("No winner :(")
    print("Thanks for playing!")