
#!/usr/bin/env python

import paho.mqtt.client as mqtt
import time
#import RPi.GPIO as GPIO
import pygame

            



def on_connect(client, userdata, flags, rc):
    print ("Connected with rc: " + str(rc))
    client.subscribe("hepta/audio/head02")

def on_message(client, userdata, msg):
    print ("Topic: "+ msg.topic+"\nMessage: "+str(msg.payload))
    if "pylon8" in str(msg.payload):
        print(str(msg.payload))
        #GPIO.output(11, True)
        pygame.mixer.music.load("8.mp3")
        pygame.mixer.music.play()
    elif "pylon9" in str(msg.payload):
        print(str(msg.payload))
        #GPIO.output(12, True)
        pygame.mixer.music.load("9.mp3")
        pygame.mixer.music.play()
 
    
    
client = mqtt.Client()
client.connect("192.168.178.29", 1883 )
print ("TEST") 
client.on_connect = on_connect
client.on_message = on_message


pygame.mixer.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()




client.loop_forever()



