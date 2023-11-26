#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Function for the Heads and Tails game
def heads_and_tails():
    print("Welcome to Heads and Tails game")
    
    # User input for choosing heads or tails
    user_input = input("Heads or Tails: ")
    
    # Valid inputs for the game
    valid_input = ["heads", "tails"]
    print("You chose", user_input)
    
    # Check if user input is valid
    if user_input not in valid_input:
        print("Please enter valid input")
    else:
        print("Let's toss the coin")
        import random
        
        # Randomly choose 'h' for heads or 't' for tails
        if random.choice("ht") == "h":
            coin_result = "heads"
        else:
            coin_result = "tails"
        
        print("Coin Result is", coin_result)
        
        # Check if user wins or loses
        if user_input == coin_result:
            print("You Win")
        else:
            print("You Lose")

# Function for the dice game
def dicegame():
    print('Welcome to the dice game') 
    
    # User input for choosing a number (1-6)
    user_input = int(input('Enter your choice (1, 2, 3, 4, 5, 6):'))
    print('Display:', user_input)
    
    # Dice roll
    import random  
    dice_result = str(random.choice([1, 2, 3, 4, 5, 6]))
    print('Dice result:', dice_result)     
   
    # Check if user wins or loses
    if user_input == dice_result:
        print('You win')
    else:
        print('You lose the game')

# Function for the cube game
def cubegame():
    # Welcome message
    num = int(input('Enter any number:'))
    print('Cubic number:', num) 
    
    # Calculate the cube of the number
    for i in range(num): 
        cubes = num ** 3
    
    print('The cube of the number is:', cubes)

# Import the tkinter module for GUI
import tkinter

# Main window configuration
window = tkinter.Tk()
window.geometry("500x500")
window.title("Python Project - SHARAYU")

# Labels for the GUI
lab = tkinter.Label(window, text='PYTHON PROJECT', font=("Arabic", 18))
lab.place(x=135, y=35)

lab1 = tkinter.Label(window, text='Made by SHARAYU', font=("Arabic", 14))
lab1.place(x=185, y=70)

# Buttons for different games
key = tkinter.Button(window, text="Heads and Tails", height=3, width=18, command=heads_and_tails)
key.place(x=190, y=120)

key2 = tkinter.Button(window, text="Dice", height=3, width=18, command=dicegame)
key2.place(x=190, y=200)

key3 = tkinter.Button(window, text="Cubes", height=3, width=18, command=cubegame)
key3.place(x=190, y=280)

# Main loop to run the GUI
window.mainloop()


# In[ ]:




