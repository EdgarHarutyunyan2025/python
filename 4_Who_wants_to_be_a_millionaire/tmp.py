from tkinter import *
import  tkinter as tk
from tkinter.ttk import Progressbar
from pygame import mixer
import pyttsx3
import json

# Initialize Pyttsx3 engine for text-to-speech
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

# Initialize Pygame mixer for playing audio files
mixer.init()

# Load and play background music

mixer.music.load('4_Who_wants_to_be_a_millionaire\\mp3\\kbc.mp3')
mixer.music.play(-1)

list_or_win=['0$','1.000$','32.000$','1.000.000$']

# List to store user names and their corresponding position in the game
users_names=[]
def get_entry():
    '''Function to get user entry and store it in users_names list'''
    val=name.get()
    if val:
        users_names.append(val)
        users_names.append(0)
    else:
        print('empty entery')
    win.destroy()

# Create the main Tkinter window for entering user name
win=Tk()
win.geometry(f"400x250+600+250")
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
            win1.geometry(f"400x500+100+200")
            win1.title('top')
            win1.config(bg='black')
            mdict={}
            with open('4_Who_wants_to_be_a_millionaire\\user.txt') as f:
                file_list=f.readlines()
                for i in file_list:
                    el=i.strip("[]\n' ").split("',")
                    mdict[el[0]]=el[1]

            row=0
            for j in sorted(mdict.items() ,key=lambda x:int(x[1]),reverse=True):
                if row<1:
                    col='green'
                if 3>row>=1:
                    col='yellow'
                if row>=3:
                    col='white'

                if int(j[1])<5:
                    max_win=list_or_win[0]
                if int(j[1])>=5:
                    max_win=list_or_win[1]
                if 5<int(j[1])>=10:
                    max_win=list_or_win[2]
                if int(j[1])>=15:
                    max_win=list_or_win[3]

                lebel_1=tk.Label(win1,text=f"{row+1}.{j[0]}: {max_win} {j[1]}",bg='black',fg=col,
                                font=('arial',18,'bold'),width=20,anchor='w')
                lebel_1.grid(row=row,column=0)
                row+=1
            win1.mainloop()

        if value==correct_answer[i]:
            global num
            num=i
            if value==correct_answer[14]:
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
                    users_names[1]=num+1
                    with open('4_Who_wants_to_be_a_millionaire\\user.txt','a') as uf:
                        uf.write(str(users_names)+'\n')

                root2.mainloop()
                break

            questionArea.delete(1.0,END)
            questionArea.insert(END,questions[i+1])

            optionButton1.config(text=first_option[i+1])
            optionButton2.config(text=second_option[i+1])
            optionButton3.config(text=third_option[i+1])
            optionButton4.config(text=fourt_option[i+1])
            amountLabel.config(image=amountimages[i])

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
            if num<4:
                print(num)
                loselabel=Label(root1,text=f'You win {list_or_win[0]}',
                        font=('arial',20,'bold'),bg='black',fg='white')
                loselabel.pack()

            if num>=4 and num<9:
                loselabel=Label(root1,text=f'You win {list_or_win[1]}',
                        font=('arial',20,'bold'),bg='black',fg='white')
                loselabel.pack()

            if num>=9 and num<=13:
                loselabel=Label(root1,text=f'You win {list_or_win[2]}',
                        font=('arial',20,'bold'),bg='black',fg='white')
                loselabel.pack()
            if len(users_names)>0:
                users_names[1]=num+1
                with open('4_Who_wants_to_be_a_millionaire\\user.txt','a') as uf:
                    uf.write(str(users_names)+'\n')
            root1.mainloop()
            break


def lifeline50():
    '''Function to implement 50-50 lifeline'''
    lifeline50button.config(image=image50X,state=DISABLED)
    correct_answer_index=[1,3,1,4,3,4,3,2,1,3,1,2,4,3,2]
    optionButton_index={1:optionButton1,2:optionButton2,3:optionButton3,4:optionButton4}
    cunt_text = optionButton3.cget('text')
    print(cunt_text)
    for i in range(15):
        if questionArea.get(1.0,'end-1c')==questions[i]:
            el=correct_answer_index[i]
            if el==1 or el==4:
                optionButton_index[2].config(text='')
                optionButton_index[3].config(text='')
            if el==3 or el==2:
                optionButton_index[1].config(text='')
                optionButton_index[4].config(text='')


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

    correct_answer_index=[1,3,1,4,3,4,3,2,1,3,1,2,4,3,2]
    optionButton_index={1:progressbarA,2:progressbarB,3:progressbarC,4:progressbarD}
    for i in range(15):
        el=correct_answer_index[i]
        if questionArea.get(1.0,'end-1c')==questions[i]:
            optionButton_index[1].config(value=20)
            optionButton_index[2].config(value=30)
            optionButton_index[3].config(value=50)
            optionButton_index[4].config(value=40)
            optionButton_index[el].config(value=90)


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
