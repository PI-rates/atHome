#!/usr/bin/python
#
# Alume diode ARDUINO si la personne est connectee au WIFI.
# Utilisation de la commande NMAP 
#


import os
import time

vincent = 0
pierre = 0
thomas= 0
# ====  initialisation des diodes a 0 =============
os.system("echo '#include <Arduino.h>\n int ledPin_vincent =  3;int ledPin_pierre = 4;int ledPin_thomas=5;void setup() {pinMode(ledPin_vincent, OUTPUT);pinMode(ledPin_pierre, OUTPUT);pinMode(ledPin_thomas, OUTPUT);digitalWrite(ledPin_vincent,"+str(vincent)+");digitalWrite(ledPin_pierre,"+str(pierre)+");digitalWrite(ledPin_thomas,"+str(thomas)+");};void loop(){};' > main.cpp")

os.system("make upload -s")

while (1):

    chgt = 0
    # ========= VINCENT =========
    nmap_vincent = os.popen("nmap -sP 192.168.1.1-255 | grep 'android-8f93'").readlines()
    
    if nmap_vincent == [] and vincent == 1:
        vincent = 0
        chgt = 1

    elif nmap_vincent != [] and vincent == 0:
        vincent = 1
        chgt = 1
    
    # ========= PIERRE =========
    nmap_pierre = os.popen("nmap -sP 192.168.1.1-255 | grep 'Honor_8'").readlines()

    if nmap_pierre == [] and pierre == 1:
        pierre = 0
        chgt = 1

    elif nmap_pierre != [] and pierre == 0:
        pierre = 1
        chgt = 1
    #==========================

    # ========= THOMAS =========
    nmap_thomas = os.popen("nmap -sP 192.168.1.1-255 | grep 'iPhonedethomas'").readlines()

    if nmap_thomas == [] and thomas == 1:
        thomas = 0
        chgt = 1

    elif nmap_thomas != [] and thomas == 0:
        thomas = 1
        chgt = 1
    #===========================


    if chgt == 1: 
        os.system("echo '#include <Arduino.h>\n int ledPin_vincent =  3;int ledPin_pierre = 4;int ledPin_thomas=5;void setup() {pinMode(ledPin_vincent, OUTPUT);pinMode(ledPin_pierre, OUTPUT);pinMode(ledPin_thomas, OUTPUT);digitalWrite(ledPin_vincent,"+str(vincent)+");digitalWrite(ledPin_pierre,"+str(pierre)+");digitalWrite(ledPin_thomas,"+str(thomas)+");};void loop(){};' > main.cpp")
        os.system("make upload -s")
    print('OK')
