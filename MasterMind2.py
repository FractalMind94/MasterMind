# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 16:24:53 2024

@author: KOM
"""

         
compare = []
colour_choice=[]
#attempts = 0
import random
# farver
colours =  [ "red", "blue", "green", "yellow", "white", "black" ]        
# Generérer 4 tilfældige farver ud defineret liste
rand_colours = [random.choice(colours) for i in range(4)] 
print(rand_colours)


   
def input_main_menu():
    
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
            print("")
            colour_choice=input("Make your guess:")
            colour_choice = colour_choice.split()
            
# samligning af farver, spiller mod com
        compare = []
        for i in range(len(colour_choice)):
            if colour_choice[i] == rand_colours[i]:
                compare.append("black")
                if compare == ['black', 'black', 'black', 'black']:
                    print("Good Job, You Won")
                    return
            elif colour_choice[i] in rand_colours:
                compare.append("white")
                
        
        compare.sort() # sortere lighederne således at sort står først
        attempts += 1 # forsøgs tæller
        print(colour_choice, compare)
        print(f"{attempts} Attempts")
        colour_choice=[]  #listen tømmes og spillet fortsætter
        
        # efter 12 forsøg ender spillet
        if attempts==12:
            print("Too Bad, You Lost")
            
input_main_menu()        
 
    
    
    

# def input_2():
#    colour_choice=[]
#    while len(colour_choice)!=4 or any(c not in colours for c in colour_choice):
#        print("")
#        colour_choice=input("Try again:")
#        colour_choice = colour_choice.split()
#    # return (colour_choice)

#    compare = []
#    for i in range(len(colour_choice)):
#        if compare == ['black', 'black', 'black', 'black']:
#            print("Good Job, You Won")
#            break
#        elif colour_choice[i] == rand_colours[i]:
#            compare.append("black")
#        elif colour_choice[i] in rand_colours:
#            compare.append("white")
      
#    print(colour_choice, compare)
#    print(f"{attempts+1} Attempts")
   
   
          



# if len(colour_choice)>4 or len(colour_choice)<4:

    # if g=="correct":
        
    # if colour_choice==rand_colours:
    #     print("Good Job, You Won")
