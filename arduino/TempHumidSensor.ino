#include <PubSubClient.h>
#include <Ethernet.h>
#include <SPI.h>
#include <dht.h>
#include <stdlib.h>

dht DHT;

#define DHT11_PIN 7

byte mac[] = {0xDE, 0xED, 0xBA, 0xFE, 0xFE, 0xEF };
byte ip[] = { 192, 168, 1, 6 };
byte localserver[] = { 192, 168, 1, 2 };

const char clientID[12] = "temperature";
const char topicName[18] = "home/bedroom/temp";

EthernetClient ethClient;
PubSubClient client(localserver, 1883, callback, ethClient);

void callback(char* topic, byte* payload, unsigned int length) {
  
}

void setup() {
  Serial.begin(9600);
  Ethernet.begin(mac, ip);
  
  if (!client.connected()) {
    Serial. print("Trying to connect...");
    client.connect(clientID);
  }
  if (client.connected()) {
    Serial.print("Connected");
  }
}

void loop() {
  client.loop();
  int chk = DHT.read11(DHT11_PIN);
  char temperature[3];
  char humidity[3];
  char* temp = dtostrf(DHT.temperature, 2, 0, temperature); 
  char* humid = dtostrf(DHT.humidity, 2, 0, humidity); 
  Serial.print("\n");
  Serial.print("Temperature = ");
  Serial.println(temp);
  Serial.print("Humidity = "); 
  Serial.println(humid);
  client.publish(topicName, temp);
//  client.publish(topicName, humid);
  delay(5000);
}


