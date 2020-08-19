#include "DHT.h"
#include <VitconBrokerComm.h>
using namespace vitcon;

#define DHTPIN A1 
#define DHTTYPE DHT22
#define SOILHUMI A6

DHT dht(DHTPIN, DHTTYPE);

uint32_t DHT22CaptureDelay = 2000;
uint32_t DHT22Capture_ST = 0;
float Temp;
float Humi;
int Soilhumi;

IOTItemFlo dht22_temp;
IOTItemFlo dht22_humi;
IOTItemInt soilhumi;

#define ITEM_COUNT 3

IOTItem *items[ITEM_COUNT] = {&dht22_temp, &dht22_humi, &soilhumi};

const char device_id[] = "c3fdf9c88abaea8893c751069880f353";
BrokerComm comm(&Serial, device_id, items, ITEM_COUNT);

void setup() {
  Serial.begin(250000);
  comm.SetInterval(200);

  dht.begin();
  pinMode(SOILHUMI, INPUT);
  DHT22Capture_ST = millis();
}

void loop() {
  Soilhumi = map(analogRead(SOILHUMI), 0, 1023, 100, 0);
  
  if (millis() - DHT22Capture_ST > DHT22CaptureDelay) {
    Temp = dht.readTemperature();
    Humi = dht.readHumidity();

    DHT22Capture_ST = millis();
  }
  
  
  dht22_temp.Set(Temp);
  dht22_humi.Set(Humi);
  soilhumi.Set(Soilhumi);
  comm.Run();
}
