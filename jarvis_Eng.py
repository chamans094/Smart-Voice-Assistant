from pip import main
import pyttsx3
import speech_recognition as sr
import webbrowser as web 
import datetime
import pyjokes
import os
import time
import subprocess
import pywhatkit
import wikipedia as googleScrap
import random
import smtplib as sm
from flask import Flask
import sys
import json
import requests

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisGui_3 import Ui_jarvisGui

# Function for playing alarm ringtone of System Music... 
def playAlarmSound():
	address = "C:\\Users\\Chaman\\Music\\Video Projects"
	songs_list = os.listdir(address)
	os.startfile(os.path.join(address, songs_list[1]))

# Function for weather...
def weather(city_name):
	api_key="1e1688c0636223e2671af0c6859def8f"
	base_url="https://api.openweathermap.org/data/2.5/weather?"
	complete_url = base_url + "appid=" + api_key + "&q=" + city_name
	response = requests.get(complete_url)
	x = response.json()

	if x["cod"] != "404":
		y = x["main"]
		current_temp = int(y["temp"] - 273.15)
		current_humidiy = y["humidity"]
		z = x["weather"]
		weather_description = z[0]["description"]
		print("\nTemperature in " + city_name + " is : " + str(round(current_temp, 0)) + " Celsius\n"
		      + "Humadity in " + city_name + " is : " + str(current_humidiy) +" %\n"
			  + "Description : " + str(weather_description))
		speak("temperature in" + city_name + " is " + str(round(current_temp, 0)) + " degree celsius")
		speak("and humidity in " + city_name + " is " + str(current_humidiy) + " percent")
		speak("now the weather description is " + weather_description)

	else:
		print("\nCity Not Found!!!, Please speak correct city name")
		speak("city not found, please speak correct city name")

# Function for sending Email via Gmail...
def sendEmail(msg):
	ob = sm.SMTP("smtp.gmail.com", 587)
	ob.ehlo()
	ob.starttls()
	speak("enter e-mail, from which e-mail id do you want to send")
	Email = input("Enter e-mail, From which e-mail id do you want to send : ")
	speak("please enter password")
	password = input("Enter password : ")
	speak("enter e-mail, from which e-mail id do you want to send")
	toEmail = input("Enter e-mail, To which e-mail id do you want to send : ")
	ob.login(Email, password)
	ob.sendmail(Email, toEmail, msg)
	ob.quit()

# Function for playing random song of System Music and 
# printing all songs those are present in the folder...
def playMusic():
	address = "C:\\Users\\Chaman\\Music\\Video Projects"
	songs_list = os.listdir(address)
	os.startfile(os.path.join(address, random.choice(songs_list)))
	print("\nThe list of songs are given below...\n")
	for song in songs_list:
		print(song)

# Function for converting any text in to voice...
def speak(x):
	engine = pyttsx3.init("sapi5")
	voices = engine.getProperty("voices")
	engine.setProperty("voice", voices[0].id)
	rate = engine.getProperty("rate")
	engine.setProperty("rate", 150)
	print(" ")
	engine.say(x)
	engine.runAndWait()

# Class for MainThread...
class MainThread(QThread):
	def __init__(self):
		super(MainThread, self).__init__()

	def run(self):
		self.TaskExecution()

	def TakeCommand(self):  # Function for converting the voice into text form...
		recognizer = sr.Recognizer()
		with sr.Microphone() as source:
			print("\nSay something... *****I'm listening here*****")
			recognizer.pause_threshold = 1
			recognizer.adjust_for_ambient_noise(source)
			audio = recognizer.listen(source)
			try:
				print("\nRecognizing...")
				data = recognizer.recognize_google(audio, language="en-in")
				return data
			except sr.UnknownValueError:
				print("\nCould not understand your voice.\nPlease speak carefully...\nThanks for using...\n")
				speak("Could not understand your voice.")
				speak("please speak carefully")
				speak("thanks for using")

	def TaskExecution(self):  # Function for task execution...	
		
		# For declaring time and date... 
		Nowtime = datetime.datetime.now().strftime("%I : %M %p")
		hr = int(Nowtime[0: 2])
		amPm = Nowtime[8: 10]
		date = datetime.datetime.now().strftime("Today date is : %B %d, %Y")

		# For wishing according to time...
		if hr <= 9 and amPm == "AM":
			print("\nGood morning sir... its - " +Nowtime )
			speak("good morning sir")
			speak("its" + Nowtime)
		elif 10 <= hr <= 11 and amPm == "AM":
			print("\nGood noon sir... its - " + Nowtime)
			speak("good noon sir")
			speak("its" + Nowtime)
		elif (hr == 12 or 1 <= hr <= 4) and amPm == "PM":
			print("\nGood afternoon sir... its - " + Nowtime)
			speak("good afternoon sir")
			speak("its" + Nowtime)
		elif (5 <= hr <= 11) and amPm == "PM":
			print("\nGood evening sir... its - " + Nowtime)
			speak("good evening  sir")
			speak("its" + Nowtime)

		print("\n*************** INSTRUCTIONS ***************")
		print("1. The name of voice assistant : JARVIS")
		print("2. Please wait THREE seconds after every task")
		print("\nJARVIS here...\nhow may i help you?")
		speak("jarvis here")
		speak("how may i help you")

		while True:

				# For declaring time and date... 
				Nowtime = datetime.datetime.now().strftime("%I : %M %p")
				hr = int(Nowtime[0: 2])
				amPm = Nowtime[8: 10]
				date = datetime.datetime.now().strftime("Today date is : %B %d, %Y")
				
				self.query = self.TakeCommand().lower()

				if "your name" in self.query: 			# For speaking voice assistant name...
					print("You said : " + self.query)
					print("My answer : My name is jarvis")
					print("how may i help you?")
					speak("my name is jarvis")
					speak("how may i help you")

				elif "how are you" in self.query:
					print("You said : " + self.query)
					print("My answer : I am fine sir\nwhat about you?\nhow may i help you?")
					speak("i am fine sir")
					speak("what about you")
					speak("how may i help you")

				elif "hello" in self.query:
					print("\nhello sir\nhow may i help you?")
					speak("hello sir")
					speak("how may i help you")

				elif "what are you doing" in self.query:
					print("You said : " + self.query)
					print("My answer : Right now i am trying to doing your help\nwhat can i do for you now?")
					speak("right now i am trying to doing your help")
					speak("what can i do for you now")

				elif "open youtube" in self.query or "youtube" in self.query:		# For opening youtube...
					print("You said : " + self.query)
					print("what do you want to search on youtube?")
					speak("what do you want to search on youtube")
					self.query = self.TakeCommand().lower()
					print("You said : " + self.query)
					web.open("https://www.youtube.com/results?search_query=" + self.query)
					print("\nMy answer : Ok sir your Youtube search has been opened please enjoy.")
					speak("ok sir")
					speak(self.query + "is opend on youtube enjoy your videos.")

				elif "open firefox" in self.query:		 # For opening Firefox...
					print("You said : " + self.query)
					subprocess.Popen("firefox.exe")
					print("\nMy answer : Ok sir Firefox has been opened please enjoy.")
					speak("ok sir")
					speak("firefox has been opend.")

				elif "open gmail" in self.query: 			# For opening Gmail...
					print("You said : " + self.query)
					web.open("https://mail.google.com/mail/u/0/#inbox")
					print("\nMy answer : Ok sir Gmail has been opened")
					speak("ok sir")
					speak("gmail has been opened")

				elif "open whatsapp" in self.query: 		# For opening Whatsapp...
					print("You said : " + self.query)
					web.open("https://web.whatsapp.com/")
					print("\nMy answer : Ok sir Whatsapp has been opened")
					speak("ok sir")
					speak("whatsapp has been opened")

				elif "joke" in self.query: 			# For speaking a english joke...
					print("You said : " + self.query)
					joke1 = pyjokes.get_jokes(language="en", category="neutral")
					print("\nMy answer : joke printed below...")
					print(joke1)
					speak(joke1)

				elif "play music" in self.query or "system music" in self.query or "system song" in self.query: 	# For opening system music...
					print("You said : " + self.query)
					playMusic()
					speak("system music has been played.")

				elif "alarm" in self.query:			# For setting alarm...
					print("You said : " + self.query)
					speak("please enter the time")
					alarmTime = input(": Time input format =hh:mm:AM/PM\nEnter the time :")
					while True:
						Nowtime1 = datetime.datetime.now().strftime("%I:%M:%p")
						if Nowtime1 == alarmTime:
							speak("its time to wake up sir")
							playAlarmSound()
							time.sleep(27)
							speak("its time to wake up sir")
							speak("alarm closed")
							break		
					break
				
				elif "temperature" in self.query or "weather" in self.query:
					print("You said : " + self.query)
					speak("please tell me the city name")
					city = self.TakeCommand().lower()
					weather(city)

				elif "music online" in self.query or "online music" in self.query:	 # For opening online music on jio savan...
					print("You said : " + self.query)
					web.open("https://www.jiosaavn.com/")
					print("\nMy answer : Ok sir I have to play music online on jio saavan for you")
					speak("ok sir")
					speak("i have to play music online on jio saavan for you")

				elif "calculator" in self.query: 	# For opening calculator...
					print("You said : " + self.query)
					subprocess.Popen("calc.exe")
					print("\nMy answer : Ok sir Calculator has been opened")
					speak("ok sir")
					speak("calculator has been opened")

				elif "paint" in self.query: 			# For opening paint...
					print("You said : " + self.query)
					subprocess.Popen("pbrush.exe")
					print("\nMy answer : Ok sir Paint has been opened")
					speak("ok sir")
					speak("paint has been opened")

				elif "sublime" in self.query:		 # For opening sublime text...
					print("You said : " + self.query)
					subprocess.Popen("C:\\Program Files\\Sublime Text\\sublime_text.exe")
					print("\nMy answer : Ok sir Sublime text has been opened")
					speak("ok sir")
					speak("sublime text has been opened")

				elif "notepad" in self.query:		 # For opening Notepad...
					print("You said : " + self.query)
					subprocess.Popen("notepad.exe")
					print("\nMy answer : Ok sir Notepad has been opened")
					speak("ok sir")
					speak("notepad has been opened")

				elif "ms word" in self.query or "open word" in self.query : 		# For opening MS word...
					print("You said : " + self.query)
					subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
					print("\nMy answer : Ok sir MS word has been opened")
					speak("ok sir")
					speak("ms word has been opened")

				elif "excel" in self.query:     		# For opening MS Excel...
					print("You said : " + self.query)
					subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
					print("\nMy answer : Ok sir MS Excel has been opened")
					speak("ok sir")
					speak("excel has been opened")

				elif "powerpoint" in self.query:		 # For opening MS powerpoint...
					print("You said : " + self.query)
					subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
					print("\nMy answer : Ok sir Powerpoint has been opened")
					speak("ok sir")
					speak("powerpoint has been opened")

				elif "cmd" in self.query or "terminal" in self.query:
					print("You said : " + self.query)
					subprocess.Popen("wt.exe")
					print("\nMy answer : Ok sir Terminal has been opened")					
					speak("ok sir")
					speak("terminal has been opened")

				elif "vs code" in self.query or "visual studio code" in self.query: 			# For opening VS code...
					print("You said : " + self.query)
					subprocess.Popen("C:\\Users\\Chaman\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
					print("\nMy answer : Ok sir VS code has been opened")
					speak("ok sir")
					speak("VS code has been opened")

				elif "time" in self.query: 			# For opening and speaking time...
					print("You said : " + self.query)
					print("\nMy answer : Ok sir now the time = " + Nowtime)
					speak("now the time is" + Nowtime)

				elif "date" in self.query:			 # For opening and speaking date...
					print("You said : " + self.query)
					print("\nMy answer : Ok sir today date is : " + date)
					speak("today date is" + date)

				elif "wish" in self.query: 			# For wishing according to time...
					if (hr <= 9) and amPm == "AM":
						print("\nGood morning sir... its - " +Nowtime )
						speak("good morning sir")
						speak("its" + Nowtime)
					elif (10 <= hr <= 11) and amPm == "AM":
						print("\nGood noon sir... its - " + Nowtime)
						speak("good noon sir")
						speak("its" + Nowtime)
					elif (hr == 12 or 1 <= hr <= 4) and amPm == "PM":
						print("\nGood afternoon sir... its - " + Nowtime)
						speak("good afternoon sir")
						speak("its" + Nowtime)
					elif (5 <= hr <= 11) and amPm == "PM":
						print("\nGood evening sir... its - " + Nowtime)
						speak("good evening  sir")
						speak("its" + Nowtime)
					print("how may i help you?")
					speak("how may i help you")
				
				elif "wikipedia" in self.query or "wiki" in self.query: 		# For searching anything on wikipedia...
					self.query = self.query.replace("wikipedia", "")
					result = googleScrap.summary(self.query, 2)
					print("You said : " + self.query)
					print("\nAccording to wikipedia : " + result)
					try:			
						pywhatkit.search(self.query + "wikipedia")
						speak("according to wikipedia" + result)
						
					except:
						speak("this may not searchable data")

				elif "open google" in self.query or "search on google" in self.query: # For searching anything on google...
					print("You said : " + self.query)
					print("What do you want to search on google?")
					speak("What do you want to search on google")
					self.query = self.TakeCommand().lower()
					print("You said : " + self.query)
					pywhatkit.search(self.query)
					speak("your input has been opened on google")

				elif "send email" in self.query:
					print("First of all, please tell me message sir")
					speak("first of all: please tell me message sir")
					Message1 = self.TakeCommand().lower()
					sendEmail(Message1)
					speak("ok sir sending email")
					print("***Email has been sent!***")
					speak("email has been sent")

				elif "quit"in self.query or "exit"in self.query or "stop" in self.query or "ok bye" in self.query or "nothing" in self.query: # For Exit...
					print("You said : " + self.query)
					print("\nMy answer : Now Exit...\nOk bye...\nThanks for using\nHave a good day\n")
					speak("ok byee thanks for using")
					speak("have a good day")
					break

				else:                                 # For searching anything on google...
					print("You said : " + self.query)
					pywhatkit.search(self.query)
					speak("these are results on web")
					
				time.sleep(3)

# For start execution...
startExecution = MainThread()

class Main(QMainWindow):

	def __init__(self):
		super().__init__()
		self.ui = Ui_jarvisGui()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.startTask)
		self.ui.pushButton_2.clicked.connect(self.close)

	def startTask(self):
		self.ui.movie = QtGui.QMovie("../jarvis/jarvis_1.gif")
		self.ui.label.setMovie(self.ui.movie)
		self.ui.movie.start()

		self.ui.movie = QtGui.QMovie("../jarvis/jarvis_2.gif")
		self.ui.label_2.setMovie(self.ui.movie)
		self.ui.movie.start()

		self.ui.movie = QtGui.QMovie("../jarvis/jarvis_3.gif")
		self.ui.label_3.setMovie(self.ui.movie)
		self.ui.movie.start()

		timer = QTimer(self)
		timer.timeout.connect(self.showTime)
		timer.start(1000)
		startExecution.start()

	def showTime(self): # For showing time and date in jarvis GUI...
		current_time = QTime.currentTime()
		current_date = QDate.currentDate()
		label_time = current_time.toString("hh:mm:ss AP")
		label_date = current_date.toString("dd/MM/yyyy")
		self.ui.textBrowser.setText(label_date)
		self.ui.textBrowser_2.setText(label_time)

# The main program will be start here...
if __name__ == "__main__":
		app = QApplication(sys.argv)
		jarvis = Main()
		jarvis.show()
		exit(app.exec_())