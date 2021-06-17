#Imported Modules

from datetime import datetime
import sys
import time
import os
from os import listdir
from os.path import isfile, join
#import requests
import json

#Main Terminal Components

function = ''
isOn = False
count = 0
startup = True
std = False
api_key = "a1789df811984d42dc068e5e118a0666"

#Defined Functions
#Current Time

def currentTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)

#Read File

def fileRead():
    filename = input("")
    mode = 'r'
    text = open(filename,mode)
    print(text.read())
    text.close()

#Clear

def clear():
    os.system('cls')
#Write to File
'''
def fileWrite():
    count = 0
    filename = input("\tFilename ")
    mode = 'a'
    text = open(filename,mode)
    i = int(input("\tLines required? "))
    while count < i:
        text.write(input())
    text.close()
'''

#Change Directory

def cdPath():
    path = str(input("Path? "))
    os.chdir(path)

#List Directory

def ls():
    path = input("Path? ")
    os.listdir(path)

#Shutdown

def shutdown():
    os.system("shutdown /s /t 10")
    std = True

#Reboot

def reboot():
    os.system("shutdown /r /t 10")
    std = True

#Abort

def abort():
    os.system("shutdown /a")
    std = False

#Execute

def exe():
    path = input("Path? ")
    os.startfile(path)

#Weather

def weather():
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = input("Enter city name : ") 
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
    response = requests.get(complete_url) 
    x = response.json() 
    if x["cod"] != "404": 
        y = x["main"] 
        current_temperature = y["temp"] 
        current_pressure = y["pressure"] 
        current_humidiy = y["humidity"] 
        z = x["weather"] 
        weather_description = z[0]["description"] 
        print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) + 
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n description = " +
                    str(weather_description)) 
  
    else: 
        print(" City Not Found ")

#Server

def server():
    #python -m SimpleHTTPServer 8000
    print("Unavaliable in your region")

#Copyright

def copystuffs():
    print("Copyright NerveRift Corporation 2019 - 2021")


#Help

def helps():
    print("\nFull Documentation And Help Can Be Found At: github.com/FederalBR/terminal\n")
#Terminal

def echo(input):
    for y in range(len(input.split()) - 1):
	    print(input.split()[y+1], end=" ", flush=True)
    print("\n")



while isOn == False:
    if startup == True:
        print('Python Terminal Designed For Windows')
        print('Initialising...')
        time.sleep(1)
        os.system('cls')
        print('Python Terminal Designed For Windows')
        startup = False
    function = input(">>> ")
    if function == 'sys.exit':
        isOn = True
    if function == 'time':
        currentTime()
    if function == 'file.read':
        fileRead()
    if function == 'cls':
        clear()
    if function == 'cd':
        cdPath()
    if function == 'shutdown':
        shutdown()
    if function == 'reboot':
        reboot()
    if function == 'abort' and std == True:
        abort()
    if function == 'exe':
        exe()
    #if function == 'weather':
        #weather()
    if function == 'serve':
        server()
    if function == 'copyright':
        copystuffs()
    if function == 'help':
        helps(function)
    if function == '' or function == ' ':
        print("\n")
    if (function.split()[0]) == "echo":
        echo(function)
    else:
        print("\n\tInvalid Function\n")
        
sys.exit
