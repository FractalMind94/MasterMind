# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 10:14:57 2024

@author: KOM
"""
compare = []
colour_choice=[]
attempts = 0
import random
# farver
colours =  [ "red", "blue", "green", "yellow", "white", "black" ]        
# Generérer 4 tilfældige farver ud defineret liste
rand_colours = [random.choice(colours) for i in range(4)] 
print(rand_colours)
#spillers input, samligning og print af resultater    
def input_main_menu():
    
    colour_choice=[]
    while len(colour_choice)!=4 or any(c not in colours for c in colour_choice):
        print("")
        colour_choice=input("Choose four colours - red, blue, yellow, green, white & black:")
        colour_choice = colour_choice.split()
    # return (colour_choice)

# samligning af farvekoder
    compare = []
    for i in range(len(colour_choice)):
        if colour_choice[i] == rand_colours[i]:
            compare.append("black")
            if compare == ['black', 'black', 'black', 'black']:
                print("Good Job, You Won")
                return print(colour_choice, rand_colours, compare)
        elif colour_choice[i] in rand_colours:
            compare.append("white")
      
            
            
    print(colour_choice, compare)
    print(f"{attempts+1} Attempts")
    

def input_2():
   colour_choice=[]
   while len(colour_choice)!=4 or any(c not in colours for c in colour_choice):
       print("")
       colour_choice=input("Try again:")
       colour_choice = colour_choice.split()
   # return (colour_choice)

   compare = []
   for i in range(len(colour_choice)):
       if compare == ['black', 'black', 'black', 'black']:
           print("Good Job, You Won")
           break
       elif colour_choice[i] == rand_colours[i]:
           compare.append("black")
       elif colour_choice[i] in rand_colours:
           compare.append("white")
      
   print(colour_choice, compare)
   print(f"{attempts+1} Attempts")
   
   
          
#Spil start
print('**********************')
print('Welcome to MasterMind')


while len(colour_choice)>4 or len(colour_choice)<4:
    colour_choice=input_main_menu()
    # if colour_choice==rand_colours:
    #     print("Good Job, You Won")
    while colour_choice!=rand_colours or attempts<11:
        attempts += 1
        colour_choice=input_2()
        if attempts==11:
            print("Too Bad, You Lost")
            attempts-=11
            break
# if colour_choice==rand_colours:
#     print("Good Job, You Won")
            

        
        
# GAMLE FORSØG 

# def input_colour(i, colour_choice):

# # rand_colours =[ "red", "blue", "green", "yellow"]
    
    # # Input 4 farver

# # colour_choice = colour_choice.split()
# # colour_choice = [ "red", "red", "green", "white"]

# 
# for x in range(len(compare)):
#     if compare[x] == ["black"]:
#         compare.append(x)
#     elif compare[x] != ["black"]:
#         compare.append("")
#     else:
#         compare.append("white")
# print(compare)        

#input("Choose four colours - red, blue, yellow, green, white & black:")


 # compare =  list(set(rand_colours).intersection(colour_choice))

 # compare = [x for x in rand_colours if x in colour_choice]

 # for colour in colour_choice:
 #     if colour_choice[0] == rand_colours[0]:
 #         compare.append(black)
 #     elif colour_choice[0] == rand_colours[1]:
 #         compare.append(white)
 #     elif colour_choice[0] == rand_colours[2]:
 #         compare.append(white)
 #     elif colour_choice[0] == rand_colours[3]:
 #         compare.append(white)

 #     elif colour_choice[1] ==  rand_colours[1]:
 #         compare.append(black)
 #     elif colour_choice[1] ==  rand_colours[0]:
 #         compare.append(white)
 #     elif colour_choice[1] == rand_colours[2]:
 #         compare.append(white)
 #     elif colour_choice[1] == rand_colours[3]:
 #         compare.append(white)

 #     elif colour_choice[2] ==  rand_colours[2]:
 #         compare.append(black)
 #     elif colour_choice[2] == rand_colours[0]:
 #         compare.append(white)
 #     elif colour_choice[2] == rand_colours[1]:
 #         compare.append(white)
 #     elif colour_choice[2] == rand_colours[3]:
 #         compare.append(white)
     
 #     elif colour_choice[3] == rand_colours[3]:
 #         compare.append(black)
 #     elif colour_choice[3] ==  rand_colours[0]:
 #         compare.append(white)
 #     elif colour_choice[3] ==  rand_colours[1]:
 #         compare.append(white)
 #     elif colour_choice[3] ==  rand_colours[2]:
 #         compare.append(white)
     
 #     else:
 #         compare.append()

 # for colour in colour_choice:
 #     for colour in rand_colours:
 #         if colour in rand_colours:
 #             compare.append(black)
 #         elif colour in rand_colours:
 #             compare.append(white)
 #         else:
 #             compare.append()
         
 # for colour in range(len(colour_choice)):
 #           # for j in range(i + 1, len(input_list)):
 #         if colour in range(len(rand_colours)):
 #             compare.append(black)
 #         elif colour in rand_colours:
 #             compare.append(white)
 #         else:
 #             compare.append()         
        
        
        
        
        
        
        
        
        
