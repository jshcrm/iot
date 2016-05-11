#include <PubSubClient.h>
#include <Ethernet.h>
#include <SPI.h>

byte mac[]    = {0xDE, 0xED, 0xBA, 0xFE, 0xFE, 0xEF };
byte ip[] = { 192, 168, 1, 7 };
byte localserver[] = { 192, 168, 1, 2 };

const char clientID[8] = "Arduino";
const char topicName[8] = "IoT/LED";
const int led = 9;

EthernetClient ethClient;
PubSubClient client(localserver, 1883, callback, ethClient);

void readState() {
 int state = digitalRead(led);
 char onoff[4];
 if (state == 1) {
   const char* onoff = "on";
   client.publish(topicName, onoff);
   Serial.print("Pin ");
   Serial.print(led);
   Serial.print(" is ");
   Serial.println(onoff);
 }
 else if (state == 0) {
   const char* onoff = "off";
   client.publish(topicName, onoff);
   Serial.print("Pin ");
   Serial.print(led);
   Serial.print(" is ");
   Serial.println(onoff);
  }
 
}

void callback(char* topic, byte* payload, unsigned int length) {
  int load = atoi ((const char*) payload);
  if (load != 0) {
    Serial.print("\n");
    Serial.print("Payload= ");
    Serial.println(load);
    switch(load) {
      case 1:
        digitalWrite(led, HIGH);
        readState();
        break;
      case 2:
        digitalWrite(led, LOW);
        readState();
        break;
      case 3:
        readState();
      default:
        break;
    }
  }
}

void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  Ethernet.begin(mac, ip);
  
  if (!client.connected()) {
    Serial. print("Trying to connect...");
    client.connect(clientID);
  }
  if (client.connected()) {
    Serial.print("Connected");
    client.subscribe(topicName);
  }
}

void loop() {
  client.loop();
}


