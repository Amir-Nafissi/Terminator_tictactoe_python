#importing random:
from random import choice

# Importing the turtle module:
from turtle import *
from turtle import _CFG  # this dictionary to be imported separately

#inputs and prints:
print("Quick!")
print("A robot has escaped Mr. Miniou's Quantum Artificial Intelligence Laboratory! You have successfully been able to corner him, but he has now challenged you to a game of Tic Tac Toe. If you win, he will go back to the labratory. But if he wins, or it's a tie, he gets to escape and use his intelligence to take over the world!")
print(" ")
print("Draw a circle in the box you want by entering its number")
print(" ")
print("You only have one try! One wrong move and it's over!")
print(" ")
print("The robot is letting you go first!")

# Resizes the default canvas size to prevent scrollbars
_CFG["canvwidth"] = 1 
_CFG["canvheight"] = 1

# Creates the grid and size 600 by 600 and title:
setup(600, 600)
bgpic("Tic-tac-toe-robot-white-backrground.png")
title("Tic Tac Toe - Amir Nafissi")

#player settings:
player = Turtle()
player.shape("turtle")
player.speed(4)
player.color("green")
player.penup()
player.pensize(10)

#bot settings:
bot = Turtle()
bot.speed(10)
bot.shape("arrow")
bot.color("blue")
bot.pensize(10)
bot.penup()

#game over checker:
game_over = False
game_over_player_won = False

#checking if a box has been marked: 
#it will change to a 1 if the bot has marked it, or 2 if the player has marked it
box1_checker = 0
box2_checker = 0
box3_checker = 0
box4_checker = 0
box5_checker = 0
box6_checker = 0
box7_checker = 0
box8_checker = 0
box9_checker = 0


#-------------------Game Mechanics:-----------------------
#function for making a circle:
def player_make_circle():
  """makes a circle
  """
  player.pendown()
  player.circle(40)
  player.penup()

#function for making a X:
def bot_make_x():
  """bot makes an x from its centre
  """
  bot.pendown()
  bot.left(45)
  for i in range(4):
    bot.left(90)
    bot.forward(50)
    bot.backward(50)
  bot.left(45)
  bot.penup()

#movement for player:
def box_player_1():
  """moves player to box 1
  """
  player.penup()
  player.goto(-200,150)

def box_player_2():
  """moves player to box 2
  """
  player.penup()
  player.goto(0,150)

def box_player_3():
  """moves player to box 3
  """
  player.penup()
  player.goto(200,150)

def box_player_4():
  """moves player to box 4
  """
  player.penup()
  player.goto(-200,-50)

def box_player_5():
  """moves player to box 5
  """
  player.penup()
  player.goto(0,-50)

def box_player_6():
  """moves player to box 6
  """
  player.penup()
  player.goto(200,-50)

def box_player_7():
  """moves player to box 7
  """
  player.penup()
  player.goto(-200,-250)

def box_player_8():
  """moves player to box 8
  """
  player.penup()
  player.goto(0,-250)

def box_player_9():
  """moves player to box 9
  """
  player.penup()
  player.goto(200,-250)

#movement for bot:
def box_bot_1():
  """moves bot to box 1
  """
  bot.penup()
  bot.goto(-200,200)

def box_bot_2():
  """moves bot to box 2
  """
  bot.penup()
  bot.goto(0,200)

def box_bot_3():
  """moves bot to box 3
  """
  bot.penup()
  bot.goto(200,200)

def box_bot_4():
  """moves bot to box 4
  """
  bot.penup()
  bot.goto(-200,0)

def box_bot_5():
  """moves bot to box 5
  """
  bot.penup()
  bot.goto(0,0)

def box_bot_6():
  """moves bot to box 6
  """
  bot.penup()
  bot.goto(200,0)

def box_bot_7():
  """moves bot to box 7
  """
  bot.penup()
  bot.goto(-200,-200)

def box_bot_8():
  """moves bot to box 8
  """
  bot.penup()
  bot.goto(0, -200)

def box_bot_9():
  """moves bot to box 9
  """
  bot.penup()
  bot.goto(200,-200)

#input for player to move:
def player_inputs_and_movement():
  """takes input from player 1,2,3,4,5,6,7,8,9 and draws a circle in the corresponding box
  """
  global box1_checker
  global box2_checker
  global box3_checker
  global box4_checker
  global box5_checker
  global box6_checker
  global box7_checker
  global box8_checker
  global box9_checker

  while True:
    move = input("Make your move: ")
    if move.isdigit():
      if move == "1":
        box1_checker += 2
        box_player_1()
        player_make_circle()
        break
        return
      elif move == "2":
        box2_checker += 2
        box_player_2()
        player_make_circle()
        break
        return
      elif move == "3":
        box3_checker += 2
        box_player_3()
        player_make_circle()
        break
        return
      elif move == "4":
        box4_checker += 2
        box_player_4()
        player_make_circle()
        break
        return
      elif move == "5":
        box5_checker += 2
        box_player_5()
        player_make_circle()
        break
        return
      elif move == "6":
        box6_checker += 2
        box_player_6()
        player_make_circle()
        break
        return
      elif move == "7":
        box7_checker += 2
        box_player_7()
        player_make_circle()
        break
        return
      elif move == "8":
        box8_checker += 2
        box_player_8()
        player_make_circle()
        break
        return
      elif move == "9":
        box9_checker += 2
        box_player_9()
        player_make_circle()
        break
        return
      else:
        print("Wrong input, do you think this is a joke?")
    else:
        print("Wrong input, do you think this is a joke?")

#bot picking random location to place the x:
def bot_box_movement():
  """picks a rondom free box, moves the bot to that box, and then draws an x
  """
  global bot_box_list

  global game_over
  
  global box1_checker
  global box2_checker
  global box3_checker
  global box4_checker
  global box5_checker
  global box6_checker
  global box7_checker
  global box8_checker
  global box9_checker

  #puting free boxes in a list for the bot to choose from:
  bot_box_list = ["prevent empty string error"]
  
  for i in range (10):
    if box1_checker == 0:
      bot_box_list.append("bot box 1")
    if box2_checker == 0:
      bot_box_list.append("bot box 2")
    if box3_checker == 0:
      bot_box_list.append("bot box 3")
    if box4_checker == 0:
      bot_box_list.append("bot box 4")
    if box5_checker == 0:
      bot_box_list.append("bot box 5")
    if box6_checker == 0:
      bot_box_list.append("bot box 6")
    if box7_checker == 0:
      bot_box_list.append("bot box 7")
    if box8_checker == 0:
      bot_box_list.append("bot box 8")
    if box9_checker == 0:
      bot_box_list.append("bot box 9")

  bot_box_choice = choice(bot_box_list) 

  if bot_box_choice == "prevent empty string error":
    pass
  elif bot_box_choice == "bot box 1":
    box_bot_1()
    bot_make_x()
    box1_checker = 1
    bot_box_list.remove("bot box 1")
  elif bot_box_choice == "bot box 2":
    box_bot_2()
    bot_make_x()
    box2_checker = 1
    bot_box_list.remove("bot box 2")
  elif bot_box_choice == "bot box 3":
    box_bot_3()
    bot_make_x()
    box3_checker = 1
    bot_box_list.remove("bot box 3")
  elif bot_box_choice == "bot box 4":
    box_bot_4()
    bot_make_x()
    box4_checker = 1
    bot_box_list.remove("bot box 4")
  elif bot_box_choice == "bot box 5":
    box_bot_5()
    bot_make_x()
    box5_checker = 1
    bot_box_list.remove("bot box 5")
  elif bot_box_choice == "bot box 6":
    box_bot_6()
    bot_make_x()
    box6_checker = 1
    bot_box_list.remove("bot box 6")
  elif bot_box_choice == "bot box 7":
    box_bot_7()
    bot_make_x()
    box7_checker = 1
    bot_box_list.remove("bot box 7")
  elif bot_box_choice == "bot box 8":
    box_bot_8() 
    bot_make_x()
    box8_checker = 1
    bot_box_list.remove("bot box 8")
  elif bot_box_choice == "bot box 9":
    box_bot_9() 
    bot_make_x()
    box9_checker = 1
    bot_box_list.remove("bot box 9")


#checking if player won:
def check_player_won():
  """goes through all possible combinations for the player to win, if true, it ends the game"""
  
  global game_over_player_won
  
  global box1_checker
  global box2_checker
  global box3_checker
  global box4_checker
  global box5_checker
  global box6_checker
  global box7_checker
  global box8_checker
  global box9_checker
  
  for i in range(9):
    if box1_checker == 2 and box2_checker == 2 and box3_checker == 2: #row 1
      game_over_player_won = True
      
    elif box4_checker == 2 and box5_checker == 2 and box6_checker == 2: #row 2
      game_over_player_won = True
    elif box7_checker == 2 and box8_checker == 2 and box9_checker == 2: #row 3
      game_over_player_won = True
    elif box1_checker == 2 and box4_checker == 2 and box7_checker == 2: #column 1
      game_over_player_won = True
      
    elif box2_checker == 2 and box5_checker == 2 and box8_checker == 2: #column 2
      game_over_player_won = True
    elif box3_checker == 2 and box6_checker == 2 and box9_checker == 2: #column 3
      game_over_player_won = True
    elif box1_checker == 2 and box5_checker == 2 and box9_checker == 2: #diagonal 1
      game_over_player_won = True
    elif box3_checker == 2 and box5_checker == 2 and box7_checker == 2: #diagonal 2
      game_over_player_won = True
      

#checking if the bot won:
def check_bot_won():
  """goes through all possible combinations for the bot to win, if true, it ends the game"""
  global game_over
  
  global box1_checker
  global box2_checker
  global box3_checker
  global box4_checker
  global box5_checker
  global box6_checker
  global box7_checker
  global box8_checker
  global box9_checker
  
  for i in range(9):
    if box1_checker == 1 and box2_checker == 1 and box3_checker == 1: #row 1
      game_over = True
    elif box4_checker == 1 and box5_checker == 1 and box6_checker == 1: #row 2
      game_over = True
    elif box7_checker == 1 and box8_checker == 1 and box9_checker == 1: #row 3
      game_over = True
    elif box1_checker == 1 and box4_checker == 1 and box7_checker == 1: #column 1
      game_over = True
    elif box2_checker == 1 and box5_checker == 1 and box8_checker == 1: #column 2
      game_over = True
    elif box3_checker == 1 and box6_checker == 1 and box9_checker == 1: #column 3
      game_over = True
    elif box1_checker == 1 and box5_checker == 1 and box9_checker == 1: #diagonal 1
      game_over = True
    elif box3_checker == 1 and box5_checker == 1 and box7_checker == 1: #diagonal 2
      game_over = True

did_bot_counter = False #will be used to check if the bot used up a turn to counter the players movement or not

#checking if the player is about to win, and then countering it:
def bot_stopping_player():
  """checks if the player will win next round and if true bot puts an x to prevent the player from moving
  """
  
  global game_over

  global did_bot_counter
  
  global box1_checker
  global box2_checker
  global box3_checker
  global box4_checker
  global box5_checker
  global box6_checker
  global box7_checker
  global box8_checker
  global box9_checker
  
  for row_1 in range (1): #a for loop will be used for organization
    if box1_checker == 0 and box2_checker == 2 and box3_checker == 2:
      box_bot_1()
      bot_make_x()
      box1_checker = 1
      did_bot_counter = True
      return
    elif box1_checker == 2 and box2_checker == 0 and box3_checker == 2:
      box_bot_2()
      bot_make_x()
      box2_checker = 1
      did_bot_counter = True
      return
    elif box1_checker == 2 and box2_checker == 2 and box3_checker == 0:
      box_bot_3()
      bot_make_x()
      box3_checker = 1
      did_bot_counter = True
      return
  
  for row_2 in range (1):
    if box4_checker == 0 and box5_checker == 2 and box6_checker == 2:
      box_bot_4()
      bot_make_x()
      box4_checker = 1
      did_bot_counter = True
      return
    elif box4_checker == 2 and box5_checker == 0 and box6_checker == 2:
      box_bot_5()
      bot_make_x()
      box5_checker = 1
      did_bot_counter = True
      return
    elif box4_checker == 2 and box5_checker == 2 and box6_checker == 0:
      box_bot_6()
      bot_make_x()
      box6_checker = 1
      did_bot_counter = True
      return

  for row_3 in range (1):
    if box7_checker == 0 and box8_checker == 2 and box9_checker == 2:
      box_bot_7()
      bot_make_x()
      box7_checker = 1
      did_bot_counter = True
      return
    elif box7_checker == 2 and box8_checker == 0 and box9_checker == 2:
      box_bot_8()
      bot_make_x()
      box8_checker = 1
      did_bot_counter = True
      return
    elif box7_checker == 2 and box8_checker == 2 and box9_checker == 0:
      box_bot_9()
      bot_make_x()
      box9_checker = 1
      did_bot_counter = True
      return
      
  for column_1 in range (1):
    if box1_checker == 0 and box4_checker == 2 and box7_checker == 2:
      box_bot_1()
      bot_make_x()
      box1_checker = 1
      did_bot_counter = True
      return
    elif box1_checker == 2 and box4_checker == 0 and box7_checker == 2:
      box_bot_4()
      bot_make_x()
      box4_checker = 1
      did_bot_counter = True
      return
    elif box1_checker == 2 and box4_checker == 2 and box7_checker == 0:
      box_bot_7()
      bot_make_x()
      box7_checker = 1
      did_bot_counter = True
      return
      
  for column_2 in range (1):
    if box2_checker == 0 and box5_checker == 2 and box8_checker == 2:
      box_bot_2()
      bot_make_x()
      box2_checker = 1
      did_bot_counter = True
      return
    elif box2_checker == 2 and box5_checker == 0 and box8_checker == 2:
      box_bot_5()
      bot_make_x()
      box5_checker = 1
      did_bot_counter = True
      return
    elif box2_checker == 2 and box5_checker == 2 and box8_checker == 0:
      box_bot_8()
      bot_make_x()
      box8_checker = 1
      did_bot_counter = True
      return
      
  for column_3 in range (1):
    if box3_checker == 0 and box6_checker == 2 and box9_checker == 2:
      box_bot_3()
      bot_make_x()
      box3_checker = 1
      did_bot_counter = True
      return
    elif box3_checker == 2 and box6_checker == 0 and box9_checker == 2:
      box_bot_6()
      bot_make_x()
      box6_checker = 1
      did_bot_counter = True
      return
    elif box3_checker == 2 and box6_checker == 2 and box9_checker == 0:
      box_bot_9()
      bot_make_x()
      box9_checker = 1
      did_bot_counter = True
      return
      
  for diagonal_1 in range (1):
    if box1_checker == 0 and box5_checker == 2 and box9_checker == 2:
      box_bot_1()
      bot_make_x()
      box1_checker = 1
      did_bot_counter = True
      return
    elif box1_checker == 2 and box5_checker == 0 and box9_checker == 2:
      box_bot_5()
      bot_make_x()
      box5_checker = 1
      did_bot_counter = True
      return
    elif box1_checker == 2 and box5_checker == 2 and box9_checker == 0:
      box_bot_9()
      bot_make_x()
      box9_checker = 1
      did_bot_counter = True
      return
      
  for diagonal_2 in range (1):
    if box3_checker == 0 and box5_checker == 2 and box7_checker == 2:
      box_bot_3()
      bot_make_x()
      box3_checker = 1
      did_bot_counter = True
      return
    elif box3_checker == 2 and box5_checker == 0 and box7_checker == 2:
      box_bot_5()
      bot_make_x()
      box5_checker = 1
      did_bot_counter = True
      return
    elif box3_checker == 2 and box5_checker == 2 and box7_checker == 0:
      box_bot_7()
      bot_make_x()
      box7_checker = 1
      did_bot_counter = True
      return
    
  if did_bot_counter == False: #if the bot did not use up turn for countering the player, then pick a random spot 
    bot_box_movement()
      
#checking if the bot can win:
def checking_if_bot_can_win():
  """checks if the bot can win next round and if true bot puts an x to win, if not bot will check if it can stop the player from winning and if not it will place x somewhere random
  """
  
  global game_over

  global did_bot_counter
  did_bot_counter = True #changes it so we can use another function if the bot can't win
  
  global box1_checker
  global box2_checker
  global box3_checker
  global box4_checker
  global box5_checker
  global box6_checker
  global box7_checker
  global box8_checker
  global box9_checker



  for row_1 in range (1):  #a for loop will be used for organization
    if box1_checker == 0 and box2_checker == 1 and box3_checker == 1:
      box_bot_1()
      bot_make_x()
      box1_checker = 1
      game_over = True
      return
    elif box1_checker ==1 and box2_checker == 0 and box3_checker ==1:
      box_bot_2()
      bot_make_x()
      box2_checker = 1
      game_over = True
      return
    elif box1_checker ==1 and box2_checker ==1 and box3_checker == 0:
      box_bot_3()
      bot_make_x()
      box3_checker = 1
      game_over = True
      return
    else:
      did_bot_counter = False

  
  for row_2 in range (1):
    if box4_checker == 0 and box5_checker ==1 and box6_checker ==1:
      box_bot_4()
      bot_make_x()
      box4_checker = 1
      game_over = True
      return
    elif box4_checker ==1 and box5_checker == 0 and box6_checker ==1:
      box_bot_5()
      bot_make_x()
      box5_checker = 1
      game_over = True
      return
    elif box4_checker ==1 and box5_checker ==1 and box6_checker == 0:
      box_bot_6()
      bot_make_x()
      box6_checker = 1
      game_over = True
      return
    else:
      did_bot_counter = False

  
  for row_3 in range (1):
    if box7_checker == 0 and box8_checker ==1 and box9_checker ==1:
      box_bot_7()
      bot_make_x()
      box7_checker = 1
      game_over = True
      return
    elif box7_checker ==1 and box8_checker == 0 and box9_checker ==1:
      box_bot_8()
      bot_make_x()
      box8_checker = 1
      game_over = True
      return
    elif box7_checker ==1 and box8_checker ==1 and box9_checker == 0:
      box_bot_9()
      bot_make_x()
      box9_checker = 1
      game_over = True
      return
    else:
      did_bot_counter = False

  
  for column_1 in range (1):
    if box1_checker == 0 and box4_checker ==1 and box7_checker ==1:
      box_bot_1()
      bot_make_x()
      box1_checker = 1
      game_over = True
      return
    elif box1_checker ==1 and box4_checker == 0 and box7_checker ==1:
      box_bot_4()
      bot_make_x()
      box4_checker = 1
      game_over = True
      return
    elif box1_checker ==1 and box4_checker ==1 and box7_checker == 0:
      box_bot_7()
      bot_make_x()
      box7_checker = 1
      game_over = True
      return
    else:
      did_bot_counter = False

  
  for column_2 in range (1):
    if box2_checker == 0 and box5_checker ==1 and box8_checker ==1:
      box_bot_2()
      bot_make_x()
      box2_checker = 1
      game_over = True
      return
    elif box2_checker ==1 and box5_checker == 0 and box8_checker ==1:
      box_bot_5()
      bot_make_x()
      box5_checker = 1
      game_over = True
      return
    elif box2_checker ==1 and box5_checker ==1 and box8_checker == 0:
      box_bot_8()
      bot_make_x()
      box8_checker = 1
      game_over = True
      return
    else:
      did_bot_counter = False

  
  for column_3 in range (1):
    if box3_checker == 0 and box6_checker ==1 and box9_checker ==1:
      box_bot_3()
      bot_make_x()
      box3_checker = 1
      game_over = True
      return
    elif box3_checker ==1 and box6_checker == 0 and box9_checker ==1:
      box_bot_6()
      bot_make_x()
      box6_checker = 1
      game_over = True
      return
    elif box3_checker ==1 and box6_checker ==1 and box9_checker == 0:
      box_bot_9()
      bot_make_x()
      box9_checker = 1
      game_over = True
      return
    else:
      did_bot_counter = False
      
      
  for diagonal_1 in range (1):
    if box1_checker == 0 and box5_checker ==1 and box9_checker ==1:
      box_bot_1()
      bot_make_x()
      box1_checker = 1
      game_over = True
      return
    elif box1_checker ==1 and box5_checker == 0 and box9_checker ==1:
      box_bot_5()
      bot_make_x()
      box5_checker = 1
      game_over = True
      return
    elif box1_checker ==1 and box5_checker ==1 and box9_checker == 0:
      box_bot_9()
      bot_make_x()
      box9_checker = 1
      game_over = True
      return
    else:
      did_bot_counter = False
      
      
  for diagonal_2 in range (1):
    if box3_checker == 0 and box5_checker ==1 and box7_checker ==1:
      box_bot_3()
      bot_make_x()
      box3_checker = 1
      game_over = True
      return
    elif box3_checker ==1 and box5_checker == 0 and box7_checker ==1:
      box_bot_5()
      bot_make_x()
      box5_checker = 1
      game_over = True
      return
    elif box3_checker ==1 and box5_checker ==1 and box7_checker == 0:
      box_bot_7()
      bot_make_x()
      box7_checker = 1
      game_over = True
      return
    else:
      did_bot_counter = False
      
  if did_bot_counter == False:
    bot_stopping_player()


#checking if a tie happened:
def tie_checker():
  """checks if a tie has occurred
  """
  global game_over
  
  global box1_checker
  global box2_checker
  global box3_checker
  global box4_checker
  global box5_checker
  global box6_checker
  global box7_checker
  global box8_checker
  global box9_checker

  if box1_checker != 0 and box2_checker != 0 and box3_checker != 0 and box4_checker != 0 and box5_checker != 0 and box6_checker != 0 and box7_checker != 0 and box8_checker != 0 and box9_checker != 0: 
    game_over = True

#checking if player made a mistake:
def check_player_mistake():
  global game_over
  
  global box1_checker
  global box2_checker
  global box3_checker
  global box4_checker
  global box5_checker
  global box6_checker
  global box7_checker
  global box8_checker
  global box9_checker

  if box1_checker >= 3:
    game_over = True  
  elif box2_checker >= 3:
    game_over = True
  elif box3_checker >= 3:
    game_over = True
  elif box4_checker >= 3:
    game_over = True 
  elif box5_checker >= 3:
    game_over = True
  elif box6_checker >= 3:
    game_over = True
  elif box7_checker >= 3: 
    game_over = True
  elif box8_checker >= 3:
    game_over = True
  elif box9_checker >= 3: 
    game_over = True
  else:
    return


#----------------The game structure:---------------------
for i in range (9): #only 9 boxes, so repeats 9 times
  print(bot_box_movement)
  
  player_inputs_and_movement()
  check_player_mistake()
  if game_over == True:
    clearscreen()
    bgpic("Tic-tac-toe- you lose screen.png")
    break
  check_player_won()
  if game_over_player_won == True:
    clearscreen()
    bgpic("Tic-tac-toe-you win screen.png")
    break

  
  checking_if_bot_can_win()
  check_bot_won()
  tie_checker()
  if game_over == True:
    clearscreen()
    bgpic("Tic-tac-toe- you lose screen.png")
    break


# Keeps the program running after the drawing is complete
done()