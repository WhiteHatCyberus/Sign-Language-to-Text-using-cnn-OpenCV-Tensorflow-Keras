#import module from tkinter for UI
from tkinter import *
import os
import subprocess
from datetime import datetime;
#creating instance of TK
root=Tk()

root.configure(background="#DFDFDF")

#root.geometry("300x300")

def function1():
    
    os.system("py create_gestures.py")
    os.system("py flip_images.py")
    os.system("py load_images.py")
    
def function2():
    
    os.system("py cnn_keras.py")

def function3():

    os.system("py display_all_gestures.py")

def function4():

    os.system("py set_hand_hist.py") #works
    
def function5():

    os.system("py recognize_gesture.py")   
  
def function6():

    os.system("py fun_util.py")   

def function7():
    os.system("py get_model_reports.py")        


def function9():

    root.destroy()


#stting title for the window
root.title("Sign To Text Converter")

#creating a text label
Label(root, text="SignText",font=("times new roman",20),fg="white",bg="#e51a4c",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Create Dataset",font=("times new roman",20),bg="#ffffff",fg='black',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Train Dataset using Keras",font=("times new roman",20),bg="#ffffff",fg="#000000",command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
Button(root,text="Display Gestures",font=('times new roman',20),bg="#ffffff",fg="#000000",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating fourth button
Button(root,text="Set Hand Histogram",font=('times new roman',20),bg="#ffffff",fg="#000000",command=function4).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating fifth button       
Button(root,text="Recognize Gesture as a Character",font=('times new roman',20),bg="#ffffff",fg="black",command=function5).grid(row=8,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating sixth button       
Button(root,text="Recognize Gesture as a Word",font=('times new roman',20),bg="#ffffff",fg="black",command=function6).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating seventh button       
Button(root,text="Model Summary",font=('times new roman',20),bg="#ffffff",fg="#000000",command=function7).grid(row=10,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating eight button              
Button(root,text="Exit",font=('times new roman',20),bg="#e51a4c",fg="white",command=function9).grid(row=11,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
