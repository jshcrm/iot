import paho.mqtt.client as mqtt
from threading import Thread


class MqttHandler(Thread):

	QOS = 0
	IPADDRESS = '192.168.1.2'
	PORT = 1883

	def __init__(self, client_id, topic):
		Thread.__init__(self)
		self.daemon = True

		self.client_id = client_id
		self.topic = topic
		self.client = mqtt.Client(client_id=self.client_id, clean_session=False)

		self.client.on_connect = self.on_connect
		self.client.on_subscribe = self.on_subscribe
		self.client.on_message = self.on_message
		self.client.on_publish = self.on_publish
		self.client.on_disconnect = self.on_disconnect

		self.client.connect(self.IPADDRESS, self.PORT)
		self.client.subscribe(self.topic, self.QOS)

	def run(self):
		while True:
			self.client.loop()

	def on_connect(self, client, userdata, flags, rc):
		self.client.publish(self.topic, "Connected")
		print(self.client_id + "Connected")

	def on_subscribe(self, client, userdata, mid, granted_qos):
		self.client.publish(self.topic, payload="3")
		print(self.client_id + "Subscribed to " + self.topic)

	def on_publish(self, client, userdata, mid):
		pass

	def on_message(self, client, userdata, message):
		print(self.client_id + str(message.payload) + '\n')

	def on_disconnect(self, client, userdata, rc):
		print(self.client_id + "Client Disconnected")
