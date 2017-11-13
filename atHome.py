#!/usr/bin/python
#
# Alume diode connectée au GPIO Raspberry PI si la personne est connectee au WIFI.
# Utilisation de la commande NMAP

import os
import RPi.GPIO as GPIO

# --- Numero de Pin pour chaque personne ----
ledPin_thomas = 1
ledPin_pierre = 2
ledPin_vincent = 3

# --- Initialisation GPIO ----
GPIO.setmode(GPIO.BCM)

GPIO.setup(ledPin_pierre, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ledPin_thomas, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ledPin_vincent, GPIO.OUT, initial=GPIO.LOW)

# --- Variable pour chaque personne ---
vincent = 0
pierre = 0
thomas= 0


# ====================================
# ======== SCAN DU RESEAU ============
# ====================================

while (1):

    chgt = 0

    os.system("nmap -sP 192.168.1.1-255 | grep -E 'android-8f93|Honor_8|iPhonedethomas' > nmap.txt")
    # ========= VINCENT =========
    nmap_vincent = os.popen("grep 'android-8f93' nmap.txt").readlines()

    if nmap_vincent == [] and vincent == 1:
        vincent = 0
        chgt = 1

    elif nmap_vincent != [] and vincent == 0:
        vincent = 1
        chgt = 1

    # ========= PIERRE =========
    nmap_pierre = os.popen("grep 'Honor_8' nmap.txt").readlines()

    if nmap_pierre == [] and pierre == 1:
        pierre = 0
        chgt = 1

    elif nmap_pierre != [] and pierre == 0:
        pierre = 1
        chgt = 1

    # ========= THOMAS =========
    nmap_thomas = os.popen("grep 'iPhonedethomas' nmap.txt").readlines()

    if nmap_thomas == [] and thomas == 1:
        thomas = 0
        chgt = 1

    elif nmap_thomas != [] and thomas == 0:
        thomas = 1
        chgt = 1
    #===========================


    if chgt == 1:
        GPIO.output(ledPin_thomas, thomas)
        GPIO.output(ledPin_pierre, pierre)
        GPIO.output(ledPin_vincent, vincent)

    print('OK')
