#include "DHT.h"
#include <VitconBrokerComm.h>
using namespace vitcon;
#include <SoftPWM.h>

#define DHTPIN A1 
#define DHTTYPE DHT22
#define SOILHUMI A6
#define PUMP 16
#define LAMP 17
SOFTPWM_DEFINE_CHANNEL(A3)

DHT dht(DHTPIN, DHTTYPE);

uint32_t DHT22CaptureDelay = 2000;
uint32_t DHT22Capture_ST = 0;
float Temp;
float Humi;
int Soilhumi;
bool fan_out_status;
bool pump_out_status;
bool lamp_out_status;

void fan_out(bool val) {
  fan_out_status = val;
}
void pump_out(bool val) {
  pump_out_status = val;
}
void lamp_out(bool val) {
  lamp_out_status = val;
}

IOTItemFlo dht22_temp;
IOTItemFlo dht22_humi;
IOTItemInt soilhumi;
IOTItemBin FanStatus;
IOTItemBin Fan(fan_out);
IOTItemBin PumpStatus;
IOTItemBin Pump(pump_out);
IOTItemBin LampStatus;
IOTItemBin Lamp(lamp_out);

#define ITEM_COUNT 9

IOTItem *items[ITEM_COUNT] = {&dht22_temp, &dht22_humi, &soilhumi, &FanStatus, &Fan, &PumpStatus, &Pump, &LampStatus, &Lamp};

const char device_id[] = "c3fdf9c88abaea8893c751069880f353";
BrokerComm comm(&Serial, device_id, items, ITEM_COUNT);



void setup() {
  Serial.begin(250000);
  comm.SetInterval(200);

  dht.begin();
  SoftPWM.begin(490);
  pinMode(SOILHUMI, INPUT);
  pinMode(PUMP, OUTPUT);
  pinMode(LAMP, OUTPUT);
  DHT22Capture_ST = millis();
}

void loop() {
  Soilhumi = map(analogRead(SOILHUMI), 0, 1023, 100, 0);
  
  if (millis() - DHT22Capture_ST > DHT22CaptureDelay) {
    Temp = dht.readTemperature();
    Humi = dht.readHumidity();

    DHT22Capture_ST = millis();
  }
  
  if (fan_out_status == true) SoftPWM.set(60);
  else SoftPWM.set(0);
  //digitalWrite(PUMP, pump_out_status)
  digitalWrite(PUMP, LOW);
  digitalWrite(LAMP, lamp_out_status);
  
  dht22_temp.Set(Temp);
  dht22_humi.Set(Humi);
  soilhumi.Set(Soilhumi);
  FanStatus.Set(fan_out_status);
  PumpStatus.Set(digitalRead(PUMP));
  LampStatus.Set(digitalRead(LAMP));
  comm.Run();
}
