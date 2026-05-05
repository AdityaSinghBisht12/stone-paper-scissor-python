#imported random library for random and fair game

import random
def Stone_Paper_Scissor():
    dic={1:"Stone",2:"Paper",3:"Scissor"}
    #scores 
    Your_Score=0
    Computer_Score=0

    #while loop for continuos gameplay
    while True:
        k=input("Enter Stone or Paper or Scissor ---> ")
        
        #condition for inappropriate input
        if k.lower() not in ["stone","paper","scissor"]:
            print("Wrong choice pls correct your spelling ")
            print("-"*40)

        #condition for different winning possibilities
        else:
            z=random.randint(1,3)
            print(dic[z])
            if k.lower()=="stone" and z==3:
                Your_Score+=1
            elif k.lower()=="scissor" and z==2:
                Your_Score+=1
            elif k.lower()=="paper" and z==1:
                Your_Score+=1
            elif k.lower()=="scissor" and z==1:
                Computer_Score+=1
            elif k.lower()=="paper" and z==3:
                Computer_Score+=1
            elif k.lower()=="stone" and z==2:
                Computer_Score+=1
            else:
                Computer_Score+=0
                Your_Score+=0

            #Scores are displayed through this block
            print("Your Score is",Your_Score)
            print("Computer's Score is",Computer_Score)
            print("-"*40)

            #block to make ur game playable by pressing enter key
            print("Press enter key to play again")
            j=input("enter X to stop game \n ----------------------------------------")

            #block which decides the final score and displays it
            if j.lower() == "x":
                print("thank you for playing")
                if Your_Score > Computer_Score:
                    print("The winner is the user by a score of ",Your_Score,"-",Computer_Score)
                elif Your_Score < Computer_Score:
                    print("The winner is the computer by a score of ",Your_Score,"-",Computer_Score)
                else:
                    print("The match was tie breaker with a score of",Your_Score,"-",Computer_Score)
                pass
        
