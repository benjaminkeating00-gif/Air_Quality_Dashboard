# Simple Arduino Reader
import datetime as dt 
import serial
import time
import os


arduino = serial.Serial('COM3', 9600)
time.sleep(2)

def Celcius_to_Fahrenheit(c):
    return (c * 9/5) + 32

# Make data folder
os.makedirs('./data', exist_ok=True)


humidity_data = []
temp_data = []
timestamps = []
first_write = True

while True:
    # Clear any old data in the buffer
    arduino.flushInput()
    
    # Wait for fresh data from Arduino
    data = arduino.readline().decode('utf-8').strip()
    
    if "Hum:" in data:
        print('Processing sensor data')
        print(data)
        # Extract humidity value
        h = data.split("Hum: ")[1].split(" %")[0]
        # Extract temperature value  
        t = data.split("Temp: ")[1].split(" °C")[0]
        humidity_data.append(float(h))
        temp_data.append(float(t))
        timestamps.append(dt.datetime.now().strftime("%M:%S.%f")[:-3])
        
        # Save to CSV for website
        with open('./data/logs.csv', 'a') as f:
            if first_write:
                f.write("ts,tempC,humidity\n")
                first_write = False
            temp_f = Celcius_to_Fahrenheit(float(t))
            f.write(f"{dt.datetime.now().isoformat()},{t},{h}\n")
            print(f"Saved: {t}°C ({temp_f:.1f}°F), {h}% humidity")
        
        # Sleep after processing data
        time.sleep(2)
        continue  # Go back to start of while loop
    
    # Small delay when no data found
    time.sleep(0.1)
