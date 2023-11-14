from tkinter import *
from PIL import Image, ImageTk
from random import randint


root = Tk()  #helps display main window on running
root.title("MyGame") #give own name to game window bar 
root.configure(background="pink") #give background color to entire window, can also give hexcode here



#import all pictures using ImageTk.PhotoImage() meth in the application:

rc=ImageTk.PhotoImage(Image.open("rc.png"))
ru=ImageTk.PhotoImage(Image.open("ru.png"))
pc=ImageTk.PhotoImage(Image.open("pc.png"))
pu=ImageTk.PhotoImage(Image.open("pu.png"))
sc=ImageTk.PhotoImage(Image.open("sc.png"))
su=ImageTk.PhotoImage(Image.open("su.png"))


#now paste the pictures or layDown them, bg="" is to set background color of icon too
#Label is widget used to implement display boxes where you can place text or images

user_label=Label(root, image=su, bg="pink")
comp_label=Label(root, image=sc, bg="pink")

comp_label.grid(row=1, column=0)   # label define krke usko grid se relate krna
user_label.grid(row=1, column=4)


#scores
playerScore=Label(root, text=0, font=100,bg="pink",fg="black")
compScore=Label(root, text=0, font=100,bg="pink",fg="black")

compScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)


#indicator to depict side of user and computer 
computer_indicator=Label(root, font=100, text="COMPUTER",bg="pink" );
user_indicator=Label(root, bg="pink",font=100,text="USER")
computer_indicator.grid(row=0, column=1)
user_indicator.grid(row=0, column=3)




#messages
msg=Label(root, font=50, bg="black", fg="white")
msg.grid(row=3, column=2)


def update_message(x):  #update message
    msg['text']=x



def updateUserScore():
    score=int(playerScore["text"])
    score+=1
    playerScore["text"]=str(score)



def updateCompScore():
    score=int(compScore["text"])
    score+=1
    compScore["text"]=str(score)



#button
rock=Button(root, width=20, height=2, text="ROCK", command= lambda:updateChoice("rock"),bg="red", fg="white").grid(row=2, column=1)
paper=Button(root, width=20, height=2, text="PAPER", command= lambda:updateChoice("paper"),bg="yellow", fg="black").grid(row=2, column=2)
scissor=Button(root, width=20, height=2, text="SCISSOR", command= lambda:updateChoice("scissor"),bg="green", fg="white").grid(row=2, column=3)



#update user score
def checkWinner(player, computer):
    if player == computer:
        update_message("it's a tie!")
    elif player=="rock":
        if computer=="paper":
            update_message("You Loose")
            updateCompScore()
        else:
            update_message("You Win!")
            updateUserScore()
    elif player=="paper":
        if computer == "scissor":
            update_message("you loose")
            updateCompScore()
        else:
            update_message("You Win")
            updateUserScore()
    elif player=="scissor":
        if computer=="rock":
            update_message("You Loose")
            updateCompScore()
        else:
            update_message("You Win")
            updateUserScore()
    else:
        pass



#update choices
choices=["rock","paper","scissor"]



def updateChoice(x):
#for computer
    compChoice=choices[randint(0,2)]
    if(compChoice=="rock"):
        comp_label.configure(image=rc)
    elif(compChoice=="paper"):
        comp_label.configure(image=pc)
    else:
        comp_label.configure(image=sc)




# for user 
    if x=="rock":
        user_label.configure(image=ru)
    elif x=="paper":
        user_label.configure(image=pu)
    else:
        user_label.configure(image=su)
    checkWinner(x,compChoice)




    
    
   






root.mainloop(); #infinite loop used to run application, wait for an event to occur and process event as long as window is not closed.

