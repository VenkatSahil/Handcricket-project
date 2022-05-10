#!/usr/bin/env python
# coding: utf-8

# # HAND CRICKET GAME USING PYTHON

# In[ ]:


import random
l=[1,2]
print('''HELLO!!! PLAYER, WELCOME TO HAND CRICKET 

"Hand Cricket is a game in which two players show scores on their respective fingers. If the scores are equal, the batsman is  declared out. Else, the score of the batsman is added to the total runs of the batting team."

In our game you are playing with the computer.
Firstly there will be a toss.The player who wins the toss will have chance to select to bat/bowl first. After the toss the play starts and scores will be counted.

You can choose random numbers between 1 and 6 for your score to bat or bowl and same for the computer.
lets start the game with toss
''')
def playagain(): 
    print("GOOD GAME !: ")
    playagain=input('''DO YOU WANT TO PLAY AGAIN ? YES/NO 
    ***ENTER YES TO PLAY AGAIN , NO TO EXIT''')
    if playagain.upper() == "YES":
        main()
    elif playagain.upper()=="NO":
        print("THANKS FOR PLAYING")
        exit()
    else:
        print("invalid input \n try again")
        playagain()
L=[1,2,3,4,5,6]
            
def main():
    def user_batting(): 
        print("YOU are BATTING")
        user_runs=0
        while(True):
            comp=random.randint(1,6)
            user=int(input("enter your runs from 1 to 6 (Bat) : "))
          
            print("computer bowls",comp)
            if (comp==user):
                print("YOU LOST ")
                print("runs : ",user_runs) 
                break
            if user not in L :
                print("invalid input. Try Again")
                continue
            user_runs=user_runs+user
            
        print("computer requires : ",user_runs+1,"to win the game") 
        comp_runs=0
        while(True):
            comp=random.randint(1,6)
            user=int(input("enter your ball from 1 to 6 (Bowling) : "))
            print("computer bats",comp)
            if (comp==user):
                print("gone...you dissmissed computer out")
                print("COMPruns : ",comp_runs)  
                break
            if user not in L:
                print("invalid input. Try again")
                continue
            
            comp_runs=comp_runs+comp
            if (comp_runs>user_runs):
                break
            
        if (comp_runs>user_runs):
            print("computer runs : ",comp_runs)
            print("you lost the game")
            playagain()
            
        elif(comp_runs<user_runs):
            print("HURRAY you won by",((user_runs)-(comp_runs)),"runs,congratulations...!")
            playagain()
        else:
            print("TIE MATCH")
            playagain()
                
                
                
    def comp_batting():
        print("computer is ready for batting")
        comp_runs=0
        while(True):
            comp=random.randint(1,6)
            user=int(input("enter your ball from 1 to 6 (Bowling) : "))
            print("computer bats",comp)
            if (comp==user):
                print("gone...you dissmissed computer out")
                print("computer score : ",comp_runs)
                break
            
            if user not in L:
                print("invalid input... try again")
                continue    
        
            
            comp_runs=comp_runs+comp  
        print("YOU require : ",comp_runs+1," runs to win the game") 
        user_runs=0 
        while(True):
            comp=random.randint(1,6)
            user=int(input("enter your runs from 1 to 6 Bat : "))
            print("computer bowls",comp)
            if (comp==user):
                print("You are out")
                print("YOUR SCORE : ",user_runs)  
                break
            if user not in L:
                print("invalid input...\n game restarting")  
                continue
                
            user_runs=user_runs+user
            if (user_runs>comp_runs):
                break
        if (comp_runs>user_runs):
            print("computer runs : ",comp_runs)
            print("you lost the game")
            playagain()
        elif (comp_runs<user_runs):
            print("HURRAY you won the by",((user_runs)-(comp_runs)),"runs,congratulations...!")
            playagain()
        else:
            print("TIE MATCH")
            playagain()
                        
    
    def toss():
        Toss=int(input('''CHOOSE ODD OR EVEN
1.EVEN
2.ODD 
***ENTER 1 for EVEN or 2 for ODD***'''))
        
        if Toss not in l :
            print ( " invalid  input , Try again ")
            toss()
        if (Toss==1):
            print ("you selected even")
        if (Toss==2):
            print("you selected odd")
        my_input=int(input("chose number from 1 to 6 : "))
        if my_input not in L:
            print("invalid input. Try Again")
            toss()
        comp_input=random.randint(1,6)
        print("comp_input is : ",comp_input)
        if Toss== 1:
            if((my_input+comp_input)%2==0):
                print("You won the toss")
                choice=int(input('''Batting or Bowling
                1.Batting
                2.Bowling
                ***ENTER 1 for Batting or 2 for Bowling***'''))
                if (choice==1):
                    user_batting()
                elif (choice==2):
                    comp_batting()
                else:
                    print("Invalid Input. Try Again")
                    toss()
            else:
                print("computer won the toss")
                comp=random.choice(["batting","bowling"])
                if comp=="batting":
                    print("computer chosen for BATTING") 
                    comp_batting()
                elif comp=="bowling":
                    print("computer chosen for BOWLING")
                    user_batting()
        elif (Toss==2):
            if((my_input+comp_input)%2==0):
                print("computer won the toss")
                comp=random.choice(["batting","bowling"])
                if comp=="batting":
                    print("computer chosen for BATTING") 
                    comp_batting()
                else:
                    print("computer chosen for BOWLING")
                    user_batting()
            else:
                print("You won the toss")
                choice=int(input('''Batting or Bowling
                1.Batting
                2.Bowling
                ***ENTER 1 for Batting or 2 for Bowling***'''))
                if (choice==1):
                    user_batting()
                elif (choice==2):
                    comp_batting()
                else:
                    print("invalid input...\n game restarting")
                    toss()
    print(toss())
print(main())

