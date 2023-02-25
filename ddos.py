#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Name: Torpeda - superfast SMS bomber for Android.
# Author: nordbearbot
# Date: 21/01/22
# Version: 0.0.1.
#
# ████████  ██████  ██████  ██████  ███████ ██████   █████  
#    ██    ██    ██ ██   ██ ██   ██ ██      ██   ██ ██   ██ 
#    ██    ██    ██ ██████  ██████  █████   ██   ██ ███████ 
#    ██    ██    ██ ██   ██ ██      ██      ██   ██ ██   ██ 
#    ██     ██████  ██   ██ ██      ███████ ██████  ██   ██ 

from os import name, system
from os.path import exists, isfile
from random import choice, randint
from threading import Thread
from time import sleep
from colorama import Fore, Style
from requests import get, post
from user_agent import generate_user_agent
from termcolor import colored

# Banner / Баннер
def banner():
    system("cls" if name == "nt" else "clear")
    print(colored( '''
   _____      _                             _____              
  / ____|    (_)                           |_   _|             
 | |     _ __ _ _ __ ___  ___  ___  _ __     | |  _ __   ___   
 | |    | '__| | '_ ` _ \/ __|/ _ \| '_ \    | | | '_ \ / __|  
 | |____| |  | | | | | | \__ \ (_) | | | |  _| |_| | | | (__ _ 
  \_____|_|  |_|_| |_| |_|___/\___/|_| |_| |_____|_| |_|\___(_) 
                     We always watching you.
		    Авторы: Enigma & Commit 404 (nordbearbot)  
		    t.me/CrimsonCoalition
        Версия: V.2.0   

''','magenta'))
                                
