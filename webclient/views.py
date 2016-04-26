from flask import render_template
from . import webclient
from MQTT.LightControl import LightControl

controller = LightControl("WebClient: ", "IoT/LED")


@webclient.route('/')
@webclient.route('/index')
def index():
	return render_template('index.html')


@webclient.route('/on')
def on():
	controller.led_on()
	return render_template('on.html')


@webclient.route('/off')
def off():
	controller.led_off()
	return render_template('off.html')


@webclient.route('/status')
def status():
	controller.get_status()
	return render_template('status.html')
