
# Simple Arduino Reader
import datetime as dt 
import serial
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Connect to Arduino
arduino = serial.Serial('COM3', 9600)
time.sleep(2)

def Celcius_to_Fahrenheit(c):
    return (c * 9/5) + 32

i = 0
humidity_data = []
temp_data = []
timestamps = []
while i<10:
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

    time.sleep(0.1)
    i+=1

df = pd.DataFrame({'humidity': humidity_data, 'temperature': temp_data, 'timestamp': timestamps})

print(df.columns)
print("\n" * 2)
print(df)


plt.figure(figsize=(10, 6))


plt.subplot(2, 1, 1)
plt.plot(df['timestamp'], df['humidity'], 'blue')
plt.title('Humidity')
plt.ylabel('Humidity %')
plt.xticks(df['timestamp'][::5], rotation=45)

plt.subplot(2, 1, 2)
plt.plot(df['timestamp'], df['temperature'], 'red')
plt.title('Temperature')
plt.ylabel('Temperature °C')
plt.xlabel('Time')
plt.xticks(df['timestamp'][::5], rotation=45)

plt.tight_layout()

plt.show()


