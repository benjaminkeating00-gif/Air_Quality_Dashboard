# Air Quality Monitor (Arduino + Python + Flask)

This project is a simple end-to-end air-quality monitor built using an Arduino, an MQ-135 gas sensor, a DHT11 temperature/humidity sensor, and a Flask server for live visualization. The Arduino streams temperature, humidity, and raw MQ-135 readings over serial, Python parses the data and writes to a CSV, and the Flask dashboard displays everything live using Plotly.

![Hardware Setup](https://github.com/user-attachments/assets/d77046b5-34fe-4972-a945-8e1a8abf07fa)

A notable part of this project is the first-order linear correction model I built for the MQ-135. I used a two-variable Taylor approximation (temperature and humidity), normalized it using several hours of baseline RS data, and pulled the αT and αRH coefficients from the MQ-135 datasheet. This keeps the sensor calibrated around real indoor conditions (20–30 °C) and avoids the overly aggressive approximations you see in broader temperature-range models.

**[RS_extreme_cases.pdf](https://github.com/user-attachments/files/23633564/RS_extreme_cases.pdf)**

<img width="100%" alt="Flask Server" src="https://github.com/user-attachments/assets/3938a0a8-33e6-43df-967b-09c0ce4f3d63" />
