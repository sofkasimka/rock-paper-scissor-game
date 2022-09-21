human_turn = 'rock'
computer_turn = 'scissors'

if human_turn == 'rock' and computer_turn == 'scissors':
    print('human wins!')
if human_turn == 'paper' and computer_turn == 'rock':
    print('human wins!')
if human_turn == 'scissors' and computer_turn == 'paper':
    print('human wins!')
if human_turn == 'rock' and computer_turn == 'paper':
    print('computer wins!')
if human_turn == 'paper' and computer_turn == 'scissors':
    print('computer wins!')
if human_turn == 'scissors' and computer_turn == 'rock':
    print('computer wins!')
if human_turn == 'rock' and computer_turn == 'rock':
    print('draw!')
if human_turn == 'paper' and computer_turn == 'paper':
    print('draw!')
if human_turn == 'scissors' and computer_turn == 'scissors':
    print('draw!')
