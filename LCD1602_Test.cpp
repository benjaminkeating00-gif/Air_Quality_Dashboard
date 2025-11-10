// Simple LCD Test
#include <Arduino.h>
#include <LiquidCrystal.h>

// LCD pins: RS, Enable, D4, D5, D6, D7
LiquidCrystal lcd(12, 11, 7, 6, 5, 4);

void setup() {
  // Initialize LCD
  lcd.begin(16, 2);
  
  // Clear screen and show test message
  lcd.clear();
  lcd.print("LCD Test");
  
  // Move to second line
  lcd.setCursor(0, 1);
  lcd.print("Working!");
}

void loop() {
  // Do nothing - just display the message
}
