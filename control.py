from voicecontrol.voice import Voice
from MQTT.LightControl import LightControl


voice = Voice()
controller = LightControl("Linux PC: ", "IoT/LED")

controller.start()
voice.start()

while True:

	if voice.q.get() == "yes":
		controller.led_on()
		voice.q.task_done()

	elif voice.q.get() == "no":
		controller.led_off()
		voice.q.task_done()

	elif voice.q.get() == "hi":
		controller.get_status()
		voice.q.task_done()

	pass

#class Amy(object):

#	def __init__(self):
#		pass
