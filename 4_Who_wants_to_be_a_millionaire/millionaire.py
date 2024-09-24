"""This Python script implements a simplified version of the
 "Who Wants to Be a Millionaire"game using Tkinter for GUI,Pygame for audio playback,
 and Pyttsx3 for text-to-speech functionalities
 The game allows users to answer multiple-choice questions, use lifelines, 
 and win virtual money based on their performance.
 ## Features
 - **Question Handling**: Questions and answer options are loaded from a JSON file (`my.json`).
    Users select answers by clicking on the corresponding buttons.
  
- **Lifelines**: Implemented lifelines include:
  - **50-50**: Removes two incorrect options.
  - **Audience Poll**: Displays audience poll results using progress bars
      to indicate percentage votes for each option.
  - **Phone a Friend**: Simulates calling a friend for help using text-to-speech
      to read out the correct answer.

- **User Experience**: 
  - Upon answering all questions correctly,
    users win a virtual prize of $1,000,000 and can view top users' scores.
  - If a wrong answer is selected, users can try again or view top users' scores."""

from random import randint
from tkinter import *
import  tkinter as tk
from tkinter.ttk import Progressbar
from pygame import mixer
import pyttsx3
import json

def usernames_entered():
    # List to store user names and their corresponding position in the game
    users=[]
    def get_entry():
        '''Function to get user entry and store it in users_names list'''
        val=name.get()
        if val:
            users.append(val)
            users.append(0)
        else:
            print('empty entery')
        win.destroy()

    # Create the main Tkinter window for entering user name
    win=Tk()
    win.geometry("400x250+600+250")
    win.title('names')
    win.config(bg='black')

    # Label and Entry for user name
    Label(win,text='user',bg='black',fg='white').grid(row=0,column=0)
    name=Entry(win,width=30,font=('arial',13,'bold'))
    name.grid(row=0,column=1,pady=40)

    # Button to submit user name
    Button(win,text='enter',command=get_entry,font=('arial',13,'bold')).grid(row=1,column=1)

    win.grid_columnconfigure(0,minsize=100)
    win.grid_columnconfigure(1,minsize=100)
    win.mainloop()
    return users
users_names=usernames_entered()

# Initialize Pygame mixer for playing audio files
mixer.init()

# Load and play background music
mixer.music.load('4_Who_wants_to_be_a_millionaire\\mp3\\kbc.mp3')
mixer.music.play(-1)

# Initialize Pyttsx3 engine for text-to-speech
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

corections_count=0
list_or_win=['0$','1.000$','32.000$','1.000.000$']
images_index=0
questions_index=[8,2,11,4,5,3,10,12,1,7,9,6,14,13]

def select(event):
    '''Function to handle user selection of answer options'''
    callButton.place_forget()
    progressbarA.place_forget()
    progressbarB.place_forget()
    progressbarC.place_forget()
    progressbarD.place_forget()

    progressbarLabelA.place_forget()
    progressbarLabelB.place_forget()
    progressbarLabelC.place_forget()
    progressbarLabelD.place_forget()

    b=event.widget
    value=b['text']
    for i in range(15):
        def top_users():
            '''Function to display top users with highest winnings'''
            win1 =tk.Tk()
            win1.geometry("400x500+100+200")
            win1.title('top')
            win1.config(bg='black')
            mdict={}
            with open('4_Who_wants_to_be_a_millionaire\\user.txt') as f:
                file_list=f.readlines()
                for i in file_list:
                    el=i.strip("[]\n' ").split("',")
                    mdict[el[0]]=el[1]

            award_seats=0
            for j in sorted(mdict.items() ,key=lambda x:int(x[1]),reverse=True):
                if award_seats<1:
                    col='green'
                if 3>award_seats>=1:
                    col='yellow'
                if award_seats>=3:
                    col='white'

                if int(j[1])<5:
                    max_win=list_or_win[0]
                if int(j[1])>=5:
                    max_win=list_or_win[1]
                if 5<int(j[1])>=10:
                    max_win=list_or_win[2]
                if int(j[1])>=15:
                    max_win=list_or_win[3]

                lebel_1=tk.Label(win1,text=f"{award_seats+1}.{j[0]}: {max_win} {j[1]}",
                                 bg='black',fg=col,font=('arial',18,'bold'),width=20,anchor='w')
                lebel_1.grid(row=award_seats,column=0)
                award_seats+=1
            win1.mainloop()

        if value==correct_answer[i]:
            global corections_count,images_index
            corections_count+=1
            if len(questions_index)==0:
                images_index=0
                def close():
                    root2.destroy()
                    root.destroy()


                def playagain():
                    '''Function to play again'''
                    lifeline50button.config(state=NORMAL,image=image50)
                    audiencePoleButton.config(state=NORMAL,image=audiencePole)
                    phoneLifelineButton.config(state=NORMAL,image=phoneImage)
                    root2.destroy()
                    questionArea.delete(1.0,END)
                    questionArea.insert(END,questions[0])

                    optionButton1.config(text=first_option[0])
                    optionButton2.config(text=second_option[0])
                    optionButton3.config(text=third_option[0])
                    optionButton4.config(text=fourt_option[0])
                    amountLabel.config(image=amountimage)
                    global questions_index,corections_count
                    questions_index=[8,2,11,4,5,3,10,12,1,7,9,6,14,13]
                    corections_count=0


                #Stop background music, play winning sound, and create result window
                mixer.music.stop()
                mixer.music.load('4_Who_wants_to_be_a_millionaire\\mp3\\Kbcwon.mp3')
                mixer.music.play()
                root2=Toplevel()
                root2.overrideredirect(True)
                root2.config(bg='black')
                root2.geometry('500x600+140+30')
                root2.title('You wan 0 pounds')

                imglabel=Label(root2,image=centerImage,bd=0)
                imglabel.pack(pady=30)


                playagainbutton=Button(root2,text='Play Again',
                        font=('arial',20,'bold'),bg='black',fg='white',
                        activebackground='black',activeforeground='white',
                        bd=0,cursor='hand2',command=playagain)
                playagainbutton.pack()


                closebutton=Button(root2,text='Close',font=('arial',20,'bold'),
                                   bg='black',fg='white',activebackground='black',
                                   activeforeground='white',bd=0,cursor='hand2',command=close)
                closebutton.pack()

                topbutton=Button(root2,text='Top Users',font=('arial',20,'bold'),
                                 bg='black',fg='white',activebackground='black',
                                 activeforeground='white',bd=0,cursor='hand2',command=top_users)
                topbutton.pack()

                winlabel=Label(root2,text='You Win 1.000.000 $',
                        font=('arial',40,'bold'),bg='black',fg='white')
                winlabel.pack()

                happyimage=PhotoImage(file='4_Who_wants_to_be_a_millionaire\\images\\happy.png')

                sadlabel=Label(root2,image=happyimage,bg='black')
                sadlabel.place(x=30,y=280)

                sadlabel=Label(root2,image=happyimage,bg='black')
                sadlabel.place(x=400,y=280)
                if len(users_names)>0:
                    users_names[1]=corections_count
                    with open('4_Who_wants_to_be_a_millionaire\\user.txt','a',encoding='utf-8') as uf:
                        uf.write(str(users_names)+'\n')

                root2.mainloop()
                break
            random_number=randint(0,len(questions_index)-1)
            el_index= questions_index[random_number]
            questionArea.delete(1.0,END)
            questionArea.insert(END,questions[el_index])
            text_button1=randint(0,1)
            if text_button1==0:
                text_button2=1
            else:
                text_button2=0
            text_button3=randint(2,3)
            if text_button3==2:
                text_button4=3
            else:
                text_button4=2
            optionButton1.config(text=options_list[text_button1][el_index])
            optionButton2.config(text=options_list[text_button2][el_index])
            optionButton3.config(text=options_list[text_button3][el_index])
            optionButton4.config(text=options_list[text_button4][el_index])
            amountLabel.config(image=amountimages[images_index])
            images_index+=1
            questions_index.pop(random_number)

        if value not in correct_answer:

            def close():
                root1.destroy()
                root.destroy()


            def tryagain():
                lifeline50button.config(state=NORMAL,image=image50)
                audiencePoleButton.config(state=NORMAL,image=audiencePole)
                phoneLifelineButton.config(state=NORMAL,image=phoneImage)
                root1.destroy()
                questionArea.delete(1.0,END)
                questionArea.insert(END,questions[0])

                optionButton1.config(text=first_option[0])
                optionButton2.config(text=second_option[0])
                optionButton3.config(text=third_option[0])
                optionButton4.config(text=fourt_option[0])
                amountLabel.config(image=amountimage)
                global questions_index
                questions_index=[8,2,11,4,5,3,10,12,1,7,9,6,14,13]


            root1=Toplevel()
            root1.overrideredirect(True)
            root1.config(bg='black')
            root1.geometry('500x600+140+30')
            root1.title('You wan 0 pounds')

            imglabel=Label(root1,image=centerImage,bd=0)
            imglabel.pack(pady=30)

            loselabel=Label(root1,text='You Lose',font=('arial',40,'bold'),bg='black',fg='white')
            loselabel.pack()

            tryagainbutton=Button(root1,text='Try Again',font=('arial',20,'bold'),
                                  bg='black',fg='white',activebackground='black',
                                  activeforeground='white',bd=0,cursor='hand2',command=tryagain)
            tryagainbutton.pack()

            closebutton=Button(root1,text='Close',font=('arial',20,'bold'),
                               bg='black',fg='white',activebackground='black',
                               activeforeground='white',bd=0,cursor='hand2',command=close)
            closebutton.pack()

            uesrbutton=Button(root1,text='Top users',font=('arial',20,'bold'),
                              bg='black',fg='white',activebackground='black',
                              activeforeground='white',bd=0,cursor='hand2',command=top_users)
            uesrbutton.pack()


            sadimage=PhotoImage(file='4_Who_wants_to_be_a_millionaire\\images\\sad.png')
            sadlabel=Label(root1,image=sadimage,bg='black')
            sadlabel.place(x=30,y=280)
            sadlabel=Label(root1,image=sadimage,bg='black')
            sadlabel.place(x=400,y=280)
            if corections_count<5:
                loselabel=Label(root1,text=f'You win {list_or_win[0]}',
                        font=('arial',20,'bold'),bg='black',fg='white')
                loselabel.pack()

            if corections_count>=5 and corections_count<9:
                loselabel=Label(root1,text=f'You win {list_or_win[1]}',
                        font=('arial',20,'bold'),bg='black',fg='white')
                loselabel.pack()

            if corections_count>=10 and corections_count<=13:
                loselabel=Label(root1,text=f'You win {list_or_win[2]}',
                        font=('arial',20,'bold'),bg='black',fg='white')
                loselabel.pack()
            if len(users_names)>0:
                users_names[1]=corections_count+1
                with open('4_Who_wants_to_be_a_millionaire\\user.txt','a') as uf:
                    uf.write(str(users_names)+'\n')
            images_index = 0
            corections_count=0
            root1.mainloop()
            break


def lifeline50():
    '''Function to implement 50-50 lifeline'''
    lifeline50button.config(image=image50X,state=DISABLED)
    correct_answer_index=correct_answer
    optionButton_index={1:optionButton1,2:optionButton2,3:optionButton3,4:optionButton4}
    button_text1 = optionButton1.cget('text')
    button_text2 = optionButton2.cget('text')
    button_text3 = optionButton3.cget('text')
    button_text4 = optionButton4.cget('text')
    for i in range(15):
        if questionArea.get(1.0,'end-1c')==questions[i]:
            el=correct_answer_index[i]
            if el==button_text1:
                optionButton_index[2].config(text='')
                optionButton_index[randint(3,4)].config(text='')
            if el==button_text2:
                optionButton_index[1].config(text='')
                optionButton_index[randint(3,4)].config(text='')
            if el==button_text3:
                optionButton_index[4].config(text='')
                optionButton_index[randint(1,2)].config(text='')
            if el==button_text4:
                optionButton_index[3].config(text='')
                optionButton_index[randint(1,2)].config(text='')


def audiencePoleLifeline():
    '''Function to implement audience poll lifeline'''
    audiencePoleButton.config(image=audiencePoleX,state=DISABLED)
    progressbarA.place(x=580,y=190)
    progressbarB.place(x=620,y=190)
    progressbarC.place(x=660,y=190)
    progressbarD.place(x=700,y=190)

    progressbarLabelA.place(x=580,y=320)
    progressbarLabelB.place(x=620,y=320)
    progressbarLabelC.place(x=660,y=320)
    progressbarLabelD.place(x=700,y=320)
    button_text1 = optionButton1.cget('text')
    button_text2 = optionButton2.cget('text')
    button_text3 = optionButton3.cget('text')
    button_text4 = optionButton4.cget('text')


    correct_answer_index=correct_answer
    optionButton_index={1:progressbarA,2:progressbarB,3:progressbarC,4:progressbarD}
    for i in range(15):
        el=correct_answer_index[i]
        if questionArea.get(1.0,'end-1c')==questions[i]:
            optionButton_index[1].config(value=20)
            optionButton_index[2].config(value=30)
            optionButton_index[3].config(value=50)
            optionButton_index[4].config(value=40)
            if el==button_text1:
                optionButton_index[1].config(value=90)
            if el==button_text2:
                optionButton_index[2].config(value=90)
            if el==button_text3:
                optionButton_index[3].config(value=90)
            if el==button_text4:
                optionButton_index[4].config(value=90)

def phoneLifeline():
    '''Function to implement phone a friend lifeline'''
    mixer.music.load("4_Who_wants_to_be_a_millionaire\\mp3\\calling.mp3")
    mixer.music.play()
    callButton.place(x=70,y=260)
    phoneLifelineButton.config(image=phoneImageX,state=DISABLED)


def phoneclick():
    '''Function to handle phone click during phone a friend lifeline'''
    for i in range(15):
        if questionArea.get(1.0,'end-1c')==questions[i]:
            engine.say(f'правильный  ответ   {correct_answer[i]}')
            engine.runAndWait()

# Load questions and answers from JSON file
with open('4_Who_wants_to_be_a_millionaire\\my.json','r') as f:
    data=json.load(f)

questions=data['questions']
correct_answer=data['correct_answer']
first_option=data['first_option']
second_option=data['second_option']
third_option=data['third_option']
fourt_option=data['fourt_option']
options_list=[first_option,second_option,third_option,fourt_option]

root=Tk()

root.geometry('1300x700')
root.title('Who wants to be a millionaire')

root.config(bg='black')

# Left Frame for lifelines, logo, and amount images
leftframe=Frame(root,bg='black',padx=90)
leftframe.grid(row=0,column=0)

# Top Frame for lifeline buttons
topframe=Frame(leftframe,bg='black',pady=15)
topframe.grid()

# Center Frame for logo image
centerframe=Frame(leftframe,bg='black',pady=15)
centerframe.grid(row=1,column=0)

# Bottom Frame for question, options, and layout image
bottomframe=Frame(leftframe)
bottomframe.grid(row=2,column=0)

# Right Frame for amount images
righttframe=Frame(root,pady=25,padx=50,bg='black')
righttframe.grid(row=0,column=1)

# Lifeline buttons
image50=PhotoImage(file='4_Who_wants_to_be_a_millionaire\\images\\50-50.png')
image50X=PhotoImage(file='4_Who_wants_to_be_a_millionaire\\images\\50-50-X.png')

lifeline50button=Button(topframe,image=image50,bg='black',bd=0,activebackground='black',
                        width=180,height=80,command=lifeline50)
lifeline50button.grid(row=0,column=0)

audiencePole=PhotoImage(file='4_Who_wants_to_be_a_millionaire\\images\\audiencePole.png')
audiencePoleX=PhotoImage(file='4_Who_wants_to_be_a_millionaire\\images\\audiencePoleX.png')

audiencePoleButton=Button(topframe,image=audiencePole,bg='black',bd=0,activebackground='black',
                          width=180,height=80,command=audiencePoleLifeline)
audiencePoleButton.grid(row=0,column=1)

phoneImage=PhotoImage(file='4_Who_wants_to_be_a_millionaire\\images\\phoneAFriend.png')
phoneImageX=PhotoImage(file='4_Who_wants_to_be_a_millionaire\\images\\phoneAFriendX.png')

phoneLifelineButton=Button(topframe,image=phoneImage,bg='black',bd=0,activebackground='black',
                           width=180,height=80,command=phoneLifeline)
phoneLifelineButton.grid(row=0,column=2)

callimage=PhotoImage(file='4_Who_wants_to_be_a_millionaire\\images\\phone.png')
callButton=Button(root,image=callimage,bd=0,bg='black',activebackground='black',
                  cursor='hand2',command=phoneclick)

centerImage=PhotoImage(file='4_Who_wants_to_be_a_millionaire\\images\\center.png')

logoLabal=Label(centerframe,image=centerImage,bg='black',width=300,height=200)
logoLabal.grid(row=0,column=0)

amountimages=[]

for i in range(1,16):
    el=PhotoImage(file=f'4_Who_wants_to_be_a_millionaire\\images\\Picture{i}.png')
    amountimages.append(el)

# Amount images in the right frame
amountimage=PhotoImage(file='4_Who_wants_to_be_a_millionaire\\images\\Picture0.png')
amountLabel=Label(righttframe,image=amountimage)
amountLabel.grid(row=0,column=0)

# Layout image in the bottom frame
layoutImage=PhotoImage(file='4_Who_wants_to_be_a_millionaire\\images\\lay.png')
layoutLabel=Label(bottomframe,image=layoutImage,bg='black')
layoutLabel.grid(row=0,column=0)

# Question and options in the bottom frame
questionArea=Text(bottomframe,font=('arial',18,'bold'),width=34,
                  height=2,wrap='word',bg='black',fg='white',bd=0)
questionArea.place(x=70,y=10)

questionArea.insert(END,questions[0])

labelA=Label(bottomframe,text='A:',bg='black',fg='white',font=('arial',16,'bold'))
labelA.place(x=60,y=110)
optionButton1=Button(bottomframe,text=first_option[0],font=('aria',18,'bold'),bg='black',fg='white',
                     bd=0,activebackground='black',activeforeground='white',cursor='hand2')
optionButton1.place(x=100,y=100)

labelB=Label(bottomframe,text='B:',bg='black',fg='white',font=('arial',16,'bold'))
labelB.place(x=330,y=110)

optionButton2=Button(bottomframe,text=second_option[0],font=('aria',18,'bold'),
                     bg='black',fg='white',bd=0,activebackground='black',
                     activeforeground='white',cursor='hand2')
optionButton2.place(x=370,y=100)

labelC=Label(bottomframe,text='C:',bg='black',fg='white',font=('arial',16,'bold'))
labelC.place(x=60,y=190)

optionButton3=Button(bottomframe,text=third_option[0],font=('aria',18,'bold'),
                     bg='black',fg='white',bd=0,activebackground='black',
                     activeforeground='white',cursor='hand2')
optionButton3.place(x=100,y=180)

labelD=Label(bottomframe,text='D:',bg='black',fg='white',font=('arial',16,'bold'))
labelD.place(x=330,y=190)

optionButton4=Button(bottomframe,text=fourt_option[0],font=('aria',18,'bold'),
                     bg='black',fg='white',bd=0,activebackground='black',
                     activeforeground='white',cursor='hand2')
optionButton4.place(x=370,y=180)

progressbarA=Progressbar(root,orient=VERTICAL,length=120)
progressbarB=Progressbar(root,orient=VERTICAL,length=120)
progressbarC=Progressbar(root,orient=VERTICAL,length=120)
progressbarD=Progressbar(root,orient=VERTICAL,length=120)

progressbarLabelA=Label(root,text='A',font=('arial',20,'bold'),bg='black',fg='white')
progressbarLabelB=Label(root,text='B',font=('arial',20,'bold'),bg='black',fg='white')
progressbarLabelC=Label(root,text='C',font=('arial',20,'bold'),bg='black',fg='white')
progressbarLabelD=Label(root,text='D',font=('arial',20,'bold'),bg='black',fg='white')

optionButton1.bind('<Button>',select)
optionButton2.bind('<Button>',select)
optionButton3.bind('<Button>',select)
optionButton4.bind('<Button>',select)

root.mainloop()
