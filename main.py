# Name: Zachary Zawodny
# Date: April 24th 2022
# Final Project: Connect 4
# Version 1

from guizero import *
import random

app = App(title='Connect 4 EXTREME', height=600, width=800, layout="grid")

# Text for Game list loop
b_text = 'B'
r_text = 'R'

# Text on the tile buttons
n_text = ""

# Text
swap_text = "Player Mode"
swap_text_player = "Player Mode"
swap_text_ai = "AI Mode"

# Game Statistics
win = 0
loss = 0
tie = 0

# Game Win Record
win_rate_text = "{0} - {0} - {0}".format(win, tie, loss)

# Text to Indicate Turn
b_turn_text = "It's Blue Turn"
r_turn_text = "It's Reds Turn"

# boolean for Ai player, the player's turn, if the game is won
ai_mode = True  # Decides whether you play another player or AI
player_turn = False  # if true its reds turn if its false it's blues turn
game_won = False  # if false

# Default list indicating no tiles are played, each number correlates to a button
game_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


# The Function to find if there is a winner or tie
def CheckForWin():
    global game_list
    global b_text
    global r_text
    global game_won
    global button_list
    for i in range(5):  # For loop logic to find a full vertical column
        if game_list[i] == b_text:
            if game_list[i + 5] == b_text:
                if game_list[i + 10] == b_text:
                    if game_list[i + 15] == b_text:
                        Win('Blue Wins')
                        game_won = True
    for i in range(20):  # For loop logic to find horizontal win
        if i == 0 or i == 1 or i == 5 or i == 6 or i == 10 or i == 11 or i == 15 or i == 16:
            if game_list[i] == b_text:
                if game_list[i + 1] == b_text:
                    if game_list[i + 2] == b_text:
                        if game_list[i + 3] == b_text:
                            Win("Blue Wins")
                            game_won = True
    for i in range(5):  # For loop logic to find diagonal win
        if i == 0 or i == 1:  # Left side diagonal Blue
            if game_list[i] == b_text:
                if game_list[i + 6] == b_text:
                    if game_list[i + 12] == b_text:
                        if game_list[i + 18] == b_text:
                            Win("Blue Wins")
                            game_won = True
        if i == 3 or i == 4:  # Right side diagonal Blue
            if game_list[i] == b_text:
                if game_list[i + 4] == b_text:
                    if game_list[i + 8] == b_text:
                        if game_list[i + 12] == b_text:
                            Win("Blue Wins")
                            game_won = True
    for i in range(5):  # For loop logic to find a full vertical column
        if game_list[i] == r_text:
            if game_list[i + 5] == r_text:
                if game_list[i + 10] == r_text:
                    if game_list[i + 15] == r_text:
                        Win('Red Wins')
                        game_won = True
    for i in range(20):  # For loop logic to find horizontal win
        if i == 0 or i == 1 or i == 5 or i == 6 or i == 10 or i == 11 or i == 15 or i == 16:
            if game_list[i] == r_text:
                if game_list[i + 1] == r_text:
                    if game_list[i + 2] == r_text:
                        if game_list[i + 3] == r_text:
                            Win("Red Wins")
                            game_won = True
    for i in range(5):  # For loop logic to find diagonal win
        if i == 0 or i == 1:  # Left side diagonal Blue
            if game_list[i] == r_text:  # Left side diagonal Red
                if game_list[i + 6] == r_text:
                    if game_list[i + 12] == r_text:
                        if game_list[i + 18] == r_text:
                            Win("Red Wins")
                            game_won = True
        if i == 3 or i == 4:  # Right side diagonal Blue
            if game_list[i] == r_text:  # Right side diagonal Red
                if game_list[i + 4] == r_text:
                    if game_list[i + 8] == r_text:
                        if game_list[i + 12] == r_text:
                            Win("Red Wins")
                            game_won = True
    for i in range(20):  # Checks for a tie
        if game_list[i] == "B" or game_list[i] == "R":
            if game_won is False and i == 19:
                Win("Tie")
                game_won = True
        else:
            break


# Function To fill in button and give the player there tile
def FillButton(button_number, row):
    global game_list
    global button_list
    global player_turn
    global ai_mode
    global game_won
    if player_turn:  # If true it is reds/ AI's turn
        button_list[button_number + row].bg = "red"  # Change button color
        game_list.remove(button_number + row)  # Replace default number
        game_list.insert(button_number + row, r_text)
        player_turn = False  # swap turn
        button_list[button_number + row].enabled = False  # turn off button
    else:
        button_list[button_number + row].bg = "blue"  # Change button color
        game_list.remove(button_number + row)
        game_list.insert(button_number + row, b_text)
        button_list[button_number + row].enabled = False
        AiMove()
    CheckForWin()


# The function that finds a suitable move for the AI to make to counter or win the game
def AiMove():
    global game_list
    global player_turn
    global ai_mode
    global game_won
    global game_text
    if ai_mode and game_won is False:  # Check to see if the game isn't won or tied and if AI mode is on
        player_turn = True  # Change to reds turn
        turn_found = False  # boolean to see if a valid AI turn is found
        for i in range(5):  # For loop logic to win game on vertical 3 tile stack
            if turn_found:
                break
            if game_list[i] == i:
                if game_list[i + 5] == "R":
                    if game_list[i + 10] == "R":
                        if game_list[i + 15] == "R":
                            turn(i)
                            turn_found = True
                            player_turn = False
                            break
        # For loop logic to counter a 3 tile horizontal line
        for x in range(3):  # This for loop shifts between columns
            if turn_found:
                break
            for i in range(4):  # This for loop shifts between rows
                i = (i * 5) + x  # an equation to
                print(i)
                if game_list[i] == "B":  # Group of Nested if statements to see if 3 tiles are in a row
                    if game_list[i + 1] == "B":
                        if game_list[i + 2] == "B":
                            if x == 2:
                                if i - 3 < 0:
                                    pass
                                else:
                                    if game_list[i - 3] == i - 3:
                                        if i + 2 < len(game_list):
                                            if game_list[i + 2] == i + 2:  # Prevents AI from giving player a
                                                # platform to win
                                                pass
                                            else:
                                                turn(1)
                                                turn_found = True
                                                player_turn = False
                                                break
                                        elif game_list[16] == 16:
                                            turn(1)
                                            turn_found = True
                                            player_turn = False
                                            break
                            if i + 3 < len(game_list):
                                if game_list[i + 3] == i + 3:
                                    if i + 8 < len(game_list):
                                        if game_list[i + 8] == i + 8:
                                            pass
                                        else:
                                            turn(3 + x)
                                            turn_found = True
                                            player_turn = False
                                            break
                                    elif game_list[i + 3] == i + 3:
                                        turn(3 + x)
                                        turn_found = True
                                        player_turn = False
                                        break
        for i in range(5):  # For loop Logic to counter a 3 tile vertical line
            if turn_found:
                break
            if game_list[i] == i:
                if game_list[i + 5] == "B":
                    if game_list[i + 10] == "B":
                        if game_list[i + 15] == "B":
                            turn(i)
                            turn_found = True
                            player_turn = False
                            break
        if turn_found is False:  # if none of the counter moves are found the AI resorts to a random placement
            ai_turn = random.randint(0, 5)
            if game_list[ai_turn] == 'R' or game_list[ai_turn] == 'B':
                for i in range(5):
                    if game_list[i] == 'R' or game_list[i] == 'B':
                        pass
                    else:
                        ai_turn = i
            game_text.value = b_turn_text
            turn(ai_turn)
            player_turn = False
    else:
        player_turn = True


# This function is to create the gravity of connect four
def turn(button_number):
    global game_list
    global button_list
    global player_turn
    if game_list[button_number] == button_number:  # if top row is clear
        if button_number + 5 < len(game_list):  # Checks if this is a valid list index
            if game_list[button_number + 5] == button_number + 5:  # checks row 2 clear
                if button_number + 10 < len(game_list):  # Checks if this is a valid list index
                    if game_list[button_number + 10] == button_number + 10:  # checks if row 3 is clear
                        if button_number + 15 < len(game_list):  # Checks if this is a valid list index
                            if game_list[button_number + 15] == button_number + 15:  # checks if row 4 is clear
                                FillButton(button_number, 15)  # FILL ROW 4
                            else:
                                FillButton(button_number, 10)  # FILL ROW 3
                        else:
                            FillButton(button_number, 10)  # FILL ROW 3
                    else:
                        FillButton(button_number, 5)  # FILL ROW 2
                else:
                    FillButton(button_number, 5)  # FILL ROW 2
            else:
                FillButton(button_number, 0)  # FILL ROW 1
        else:
            FillButton(button_number, 0)  # FILL ROW 1
    print(game_list, "GAME LIST")


# Function that is called when a player wins
def Win(player):
    global game_text
    global win
    global loss
    global tie
    global win_rate_text
    global win_rate
    global game_won
    if game_won is False:
        game_won = True
        if player == "Blue Wins":
            win = win + 1
        elif player == "Tie":
            tie = tie + 1
        elif player == "Red Wins":
            loss = loss + 1
        win_rate_text.format(win, tie, loss)
        print(win, loss, tie)
        print(win_rate_text)
        for i in button_list:
            i.enabled = False
        win_rate.value = "{} - {} - {}".format(win, tie, loss)
        game_text.value = player


# Function to Reset the game
def ResetGame():
    global game_list
    global player_turn
    global game_won
    game_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    player_turn = False
    game_won = False
    stop_value = 0
    game_text.value = b_turn_text
    for i in button_list:  # Resets the button's color and enables them
        i.enabled = True
        i.bg = 'white'


def SwapMode():
    global ai_mode
    global swap_text
    global Swap_button
    if ai_mode:
        ai_mode = False
        Swap_button.text = swap_text_ai
    else:
        ai_mode = True
        Swap_button.text = swap_text_player
    ResetGame()


# All the buttons
button1 = PushButton(app, text=n_text, align="left", grid=[0, 0], width=10, height=4, command=turn, args=[0])
button2 = PushButton(app, text=n_text, align="left", grid=[1, 0], width=10, height=4, command=turn, args=[1])
button3 = PushButton(app, text=n_text, align="left", grid=[2, 0], width=10, height=4, command=turn, args=[2])
button4 = PushButton(app, text=n_text, align="left", grid=[3, 0], width=10, height=4, command=turn, args=[3])
button5 = PushButton(app, text=n_text, align="left", grid=[4, 0], width=10, height=4, command=turn, args=[4])
button6 = PushButton(app, text=n_text, align="left", grid=[0, 1], width=10, height=4, command=turn, args=[5])
button7 = PushButton(app, text=n_text, align="left", grid=[1, 1], width=10, height=4, command=turn, args=[6])
button8 = PushButton(app, text=n_text, align="left", grid=[2, 1], width=10, height=4, command=turn, args=[7])
button9 = PushButton(app, text=n_text, align="left", grid=[3, 1], width=10, height=4, command=turn, args=[8])
button10 = PushButton(app, text=n_text, align="left", grid=[4, 1], width=10, height=4, command=turn, args=[9])
button11 = PushButton(app, text=n_text, align="left", grid=[0, 2], width=10, height=4, command=turn, args=[10])
button12 = PushButton(app, text=n_text, align="left", grid=[1, 2], width=10, height=4, command=turn, args=[11])
button13 = PushButton(app, text=n_text, align="left", grid=[2, 2], width=10, height=4, command=turn, args=[12])
button14 = PushButton(app, text=n_text, align="left", grid=[3, 2], width=10, height=4, command=turn, args=[13])
button15 = PushButton(app, text=n_text, align="left", grid=[4, 2], width=10, height=4, command=turn, args=[14])
button16 = PushButton(app, text=n_text, align="left", grid=[0, 3], width=10, height=4, command=turn, args=[15])
button17 = PushButton(app, text=n_text, align="left", grid=[1, 3], width=10, height=4, command=turn, args=[16])
button18 = PushButton(app, text=n_text, align="left", grid=[2, 3], width=10, height=4, command=turn, args=[17])
button19 = PushButton(app, text=n_text, align="left", grid=[3, 3], width=10, height=4, command=turn, args=[18])
button20 = PushButton(app, text=n_text, align="left", grid=[4, 3], width=10, height=4, command=turn, args=[19])

# The button to reset the game
reset_button = PushButton(app, text="Reset", align="left", grid=[2, 4], width=10, height=4, command=ResetGame)

Swap_button = PushButton(app, text=swap_text, align="left", grid=[0, 4], width=10, height=4, command=SwapMode)

# The text to indicate winner, tie, and who's turn it is
game_text = Text(app, text="It's Blues turn", grid=[2, 5])

win_rate = Text(app, text=win_rate_text, grid=[4, 5])

info_text = Text(app, text="Welcome to Connect 4!", align="left", grid=[5, 0])
info_text_1 = Text(app, text="The Rules are simple, Connect 4 tiles in a\nrow Horizontally, Vertically, Or Diagonally",
                   align="left", grid=[5, 1])
info_text_2 = Text(app, text="Play against a friend, or the  \nnew custom Connect 4 AI,    \nwho can counter your moves"
                   , align="left", grid=[5, 2])

info_text_3 = Text(app, text="To reset the game, click the 'Reset' button\nat the bottom center of the board.\n"
                             "To toggle between modes click the button\nat the bottom left corner of the board."
                   , align="left", grid=[5, 3])

# A list containing all buttons
button_list = [button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11,
               button12, button13, button14, button15, button16, button17, button18, button19, button20]


def main():
    for i in button_list:  # Change all the buttons color to white
        i.bg = 'white'
    app.display()


if __name__ == '__main__':
    main()
