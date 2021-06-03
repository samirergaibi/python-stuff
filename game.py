import random
from enum import Enum

class Actions(Enum):
  ROCK = 'rock'
  PAPER = 'paper'
  SCISSOR = 'scissor'

actions_list = [Actions.ROCK, Actions.PAPER, Actions.SCISSOR]

class Results(Enum):
  PLAYER = 'You win 🎈'
  COMPUTER = 'Computer wins ❌'
  NONE = 'No winner 🤷'

def computer_action():
  return actions_list[random.randint(0, 2)]

def find_victor(player_choice, computer_choice):
  if player_choice == computer_choice:
    return Results.NONE

  if player_choice == Actions.ROCK:
    if computer_choice == Actions.PAPER:
      return Results.COMPUTER
  if player_choice == Actions.PAPER:
    if computer_choice == Actions.SCISSOR:
      return Results.COMPUTER
  if player_choice == Actions.SCISSOR:
    if computer_choice == Actions.ROCK:
      return Results.COMPUTER
  
  return Results.PLAYER


def find_player_choice(input):
  if input == 'r' or input == 'rock':
    return Actions.ROCK
  elif input == 'p' or input == 'paper':
    return Actions.PAPER
  elif input == 's' or input == 'scissor':
    return Actions.SCISSOR
  else:
    raise Exception("Invalid player choice")

player_score = 0
computer_score = 0

def handle_score(winner):
  global player_score
  global computer_score
  if winner == Results.PLAYER:
    player_score += 1
  elif winner == Results.COMPUTER:
    computer_score += 1
  else:
    return

def end_game_print():
  if player_score == 3:
    print('You won, Congratulations! 🎈 🥳 👑')
  else:
    print('You lost, better luck next time 😢')

def start_game():
  print("Let's play a game... of 🤘 🧻 ✂ !")
  while player_score < 3 and computer_score < 3:
    print('----------------------------')
    player_input = input('Make your choice:\nrock (r)\npaper (p)\nscissor (s)\n')
    player_choice = find_player_choice(player_input)
    computer_choice = computer_action()
    winner = find_victor(player_choice, computer_choice)
    handle_score(winner)
    
    print('----------------------------')
    print('Choices and result:')
    print('🧑 (player) : ', player_choice.value)
    print('🤖 (bot) : ', computer_choice.value)
    print('👑 (result): ', f' 🧑 {player_score} - {computer_score} 🤖')
  
  end_game_print()
    
start_game()