# Description: Python Radio player
# Author: l0gg3r
# Source: https://github.com/damian1421/python/radios.py

import os, subprocess

clear = lambda: os.system('clear')
sleep = lambda: os.system('sleep 1')
play = lambda x: subprocess("mpv $x")
print("Radios", "by l0gg3r")
clear()
#Here goes a menu that iterates between numbers of items and lines of another file with urls.
# 1- Vale 97.5 https://vale97.5/online.m3u
print("1- FM 97.5	- Vale 97.5")
print("2- FM 99.9	- La 100")
print("3- FM 104.3	- Urbana Play")
choice = input("Choose a number: ")
sleep ()
print("Loading stream: ",choice)
play(choice) #Not working yet
