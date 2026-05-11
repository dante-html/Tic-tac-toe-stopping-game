import time
import threading
import os

board = [" " for _ in range(9)]
choice = True
stop = False
round = 1
Diff = 0.5
x = 0


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_board():
    clear()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

    print("\n" + "="*20)
    if not choice:
        print("Press Enter to stop X's movement...")


def check_winner(player):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
            [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    return any(board[a] == board[b] == board[c] == player for a, b, c in wins)


def x_moving():
    global stop, choice, Diff, round
    if round == 1:
        Diff = 0.5
    else:
        Diff = 0.3
    while True:
        for move in range(9):
            if board[move] == " " and not stop:
                board[move] = "X"
                print_board()
                time.sleep(Diff)
                board[move] = " "
                print_board()
            if stop:
                board[move] = "X"
                print_board()
                return


print_board()
choice = False
time.sleep(1)
print("You are playing as 'X'. Try to get three in a row, or you lose!")
print("Ready for round 1?")
input("Press Enter to continue...")

while True:
    stop = False
    choice = False
    print_board()
    thread = threading.Thread(target=x_moving)
    thread.start()
    input()
    x += 1
    stop = True
    thread.join()
    choice = True
    if check_winner("X"):
        if round == 1:
            print("You win!")
            round += 1
            x = 0
            board = [" " for _ in range(9)]
            input("Ready for round 2?")
        else:
            print("Congratulations! You've completed the game!")
            answer = input("Do you want to play again? (y/n): ").lower()
            if answer == 'y':
                x = 0
                round = 1
                board = [" " for _ in range(9)]
                print_board()
                input("Ready for round 1?")
            else:
                print("Thanks for playing!")
                break
    elif x == 3:
        answer = input("Do you want to play again? (y/n): ").lower()
        if answer == 'y':
            x = 0
            round = 1
            board = [" " for _ in range(9)]
            print_board()
            input("Ready for round 1?")
        else:
            print("Thanks for playing!")
            break
    time.sleep(0.5)
