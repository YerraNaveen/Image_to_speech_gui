
from tkinter import *

#import tkinter as tk

import os

from gtts import gTTS

#from gtts import *

from playsound import playsound

from tkinter import filedialog

from gtts.tokenizer import pre_processors

import pytesseract

import cv2

import pygame

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pygame.init()
# Initiating Pygame Mixer
pygame.mixer.init()

def upload():
    global file
    file = filedialog.askopenfile(filetypes = [('Image files', '*.jpg'), ('Image files', '*.png')])
    #print(file.name)
    #print(dir(file))
    #fname = file.name
    #fname = fname[fname.rfind('/')+1:]
    
    if file!=None:
        label2 = Label(text = "You have successfully selected your file...Click on convert to to convert it into text")
        label2.place(x = 0, y = 230)
        conver_button = Button(sc, text = "convert to text", width = "30", height = "2", bg = "black", fg = "white", command = convert)
        conver_button.place(x = 100, y = 250)

    else:
        label3 = Label(text = "You have not selected any file")
        label3.place(x = 0, y = 230)

def playy():
    pygame.mixer.music.load(song1)
    pygame.mixer.music.play()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()
def playsoundfun(song):
    global song1
    song1 = song
    pla = Button(sc, text="Play", width = "7", height = "2", bg = "black", fg = "white", command = playy)
    pla.place(x=100,y=450)
    
    paus = Button(sc, text="Pause", width = "7", height = "2", bg = "black", fg = "white", command = pause)
    paus.place(x=180,y=450)
    
    unpaus = Button(sc, text="Unpause", width = "7", height = "2", bg = "black", fg = "white", command = unpause)
    unpaus.place(x=260,y=450)

def play():
    fname = file.name
    fname = fname[fname.rfind('/')+1:]
    #print(fname)
    songName = str(fname) + ".mp3"
    print(songName)
    print(os.path.exists(songName))
    if not os.path.exists(songName):
        label8 = Label(text="We have successfully converted the text into speech.\nClick the play button to listen")
        label8.place(x = 0, y =400 )
        #speech = gTTS(text=text, lang="en")
        
        speech = gTTS(text = text, tld='com', lang='en', slow=False, lang_check=True, pre_processor_funcs=[
            pre_processors.tone_marks,
            pre_processors.end_of_line,
            pre_processors.abbreviations,
            pre_processors.word_sub
            ]
        )
        #speech = gTTS.tokenizer.pre_processors.end_of_line(text)
        speech.save(songName)
        playsoundfun(songName)
    else:
        label9  = Label(text = "The speech already exists.Click on play to listen")
        label9.place(x = 0, y =400 )
        playsoundfun(songName)


def convert():
    print("Reading the file!")
    img = cv2.imread(file.name)
    print(file.name)
    #cv2.imshow("image name", img)
    #cv2.waitKey(1)
    print("Converting the image to gray")
    #img  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print("Getting the text from the image")
    global text
    text = pytesseract.image_to_string(img)
    print(text)
    #print(len(text))
    #text = text + "hello"
    l = text.strip()
    #print(len(l))
    #print(l)
    if len(l) == 0 :
        label5 = Label(text = "         No text available from the image ): \nPlease select another image (:")
        label5.place(x = 0, y = 300)
    else:
        #label4 = Label(text=text)
        #label4.place(x = 0, y = 300)
        label6 = Label(text = "We have successfully converted the image into text. Click the play button to listen")
        label6.place(x = 0, y = 300)

        play_button = Button(sc, text = "Convert to Speech",  width = "30", height = "2", bg = "black", fg = "white", command = play)
        play_button.place(x = 100, y = 350)

        #speech = gTTS(text = text, lang="en")
        #speech.save('speech.mp3')
        #playsound('speech.mp3')

    #cv2.imshow("Image",img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()


sc = Tk()
sc.geometry("500x700")
sc.title("Image -> Text -> Speech")
heading = Label(text = "We will read...", bg = "black", fg = "white", width = "500", height = "3")
heading.pack()

intro_label = Label(text = "Hello, User ,Read the following instructions and start using")
intro_label.place(x = 0, y = 50)

instruction = Label(text = "1.Choose an image having text to read\n     2.And click on choose to choose your file")
instruction.place(x = 5, y = 65)

label1 = Label(text = 'Choose file:', width = "10", height = "3")
label1.place(x = 0, y = 150)

upload_button = Button(sc, text = "Choose", width = "30", height = "2", bg = "black", fg = "white", command= upload)
upload_button.place(x = 100, y = 150)



sc.mainloop()
