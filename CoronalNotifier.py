# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 13:30:16 2020

@author: lefin
"""


import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import time
import os
from win10toast import ToastNotifier
toaster = ToastNotifier()

clear = lambda: os.system('cls') #on Windows System

def listToString(s):  
    
    # initialize an empty string 
    str1 = "" 
    
    # return string   
    return (str1.join(s)) 

def split(word): 
    return [char for char in word]  

url = "https://www.worldometers.info/coronavirus/"
result = requests.get(url)
#print(result)
print('Welcome to Coronal Notifier')
if str(result.status_code)[0] == '2':
    print('connection has successfully established...')
else:
    print('connection issues, please check your internet.')

print("\n press Ctrl+C to terminate the program")

src = result.content

time.sleep(2)
clear()
soup = BeautifulSoup(src, 'lxml')
divs = soup.find_all('div', {"class": "maincounter-number"})
header = ['Cases', 'Lives Taken', 'Recovered']
stats = []
n = []
for i in divs:
    i = i.find('span')
    for x in i:
        n.append(x)
stats.append(n)
   
#for div in divs:
    #if div['id'] == 'maincounter-wrap':
        #print(div)
    #if h1 == 'Coronavirus Cases:':
        #break
    #    stats[0] = span.text
    #if h1 == 'Deaths:':
    #    stats[1] = span.text
    #if h1 == 'Recovered:':
    #    stats[2] = span.text
print('Data Retrieved From:')
print('worldometers. (n.d.). COVID-19 CORONAVIRUS PANDEMIC. Retrieved from https://www.worldometers.info/coronavirus/')
print('')
print(tabulate(stats, headers=header), end='\r')   
prevTot = ''
prevRec = ''
while 1:
    result = requests.get(url)
    src = result.content
    time.sleep(2)
    soup = BeautifulSoup(src, 'lxml')
    divs = soup.find_all('div', {"class": "maincounter-number"})
    header = ['Cases', 'Lives Taken', 'Recovered']
    stats = []
    n = []
    for i in divs:
        i = i.find('span')
        for x in i:
            n.append(x)
    stats.append(n)
    Tot = split(stats[0][0])
    Rec = split(stats[0][2])
    
    for char in Tot:
        if char.isdigit() == False:
            Tot.remove(char)
    for char in Rec:
        if char.isdigit() == False:
            Rec.remove(char)
    Tot = listToString(Tot)
    Rec = listToString(Rec)
    if prevTot != '' and prevRec != '':
        if Tot != prevTot:
            difference = int(Tot) - int(prevTot)
            text = "The number of cases has changed by: " + str(difference) +'\n stay strong, stay healthy, stay sanitized, stay at home'
            toaster.show_toast("Coronal Notification", text)
        if Rec != prevRec:
            difference = int(Rec) - int(prevRec)
            text2 = "Great News! " + str(difference) +' people recovered! \n stay strong, stay healthy, stay sanitized, stay at home'
            toaster.show_toast("Coronal Notification", text2)
    an = tabulate(stats, headers=header).split('\n')
    
    print(an[-1], end='\r')  
    prevTot = Tot
    prevRec = Rec
    #for div in divs:
        #if div['id'] == 'maincounter-wrap':
            #print(div)
        #if h1 == 'Coronavirus Cases:':
            #break
        #    stats[0] = span.text
        #if h1 == 'Deaths:':
        #    stats[1] = span.text
        #if h1 == 'Recovered:':
        #    stats[2] = span.text
   
