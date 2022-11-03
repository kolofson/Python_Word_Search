import string
import random
from datetime import datetime
import tkinter.messagebox
from tkinter.simpledialog import askstring


def display_new_game():
   create_new_game()
   for i in range(len(game_board)):
       for j in range(len(game_board[i])):
           print(game_board[i][j], end='')
       print()


def create_new_game():
   for i in range(len(game_board)):
       for j in range(len(game_board[i])):
           game_board[i][j] = random.choice(alphabet)

   # Keep Track of angles
   angles = []
   # Display 3 words
   words = 0
   while words < 3:
       # Add Words to Board
       x = random.randint(0, 2)
       if x in angles:
           continue
       angles.append(x)
       words += 1
       # First row across
       if x == 0:
           word = random.randint(0, len(answer_key) - 1)
           for i in range(len(answer_key[word])):
               start = i + 1
               game_board[0][start] = answer_key[word][i]
           continue
       # Down first column
       if x == 1:
           word = random.randint(0, len(answer_key) - 1)
           for i in range(len(answer_key[word])):
               game_board[i][0] = answer_key[word][i]
           continue
       # Diagonal from top left
       if x == 2:
           word = random.randint(0, len(answer_key) - 1)
           for i in range(len(answer_key[word])):
               game_board[i+1][i+1] = answer_key[word][i]
           continue


alphabet = string.ascii_letters.upper()
game_words = ["happy", "sugar", "drink", "paper", "mouse", "timer", "avoid"]
answer_key = [['H', 'A', 'P', 'P', 'Y'],
             ['S', 'U', 'G', 'A', 'R'],
             ['D', 'R', 'I', 'N', 'K'],
             ['P', 'A', 'P', 'E', 'R'],
             ['M', 'O', 'U', 'S', 'E'],
             ['T', 'I', 'M', 'E', 'R'],
             ['A', 'V', 'O', 'I', 'D']]

game_board = [['', '', '', '', '', '', '', '', ''],
             ['', '', '', '', '', '', '', '', ''],
             ['', '', '', '', '', '', '', '', ''],
             ['', '', '', '', '', '', '', '', ''],
             ['', '', '', '', '', '', '', '', ''],
             ['', '', '', '', '', '', '', '', '']]

# Create new word search game
display_new_game()
start_time = datetime.now()
start_time = start_time.strftime("%H:%M:%S")
start_minute = start_time[3:5]
start_seconds = start_time[6:8]

# Player
player_words = []
while len(player_words) < 3:
   player_answer = askstring("Answer", "Enter a word you found: ").lower()
   # Check entered word
   if player_answer in player_words:
       tkinter.messagebox.showinfo("Game Response", "You already entered that word!")
   elif player_answer in game_words:
       tkinter.messagebox.showinfo("Game Response", "You found a word, good job!")
       player_words.append(player_answer)
   else:
       tkinter.messagebox.showinfo("Game Response", "Sorry, that's not a word in the game!")

# Get end time
end_time = datetime.now()
end_time = end_time.strftime("%H:%M:%S")
end_minute = end_time[3:5]
end_seconds = end_time[6:8]
tkinter.messagebox.showinfo("Game Over", "Congratulations, you found all the words in the word search!")
# Calculate time it took

total_mins = int(end_minute) - int(start_minute)
total_secs = int(end_seconds) - int(start_seconds)
total_mins = str(total_mins)
total_secs = str(total_secs)
tkinter.messagebox.showinfo("Total Time Consumed", "Time taken to solve puzzle: " + total_mins + ":" + total_secs)



