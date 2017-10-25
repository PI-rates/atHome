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
# ====  data =============
cpp_code = """#include <Arduino.h>

int ledPin_vincent = 3;
int ledPin_pierre = 4;
int ledPin_thomas = 5;

void setup() {
    pinMode(ledPin_vincent, OUTPUT);
    pinMode(ledPin_pierre, OUTPUT);
    pinMode(ledPin_thomas, OUTPUT);
    digitalWrite(ledPin_vincent, %d);
    digitalWrite(ledPin_pierre, %d);
    digitalWrite(ledPin_thomas, %d);
};

void loop(){};
"""

nmap_cmd = "nmap -sP 192.168.1.1-255 | grep %s"

# ======== Initialize ==========
with open("main.cpp", "w") as f:
    f.write(cpp_code %(0, 0, 0))
os.system("make upload -s")

while (1):

    chgt = 0
    # ========= VINCENT =========
    nmap_vincent = os.popen(nmap_cmd %("android-8f93")).readlines()
    
    if nmap_vincent == [] and vincent == 1:
        vincent = 0
        chgt = 1

    elif nmap_vincent != [] and vincent == 0:
        vincent = 1
        chgt = 1
    
    # ========= PIERRE =========
    nmap_pierre = os.popen(nmap_cmd %("Honor_8")).readlines()

    if nmap_pierre == [] and pierre == 1:
        pierre = 0
        chgt = 1

    elif nmap_pierre != [] and pierre == 0:
        pierre = 1
        chgt = 1

    # ========= THOMAS =========
    nmap_thomas = os.popen(nmap_cmd %("iPhonedethomas")).readlines()

    if nmap_thomas == [] and thomas == 1:
        thomas = 0
        chgt = 1

    elif nmap_thomas != [] and thomas == 0:
        thomas = 1
        chgt = 1
    #===========================


    if chgt == 1: 
        with open("main.cpp", "w") as f:
            f.write(cpp_code %(vincent, pierre, thomas))

        os.system("make upload -s")
    print('OK')
