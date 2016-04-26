from .MqttHandler import MqttHandler


class LightControl(MqttHandler):

	def led_on(self):
		self.client.publish(self.topic, payload="1")
		print(self.client_id + "LED is ON")

	def led_off(self):
		self.client.publish(self.topic, payload="2")
		print(self.client_id + "LED is OFF")

	def get_status(self):
		self.client.publish(self.topic, payload="3")
