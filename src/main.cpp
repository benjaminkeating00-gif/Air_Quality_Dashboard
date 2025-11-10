#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  Serial.print("Hum: ");
  Serial.print(h);
  Serial.print(" %  Temp: ");
  Serial.print(t);
  Serial.println(" °C");

  delay(50);
}
