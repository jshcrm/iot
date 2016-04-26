from threading import Thread
import speech_recognition as sr
from queue import Queue


# Voice is initiated from Amy.py as a thread, the queue
# data from the microphone is returned to Amy for processing

class Voice(Thread):

	def __init__(self):
		Thread.__init__(self)
		self.daemon = True

	def run(self):
		self.q = Queue()
		self.r = sr.Recognizer()
		with sr.Microphone() as source:
			while True:
				self.mainfunction(source)

	def mainfunction(self, source):
		audio = self.r.listen(source)
		user = self.r.recognize_sphinx(audio)
		print(user)

		if user == 'yes':
			self.q.put('yes')
		elif user == 'no':
			self.q.put('no')
		elif user == 'hi':
			self.q.put('hi')
