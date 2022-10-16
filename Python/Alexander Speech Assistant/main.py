#Alexander Speech Assistant
#This assistant listens for user voice commands and uses google speech recognition to reply to questions
#as well as perform google searches and look up a location on google maps.

import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record_audio(question = False):
	with sr.Microphone() as source:
		if question:
			alexander_speak(question)
		try:
			audio = r.listen(source,timeout=1,phrase_time_limit=10)
		except sr.WaitTimeoutError:
			return ''
		voice_data = ''
		try:
			voice_data = r.recognize_google(audio)
		except sr.UnknownValueError:
			alexander_speak('Sorry, I didn\'t get that.')
		except sr.RequestError:
			alexander_speak('Sorry, my speech service is down.')
		return voice_data

def alexander_speak(audio_string):
	tts = gTTS(text=audio_string, lang='en')
	r = random.randint(1,10000000)
	audio_file = 'audio-'+str(r)+'.mp3'
	tts.save(audio_file)
	playsound.playsound(audio_file)
	print(audio_string)
	os.remove(audio_file)

def respond(voice_data):
	if 'what is your name' in voice_data:
		alexander_speak('My name is Alexander')
	if 'what time is it' in voice_data:
		alexander_speak(ctime())
	#If command is to search for an item on google
	if 'search' in voice_data:
		search = record_audio('what do you want to search for')
		url = 'https://google.com/search?q=' + search
		webbrowser.get().open(url)
		alexander_speak('Here is what I found for ' + search)

	#if command is to find a location
	if 'find location' in voice_data:
		location = record_audio('what is the location')
		url = 'https://google.nl/maps/place/' + location + '/&amp;'
		webbrowser.get().open(url)
		alexander_speak('Here is the location of ' + location)

	#Exit command
	if 'exit' in voice_data:
		exit()

#Start of the program
alexander_speak("Hello! What can I help you with?")
time.sleep(1)
while 1:
	voice_data = record_audio()
	respond(voice_data)
