# importeer nodioge modules
from gpiozero import Button
import RPi.GPIO as GPIO
import time
import requests
import datetime
from interface import startWebInterface
from queue import Queue
import subprocess

gateSensor = Button(22, pull_up = 0)
URL = "https://michael2222.pythonanywhere.com/status"
active = True
gate = "closed"

# Run the other script
subprocess.run(["python", "C:\scripts\other.py"])

try:
    queue = Queue()
    startWebInterface(queue)
except Exception as e:
    print(e, " erroor")

def changeGate():
    active = True
    toggle_interval = 0.2  # Interval in seconds
    while active:
        start_time = time.time()
        GPIO.output(12, GPIO.HIGH)
        # Wait until the desired interval is reached
        while time.time() - start_time < toggle_interval:
            pass
        GPIO.output(12, GPIO.LOW)
        # Wait until the desired interval is reached
        while time.time() - start_time < 2 * toggle_interval:
            active = False

while True: 
    if gateSensor.is_pressed:
        gate = "closed"
    else:
        gate = "opened"
    data = queue.get()
    if (data != gate & len(data != 0)):
        changeGate()
        if data == gate:
            winData = dict()
            winData["gateStatus"]= gate
            winData["lastTimeChanged"]= str(datetime.datetime.now())[2:]
            requests.post(url = "https://michael2222.pythonanywhere.com/status" , json = winData)
    else: 
        queue.put(data)
    