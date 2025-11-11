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

i = 0
humidity_data = []
temp_data = []
timestamps = []
first_write = True

while True:
    data = arduino.readline().decode('utf-8').strip()
    if "Hum:" in data:
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

    time.sleep(2)  # 2 seconds
    

print(f"Collected {len(humidity_data)} readings!")