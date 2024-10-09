#_____________________________________________________J.A.R.V.I.S________________________________________________________
#Python modules used for this programm
import sys
import speech_recognition as sr
import pyttsx3
# import pywhatkit
# import pywhatkit as kit
# import datetime
# import wikipedia
# import pyjokes
# import webbrowser
# import time
# import subprocess
import os
# import cv2
# import random
from requests import get
# import smtplib
# import psutil
# import instaloader
# import pyautogui
# import PyPDF2
# from Recordings import Record_Option
from PIL import ImageGrab
# import pyaudio
# import wave
import numpy as np 
from PhoneNumer import Phonenumber_location_tracker
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from JarvisUi import Ui_JarvisUI
from state import state
from pywikihow import search_wikihow
# import speedtest
from pytube import YouTube
# import qrcode

#Set our engine to "Pyttsx3" which is used for text to speech in Python 
#and sapi5 is Microsoft speech application platform interface 
#we will be using this for text to speech function.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id) #index '0' for 'David'(male) voice index '1' for 'zira'(female) voice

#Main classs where all the functiona are present
class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
    
    def run(self):
        self.Intro()
    
    def Intro(self):
        self.talk("Initializing Jarvis...")
        # Add any additional initialization tasks here
    def talk(self, message):
        engine.say(message)
        engine.runAndWait()
    
    #function that will take the commands  to convert voice into text
    def take_Command(self):
        try:
            listener = sr.Recognizer()
            with sr.Microphone() as source:
                print('Listening....')
                listener.pause_threshold = 1
                voice = listener.listen(source,timeout=4,phrase_time_limit=7)
                print("Recognizing...")
                command1 = listener.recognize_google(voice,language='en-in')
                command1 = command1.lower()  
                if 'jarvis' in command1: 
                    command1 = command1.replace('jarvis','')
            return command1
        except:
            return 'None'
        
    #Jarvis commands controller 
    def run_jarvis(self):
        self.wish()
        self.talk('Hello boss I am jarvis your assistant. please tell me how can i help you')
        while True:
            self.command = self.take_Command() #Every time taking command after a task is done
            print(self.command)
            if ('play a song' in self.command) or ('youtube' in self.command) or ("download a song" in self.command) or ("download song" in self.command) : 
                #commands for opening youtube, playing a song in youtube, and download a song in youtube
                self.yt(self.command) #function is from line 555
            elif ('your age' in self.command) or ('are you single'in self.command) or ('are you there' in self.command) or ('tell me something' in self.command) or ('thank you' in self.command) or ('in your free time' in self.command) or ('i love you' in self.command) or ('can you hear me' in self.command) or ('do you ever get tired' in self.command):
                self.Fun(self.command)
            elif 'time' in self.command : 
                self.Clock_time(self.command)
            elif (('hi' in self.command) and len(self.command)==2) or ((('hai' in self.command) or ('hey' in self.command)) and len(self.command)==3) or (('hello' in self.command) and len(self.command)==5):
                self.comum(self.command)
            elif ('what can you do' in self.command) or ('your name' in self.command) or ('my name' in self.command) or ('university name' in self.command):
                self.Fun(self.command)
            elif ('joke'in self.command) or ('date' in self.command):
                self.Fun(self.command)
     
    #no result found
    def No_result_found(self):
        self.talk('Boss I couldn\'t understand, could you please say it again.')        

startExecution = MainThread()
class Main(QMainWindow):
    cpath =""
    
    def __init__(self,path):
        self.cpath = path
        super().__init__()
        self.ui = Ui_JarvisUI(path=current_path)
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.startTask)
        self.ui.pushButton_3.clicked.connect(self.close)
    
    #NOTE make sure to place a correct path where you are keeping this gifs
    def startTask(self):
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\ironman1.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\ringJar.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\circle.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\lines1.gif")
        self.ui.label_7.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\ironman3.gif")
        self.ui.label_8.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\circle.gif")
        self.ui.label_9.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\powersource.gif")
        self.ui.label_12.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\powersource.gif")
        self.ui.label_13.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\ironman3_flipped.gif")
        self.ui.label_16.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\Sujith.gif")
        self.ui.label_17.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
    
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

current_path = os.getcwd()
app = QApplication(sys.argv)
jarvis = Main(path=current_path)
jarvis.show()
exit(app.exec_())