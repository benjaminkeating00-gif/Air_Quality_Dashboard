// Combined DHT11 + LCD Display
#include <Arduino.h>
#include <DHT.h>
#include <LiquidCrystal.h>

// DHT11 setup
#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// LCD setup: RS, Enable, D4, D5, D6, D7
LiquidCrystal lcd(12, 11, 7, 6, 5, 4);

void setup() {
  // Start serial and sensors
  Serial.begin(9600);
  dht.begin();
  
  // Start LCD
  lcd.begin(16, 2);
  lcd.clear();
  lcd.print("DHT11 Monitor");
  delay(2000);
}

void loop() {
  // Read sensor
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  
  // Print to serial (for Python)
  Serial.print("Hum: ");
  Serial.print(h);
  Serial.print(" %  Temp: ");
  Serial.print(t);
  Serial.println(" °C");
  
  // Display on LCD
  lcd.clear();
  
  // Line 1: Temperature
  lcd.setCursor(0, 0);
  lcd.print("Temp: ");
  lcd.print(t);
  lcd.print(" C");
  
  // Line 2: Humidity
  lcd.setCursor(0, 1);
  lcd.print("Hum:  ");
  lcd.print(h);
  lcd.print(" %");
  
  delay(50);
}