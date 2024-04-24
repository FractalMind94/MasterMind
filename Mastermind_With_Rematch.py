# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 10:49:10 2024

@author: KOM
"""

import random
# farver
colours =  [ "red", "blue", "green", "yellow", "white", "black" ]        


   
def input_main_menu():
    # Generérer 4 tilfældige farver ud defineret liste
    rand_colours = [random.choice(colours) for i in range(4)] 
    print (rand_colours) #test ved rigtigt svar
    Rematch=0
    #Spil start/kort intro
    print('**********************')
    print('Welcome to MasterMind')
    print('Choose four colours:')
    print('black, white, blue, red, green or yellow')
    attempts = 0  
    colour_choice=[]
    
    #while loop med spillers input
    while attempts<12:
        while len(colour_choice)!=4 or any(c not in colours for c in colour_choice):
            print(" ")
            colour_choice=input("Make your guess:")
            colour_choice = colour_choice.split()
            
            if len(colour_choice)!=4 or any(c not in colours for c in colour_choice):
                print("Error", "Invalid input! Please enter 4 valid colors.")
        
# samligning af farver, spiller mod com
        compare = []
        for i in range(len(colour_choice)):
            if colour_choice[i] == rand_colours[i]:
                compare.append("black")
                if compare == ['black', 'black', 'black', 'black']:
                    print("Good Job, You Won")
                    print(" ")
                    Rematch=input("Do yoy want a rematch (yes or no):")
                    if Rematch=="yes":
                        attempts=0
                        rand_colours = [random.choice(colours) for i in range(4)]                      
                    else:
                        return
            elif colour_choice[i] in rand_colours:
                compare.append("white")
                
        
        if Rematch !="yes":
            compare.sort() # sortere lighederne således at sort står først
            attempts += 1 # forsøgs tæller
            print(colour_choice, compare)
        else:
            Rematch=0
            
            
        #Ved første forsøg uden s ellers med s
        if attempts==1:
            print(f"{attempts} Attempt")
        elif attempts>=2:
            print(f"{attempts} Attempts")
        elif attempts==0:
            pass
        
            
        colour_choice=[]  #listen tømmes og spillet fortsætter
        
        # efter 12 forsøg ender spillet
        if attempts==12:
            print("Too Bad, You Lost", f"Right answer: {rand_colours}")
            print(" ")
            Rematch=input("Do yoy want a rematch (yes or no):")
            if Rematch=="yes":
                Rematch=0
                attempts=0
                rand_colours = [random.choice(colours) for i in range(4)] 
            else:
                return
                
input_main_menu()