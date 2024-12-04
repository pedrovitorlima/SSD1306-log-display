from PiicoDev_SSD1306 import create_PiicoDev_SSD1306
from time import sleep, strftime
import os

# Initialize OLED
oled = create_PiicoDev_SSD1306()

def get_cpu_temp():
    # Read CPU temperature
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
        temp = int(file.read()) / 1000
    return temp

while True:
    # Clear the display
    oled.fill(0)
    
    # Get system info
    current_time = strftime("%H:%M:%S")
    cpu_temp = get_cpu_temp()
    
    # Display info
    oled.text("System Info", 0, 0)
    oled.text(f"Time: {current_time}", 0, 16)
    oled.text(f"CPU Temp: {cpu_temp:.1f}C", 0, 32)
    
    # Update the display
    oled.show()
    
    # Update every second
    sleep(1)
