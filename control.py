# from voicecontrol.voice import Voice
from datetime import datetime, time


from MQTT.LightControl import LightControl


# voice = Voice()
controller = LightControl(client_id="Linux PC: ", topic="IoT/LED")
evening_shutoff = time(23, 35, 0, 00000).strftime('%H:%M:%S:%Z')


controller.start()

while True:
	if str(datetime.now().time().strftime('%H:%M:%S:%Z')) == str(evening_shutoff):
		controller.led_on()
	print (evening_shutoff, datetime.now().time().strftime('%H:%M:%S'))

# voice.start()

# while True:

# 	if voice.q.get() == "yes":
# 		controller.led_on()
# 		voice.q.task_done()

# 	elif voice.q.get() == "no":
# 		controller.led_off()
# 		voice.q.task_done()

# 	elif voice.q.get() == "hi":
# 		controller.get_status()
# 		voice.q.task_done()
# 	pass
