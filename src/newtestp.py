#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import Tkinter
from PIL import Image, ImageTk
from Tkinter import Tk, Label, BOTH, RAISED, RIGHT
from ttk import Frame, Style, Button
import Tkinter as tk
import os
from subprocess import call
import tkFont
import time
import sys
import subprocess
from datetime import date


rf = 'python rfxsend.py -r '
today = date.today()

class App(Frame):

       

    def __init__(self, db, width=1600, height=720, x=0, y=0):
        self.db = db
        self.root = tk.Tk()
        self.root.wm_attributes("-topmost", 1)
        geometry = '{}x{}+{}+{}'
        self.root.geometry(geometry.format(width, height, x, y))
        Frame.__init__(self, self.root)
        self.initUI()
        self.refresh()
    
        
    def initUI(self):

        
        self.root.title("Home Automation")
        self.pack(fill=BOTH, expand=1)
        self.customFont = tkFont.Font(family="Helvetica", size=14)
        self.customFont1 = tkFont.Font(family="Helvetica", size=12)
        Style().configure("TFrame", background="#FFFFFF")

        floorp = Image.open("Floorplan.jpg")
        floorplan = ImageTk.PhotoImage(floorp)
        label1 = Label(self, image=floorplan)
        label1.image = floorplan
        label1.place(x=0, y=0)

        self._switchon = tk.PhotoImage(file='switchon.gif')
        self._switchoff = tk.PhotoImage(file='switchoff.gif')
        self._lighton = tk.PhotoImage(file='lighton.gif')
        self._lightoff = tk.PhotoImage(file='lightoff.gif')
        self._Off = tk.PhotoImage(file='Off.gif')
        self._Stat = tk.PhotoImage(file='Stat.gif')
        self._18 = tk.PhotoImage(file='18.gif')
        self.result1 = ''
        self.result2 = ''
        self.result3 = ''
        self.result4 = ''
        self.result5 = ''
        self.result6 = ''
        self.result7 = ''
        self.result8 = ''
        self.result9 = ''
        self.result10 = ''
        self.result11 = ''
        self.result12 = ''
        self.result13 = ''
        self.result14 = ''
        self.result15 = ''
        self.result16 = ''
        self.result17 = ''
        self.result18 = ''
        self.result19 = ''
        self.result20 = ''
        self.result21 = ''
        self.result22 = ''
        self.result23 = ''
        self.result24 = ''
        self.result25 = ''
        self.result26 = ''
        self.result27 = ''
        self.result28 = ''
        self.result29 = ''
        self.result30 = ''
        self.result31 = ''
        self.result32 = ''  
        self.result33 = '' 
        self.result34 = ''
        self.result35 = ''
        self.result36 = ''
        self.result37 = ''
        self.result38 = ''
        self.result39 = ''
        self.result40 = ''
        self.result41 = ''


        self.label1 = ''
        self.label2 = ''
        self.label3 = ''
        self.label4 = ''
        self.label5 = ''
        self.label6 = ''
        self.label7 = ''
        self.label8 = ''
        self.label9 = ''
        self.label10 = ''
        self.label11 = ''
        self.label12 = ''
        self.label13 = ''
        self.label14 = ''
        self.label15 = ''
        self.label16 = ''
        self.label17 = ''
        self.label18 = ''  
        self.label19 = ''
        self.label20 = ''
        self.label21 = ''
        self.label22 = ''
        self.label23 = ''   
        self.label24 = ''
        self.label25 = ''

    def hwon(self):
        os.system(rf + '0A140000F4333308010070')

    def hwoff(self):
        os.system(rf + '0A140000F4333308000070')


    def gardon(self):
        os.system(rf + '0A140005F1234561010070')

    def gardoff(self):
        os.system(rf + '0A140005F1234561000070')


    def g2on(self):
        os.system(rf + '0A140000F1529702010080')


    def g2off(self):
        os.system(rf + '0A140000F1529702000080')

        
    def g1on(self):
        os.system(rf + '0A140000F1529701010080')

    def g1off(self):
        os.system(rf + '0A140000F1529701000080')
 

    def con1on(self):
        os.system(rf + '0A140000F291F401010070')
        time.sleep(2)
        os.system(rf + '0A140000F291F402010070')

    def con1off(self):    
        os.system(rf + '0A140000F291F401000070')
        time.sleep(2)
        os.system(rf + '0A140000F291F402000070')

    def con2on(self):
        os.system(rf + '0A140005F291F403010070')
    def con2off(self):
        os.system(rf + '0A140005F291F403000070')


    def boileron(self):
        os.system(rf + '0A140000F1322202010070')
    def boileroff(self):
        os.system(rf + '0A140000F1322202000070')

    def rcon(self):
        os.system(rf + '0A140003F291F40D010060')
    def rcoff(self):
        os.system(rf + '0A140003F291F40D000060')

    def dlon(self):
        os.system(rf + '0A140001F291F40E010060')
    def dloff(self):
        os.system(rf + '0A140001F291F40E000060')

    def bglon(self):
        os.system(rf + '0A140000F291F40F010060')
        os.system(rf + '0A140005F1234561010070')

    def bgloff(self):
        os.system(rf + '0A140001F291F40F000060')
        os.system(rf + '0A140005F1234561000070')

    def fcamon(self):
        os.system(rf + '0A140000F291F410010060')
    def fcamoff(self):
        os.system(rf + '0A140001F291F410000060')    

    def pslon(self):
        os.system(rf + '0A140000F291F409010070')
    def psloff(self):
        os.system(rf + '0A140000F291F409000070')

    def flon(self):
        os.system(rf + '0A14001BF291F40A010070')
    def floff(self):
        os.system(rf + '0A14001BF291F40A000070')

    def luon(self):
        os.system(rf + '0A140000F291F404010070')
    def luoff(self):
        os.system(rf + '0A140000F291F404000070')

    def l1on(self):
        os.system(rf + '0A140000F291F405010070')
    def l1off(self):
        os.system(rf + '0A140000F291F405000070')

    def l2on(self):
        os.system(rf + '0A140000F291F406010070')
    def l2off(self):
        os.system(rf + '0A140000F291F406000070')

    def hlon(self):
        os.system(rf + '0A140000F291F407010070')
    def hloff(self):
        os.system(rf + '0A140000F291F407000070')

    def fhon(self):
        os.system(rf + '0A140000F291F408010070')
    def fhoff(self):
        os.system(rf + '0A140000F291F408000070')

    def fpon(self):
        os.system(rf + '0A140000F291F40B010070')
    def fpoff(self):
        os.system(rf + '0A140000F291F40B000070')

    def garon(self):
        os.system(rf + '0A140000F291F40C010070')
    def garoff(self):
        os.system(rf + '0A140000F291F40C000070')

    def ltlon(self):
        os.system(rf + '0A140005F52B530D010070')
    def ltloff(self):
        os.system(rf + '0A140005F52B530D000070')

    def loungeron(self):
         os.system(rf + '0A14003DF552E801010080')
    def loungeroff(self):
         os.system(rf + '0A14003DF552E801000080')

    def wfon(self):
         os.system(rf + '0A14003DF1529604010080')
    def wfoff(self):
         os.system(rf + '0A14003DF1529604000080')


    def a5on(self):
         os.system(rf + '0A14003DF0987D03010080')
    def d5off(self):    
        os.system(rf + '0A14003DF0987D03000080')
    def ppoff(self):
        os.system('sudo python /home/pi/alarm/pooloff.py &')
    def ppon(self):
         os.system('sudo python /home/pi/alarm/poolon.py &')
 
     
    def d6off(self):
        os.system(rf + '0A14003FF0987D05000080')
    def d6on(self):
        os.system(rf + '0A14003DF0987D05010080')
    def d1off(self):
        os.system(rf + '0A14003FF0987D01000080')
 
    def rwofficeon(self):
        os.system(rf + '0A140005F1234701010070')
    def rwofficeoff(self):
        os.system(rf + '0A140005F1234701000070')


    def birdon(self):
        os.system(rf + '0A140000F291F205010070')
    def birdoff(self):
        os.system(rf + '0A140000F291F205000070')

    def pheon(self):
        os.system('sudo python /home/pi/alarm/poolelectricon.py &')
    def pheoff(self):
        os.system('sudo python /home/pi/alarm/poolelectricoff.py &')

    def phon(self):
        os.system('sudo python /home/pi/alarm/poolonsimple.py &')
        os.system(rf + '0A14003DF1528502010080')
    def phoff(self):
        os.system(rf + '0A14003DF1528502000080')
 
    def heaton(self):
        os.system(rf + '0A14003DF1528504010080')
    def heatoff(self):
        os.system(rf + '0A14003DF1528504000080')

    def poolsupplyon(self):
        os.system(rf + '0A14003DF552E802010080')
    def poolsupplyoff(self):
        os.system(rf + '0A14003DF552E802000080')

    def pcopen(self):
        os.system('sudo python /home/pi/pcopen.py &')  


    def pcclose(self):    
        os.system('sudo python /home/pi/pcclose.py &')


    def constat(self):
        os.system('sudo python /home/pi/alarm/constat.py')

    def conoff(self):
        os.system('sudo python /home/pi/alarm/conoff.py')

    def con18(self):
        os.system('sudo python /home/pi/alarm/con18.py')




    def refresh(self):

        #Stops program at 10am and 3pm to restart via mystart.sh in crontab
        
        now = time.strftime('%H%M')
        
        if now == '1500' or now == '1000':
            sys.exit(0)

        cursor = self.db.cursor() 

       #Garden Lights

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Garden Lights'")
        result, = cursor.fetchone()
        if result <> self.result38:
            self.result38 = result
            if result == 'On':
                button1 = tk.Button(image=self._lighton,command=self.gardoff)
                button1.place(x=196, y=104)
            else:
                button1 = tk.Button(image=self._lightoff,command=self.gardon)
                button1.place(x=196, y=104)



        #Conservatory ceiling Lights

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Con Light1'")
        result, = cursor.fetchone()
        if result <> self.result1:
            self.result1 = result
            if result == 'On':
                button1 = tk.Button(image=self._lighton,command=self.con1off)
                button1.place(x=240, y=290)
            else:
                button1 = tk.Button(image=self._lightoff,command=self.con1on)
                button1.place(x=240, y=290)

         #Conservatory side lights 

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Con Table Lights'")
        result, = cursor.fetchone()
        if result <> self.result2:
            self.result2 = result
            if result == 'On':
                button1 = tk.Button(image=self._lighton,command=self.con2off)
                button1.place(x=180, y=180)
            else:
                button1 = tk.Button(image=self._lightoff,command=self.con2on)
                button1.place(x=180, y=180)


        #Lounge Router  switch

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Lounge Router'")
        result, = cursor.fetchone()
        if result <> self.result23:
            self.result23 = result
            if result == 'On':
                button1 = tk.Button(image=self._switchon,command=self.loungeroff)
                button1.place(x=597, y=430)
            else:
                button1 = tk.Button(image=self._switchoff,command=self.loungeron)
                button1.place(x=597, y=430)


        #Boiler Main switch

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Boiler'")
        result, = cursor.fetchone()
        if result <> self.result11:
            self.result11 = result
            if result == 'On':
                button1 = tk.Button(image=self._switchon,command=self.boileroff)
                button1.place(x=640, y=190)
            else:
                button1 = tk.Button(image=self._switchoff,command=self.boileron)
                button1.place(x=640, y=190)



        #Pool Pump
        
        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Pool Pump'")
        result, = cursor.fetchone()
        if result <> self.result3:
            self.result3 = result
            if result == 'On':
                button1 = tk.Button(image=self._switchon,command=self.ppoff)
                button1.place(x=990, y=160)
            else:
                button1 = tk.Button(image=self._switchoff,command=self.ppon)
                button1.place(x=990, y=160)

        #House Heating

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Heating'")
        result, = cursor.fetchone()
        if result <> self.result20:
            self.result20 = result
            if result == 'On':
                button1 = tk.Button(image=self._switchon,command=self.heatoff)
                button1.place(x=600, y=190)
            else:
                button1 = tk.Button(image=self._switchoff,command=self.heaton)
                button1.place(x=600, y=190)

        #Hot water heat pump

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Hot Water'")
        result, = cursor.fetchone()
        if result <> self.result40:
            self.result40 = result
            if result == 'On':
                button1 = tk.Button(image=self._switchon,command=self.hwoff)
                button1.place(x=600, y=145)
            else:
                button1 = tk.Button(image=self._switchoff,command=self.hwon)
                button1.place(x=600, y=145)


        #Utility Router & wifi
        
        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Utility Router'")
        result, = cursor.fetchone()
        if result <> self.result15:
            self.result15 = result
            if result == 'On':
                button1 = tk.Button(image=self._switchon,command=self.rcoff)
                button1.place(x=730, y=210)
            else:
                button1 = tk.Button(image=self._switchoff,command=self.rcon)
                button1.place(x=730, y=210)

        

        #Pool Heating Gas
        
        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Pool Heating'")
        result, = cursor.fetchone()
        if result <> self.result14:
            self.result14 = result
            if result == 'On':
                button1 = tk.Button(image=self._switchon,command=self.phoff)
                button1.place(x=990, y=210)
            else:
                button1 = tk.Button(image=self._switchoff,command=self.phon)
                button1.place(x=990, y=210)

        #Pool Heating Electric

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Pool Electric Heating'")
        result, = cursor.fetchone()
        if result <> self.result39:
            self.result39 = result
            if result == 'On':
                button1 = tk.Button(image=self._switchon,command=self.pheoff)
                button1.place(x=1080, y=210)
            else:
                button1 = tk.Button(image=self._switchoff,command=self.pheon)
                button1.place(x=1080, y=210)



        #Pool Cover Temp
        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Pool Cover Temp'")
        result, = cursor.fetchone()

        if result <> self.label18:
            self.label18 = result
            labelland = Label(self, background = "white",font=self.customFont, text= 'Enclosure temp ' + result + "    ")
            labelland.place(x=1030, y=280)

        #Pool Cover auto or manual

        cursor.execute("SELECT ID FROM petstatus WHERE Name = 'Pool Cover'")
        result, = cursor.fetchone()
        
        if result <> self.label19:
            self.label19 = result
            labelland = Label(self, background = "white",font=self.customFont, text= result)
            labelland.place(x=1200, y=250)

        #Pool Start times
        if self.label21 == '':
            cursor.execute("SELECT code FROM petstatus WHERE Name = 'Pool Temp'")
            result, = cursor.fetchone()
            self.label21 = result
            cursor.execute("SELECT Time FROM petstatus WHERE Name = 'Pool Temp'")
            result1, = cursor.fetchone()

            labelland = Label(self, background = "white",font=self.customFont, text= 'Start time yesterday: ' + result + "  today:  " + result1)
            labelland.place(x=905, y=302)


        # Pool Cover
        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Pool Cover'")
        result, = cursor.fetchone()
        if result <> self.result21:
            self.result21 = result
           
            labelland = Label(self, background = "white",font=self.customFont, text= 'Pool Cover ' + result + "  ")
            labelland.place(x=1030, y=250)

            if result == 'Open':
                button1 = tk.Button(image=self._switchon,command=self.pcclose)
                button1.place(x=990, y=250)

            else:
                button1 = tk.Button(image=self._switchoff,command=self.pcopen)
                button1.place(x=990, y=250)

        # Pool Supply
        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Pool Supplies'")
        result, = cursor.fetchone()
        if result <> self.result24:
            self.result24 = result

            

            if result == 'On':
                button1 = tk.Button(image=self._switchon,command=self.poolsupplyoff)
                button1.place(x=990, y=330)

            else:
                button1 = tk.Button(image=self._switchoff,command=self.poolsupplyon)
                button1.place(x=990, y=330)




        #Garage Router & Rpi Camera
        
        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Garage Switch'")
        result, = cursor.fetchone()
        if result <> self.result16:
            self.result16 = result
            if result == 'On':
                button1 = tk.Button(image=self._switchon,command=self.garoff)
                button1.place(x=50, y=470)
            else:
                button1 = tk.Button(image=self._switchoff,command=self.garon)
                button1.place(x=50, y=470)

        
        #Front Camera
        
        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Front Camera'")
        result, = cursor.fetchone()
        if result <> self.result4:
            self.result4 = result
            if result == 'On':
                button1 = tk.Button(image=self._switchon,command=self.fcamoff)
                button1.place(x=50, y=370)
            else:
                button1 = tk.Button(image=self._switchoff,command=self.fcamon)
                button1.place(x=50, y=370)

    

        #Front Exterior Lights
        
        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Front Exterior Lights'")
        result, = cursor.fetchone()
        if result <> self.result5:
            self.result5 = result
            if result == 'On':
                button1 = tk.Button(image=self._lighton,command=self.floff)
                button1.place(x=600, y=480)
            else:
                button1 = tk.Button(image=self._lightoff,command=self.flon)
                button1.place(x=600, y=480)
       
        #Drive Light
        
        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Drive Light'")
        result, = cursor.fetchone()
        if result <> self.result6:
            self.result6 = result
            if result == 'On':
                button1 = tk.Button(image=self._lighton,command=self.dloff)
                button1.place(x=50, y=410)
            else:
                button1 = tk.Button(image=self._lightoff,command=self.dlon)
                button1.place(x=50, y=410)


        #Back Garden Lights
        
        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Back Garden Lights'")
        result, = cursor.fetchone()
        if result <> self.result8:
            self.result8 = result
            if result == 'On':
                button1 = tk.Button(image=self._lighton,command=self.bgloff)
                button1.place(x=620, y=60)
            else:
                button1 = tk.Button(image=self._lightoff,command=self.bglon)
                button1.place(x=620, y=60)

        #Lounge Table Lamps

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Lounge Table Lamps'")
        result, = cursor.fetchone()
        if result <> self.result22:
            self.result22 = result
            if result == 'On':
                button1 = tk.Button(image=self._lighton,command=self.ltloff)
                button1.place(x=602, y=280)
            else:
                button1 = tk.Button(image=self._lightoff,command=self.ltlon)
                button1.place(x=602, y=280)

        

        #Pool Side Light
        
        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Pool Side Light'")
        result, = cursor.fetchone()
        if result <> self.result9:
            self.result9 = result
            if result == 'On':
                button1 = tk.Button(image=self._lighton,command=self.psloff)
                button1.place(x=890, y=250)
            else:
                button1 = tk.Button(image=self._lightoff,command=self.pslon)
                button1.place(x=890, y=250)

       

        #Lounge Uplighters
        
        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Lounge Uplighters'")
        result, = cursor.fetchone()
        if result <> self.result12:
            self.result12 = result
            if result == 'On':
                button1 = tk.Button(image=self._lighton,command=self.luoff)
                button1.place(x=602, y=385)
            else:
                button1 = tk.Button(image=self._lightoff,command=self.luon)
                button1.place(x=602, y=385)

        #Corner Camera supply
        
        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Corner Camera Supply'")
        result, = cursor.fetchone()
        if result <> self.result13:
            self.result13 = result
            if result == 'On':
                button1 = tk.Button(image=self._switchon,command=self.l1off)
                button1.place(x=295, y=360)
            else:
                button1 = tk.Button(image=self._switchoff,command=self.l1on)
                button1.place(x=295, y=360)

        #Garage 1 charger

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Garage 1'")
        result, = cursor.fetchone()
        if result <> self.result36:
            self.result36 = result
            if result == 'On':
                button1 = tk.Button(image=self._switchon,command=self.g1off)
                button1.place(x=50, y=525)
            else:
                button1 = tk.Button(image=self._switchoff,command=self.g1on)
                button1.place(x=50, y=525)

        #Garage 2 charger

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Garage 2'")
        result, = cursor.fetchone()
        if result <> self.result37:
            self.result37 = result
            if result == 'On':
                button1 = tk.Button(image=self._switchon,command=self.g2off)
                button1.place(x=280, y=525)
            else:
                button1 = tk.Button(image=self._switchoff,command=self.g2on)
                button1.place(x=280, y=525)

        #RW office switch

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'RW Switch'")
        result, = cursor.fetchone()
        if result <> self.result41:
            self.result41 = result
            if result == 'On':
                button1 = tk.Button(image=self._switchon,command=self.rwofficeoff)
                button1.place(x=636, y=430)
            else:
                button1 = tk.Button(image=self._switchoff,command=self.rwofficeon)
                button1.place(x=636, y=430)


        #Supply to Bird Cam

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Bird Cam'")
        result, = cursor.fetchone()
        if result <> self.result32:
            self.result32 = result
            if result == 'On':
                button1 = tk.Button(image=self._switchon,command=self.birdoff)
                button1.place(x=640, y=475)
            else:
                button1 = tk.Button(image=self._switchoff,command=self.birdon)
                button1.place(x=640, y=475)

        #Water Feature

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Water Feature'")
        result, = cursor.fetchone()
        if result <> self.result34:
            self.result34 = result
            if result == 'On':
                button1 = tk.Button(image=self._switchon,command=self.wfoff)
                button1.place(x=328, y=100)
            else:
                button1 = tk.Button(image=self._switchoff,command=self.wfon)
                button1.place(x=328, y=100)



        #Supply to back cameras & pond Rpi

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Back Camera Supply'")
        result, = cursor.fetchone()
        if result <> self.result7:
            self.result7 = result
            if result == 'On':
                button1 = tk.Button(image=self._switchon,command=self.l2off)
                button1.place(x=480, y=100)
            else:
                button1 = tk.Button(image=self._switchoff,command=self.l2on)
                button1.place(x=480, y=100)

        #Hall Lights

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Hall Lights'")
        result, = cursor.fetchone()
        if result <> self.result17:
            self.result17 = result
            if result == 'On':
                button1 = tk.Button(image=self._lighton,command=self.hloff)
                button1.place(x=600, y=247)
            else:
                button1 = tk.Button(image=self._lightoff,command=self.hlon)
                button1.place(x=600, y=247)

        #Front Hall Light

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Front Hall Light'")
        result, = cursor.fetchone()
        if result <> self.result18:
            self.result18 = result
            if result == 'On':
                button1 = tk.Button(image=self._lighton,command=self.fhoff)
                button1.place(x=450, y=320)
            else:
                button1 = tk.Button(image=self._lightoff,command=self.fhon)
                button1.place(x=450, y=320)

         #Front Porch Light

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Front Porch Light'")
        result, = cursor.fetchone()
        if result <> self.result19:
            self.result19 = result
            if result == 'On':
                button1 = tk.Button(image=self._lighton,command=self.fpoff)
                button1.place(x=460, y=440)
            else:
                button1 = tk.Button(image=self._lightoff,command=self.fpon)
                button1.place(x=460, y=440)

        #Conservatory Heating

        cursor.execute("SELECT Code FROM petstatus WHERE Name = 'Con Heat'")
        result, = cursor.fetchone()
        if result <> self.result31:
            self.result31 = result
            if result == 'Off':
                button1 = tk.Button(image=self._Off,command=self.constat)
                button1.place(x=280, y=250)

            if result == 'Stat':
                button1 = tk.Button(image=self._Stat,command=self.con18)
                button1.place(x=280, y=250)

            if result == '18':
                button1 = tk.Button(image=self._18,command=self.conoff)
                button1.place(x=280, y=250)

        
        #Total Power

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Power Usage'")
        result, = cursor.fetchone()
        if result <> self.label1:
            self.label1 = result
            labelland = Label(self, background = "white",font=self.customFont, text="Power use " + result + " watts  ")
            labelland.place(x=900, y=375)
            hour = int(time.strftime("%H"))
            cursor.execute("SELECT state FROM petstatus WHERE Name = 'Pool Electric Heating'")
            pelect, = cursor.fetchone()

            if pelect == 'On':

                if int(result) > 10000 and hour >6 and hour<23:
             
                    command = "sudo python /home/pi/alarm/5000warn1.py"
                    subprocess.Popen(command, shell=True)

            if pelect == 'Off':

                if int(result) > 5500 and hour >6 and hour<23:
 
                    command = "sudo python /home/pi/alarm/5000warn1.py"
                    subprocess.Popen(command, shell=True)
            


        #Solar 

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Solar'")
        result, = cursor.fetchone()
        if result <> self.label24:
            self.label24 = result
            cursor.execute("SELECT code FROM petstatus WHERE Name = 'Solar'")
            kwh, = cursor.fetchone()
           
            labelland = Label(self, background = "white",font=self.customFont, text="Solar " + result + " watts  " + " High today   " + kwh + "   ")
            labelland.place(x=900, y=400)                            


        #Battery

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Battery'")
        result, = cursor.fetchone()
        if result <> self.label2:
            self.label2 = result
            labelland = Label(self, background = "white",font=self.customFont, text="Battery " + result + "% ")
            labelland.place(x=900, y=425)
            cursor.execute("UPDATE petstatus Set Code = %s WHERE Name = %s",('','Battery'))
            hour = int(time.strftime("%H"))

            if result == '10': # or result == '5':

                cursor.execute("SELECT ID FROM petstatus WHERE Name = 'Battery'")
                old, = cursor.fetchone()
                cursor.execute("SELECT Code FROM petstatus WHERE Name = 'Battery'")
                flag, = cursor.fetchone()
                if result < old and flag != result:
                    if hour >6 and hour < 22:   
                        command = "aplay /home/pi/alarm/"+ result+ "percent.wav"    
                        subprocess.Popen(command, shell=True)               
                        cursor.execute("UPDATE petstatus Set Code = %s WHERE Name = %s",(result,'Battery'))

            if result == '90':
                cursor.execute("SELECT ID FROM petstatus WHERE Name = 'Battery'")
                old, = cursor.fetchone()
                cursor.execute("SELECT Code FROM petstatus WHERE Name = 'Battery'")
                flag, = cursor.fetchone()
                if result > old and flag != result:
                    if hour >6 and hour < 23:
                        command = "aplay /home/pi/alarm/90percent.wav"
                        subprocess.Popen(command, shell=True)
                        cursor.execute("UPDATE petstatus Set Code = %s WHERE Name = %s",(result,'Battery'))


        #Battery High

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Battery High'")
        result, = cursor.fetchone()
        if result <> self.label5:
            self.label5 = result
            cursor.execute("SELECT code FROM petstatus WHERE Name = 'Battery High'")
            time1, = cursor.fetchone()

            labelland = Label(self, background = "white",font=self.customFont, text= "High "+ result + '% at ' + time1[0:5])
            labelland.place(x=900, y=450)

        #Battery Low

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Battery Low'")
        result, = cursor.fetchone()
        if result <> self.label25:
            self.label25 = result
            cursor.execute("SELECT code FROM petstatus WHERE Name = 'Battery Low'")
            time1, = cursor.fetchone()

            labelland = Label(self, background = "white",font=self.customFont, text= "Low "+ result + '% at ' + time1[0:5])
            labelland.place(x=1060, y=450)

        

        #Dark/Light

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Dark'")
        result, = cursor.fetchone()
        if result <> self.label4:
            self.label4 = result
            labelland = Label(self, background = "white",font=self.customFont, text=result + "  ")
            labelland.place(x=900, y=475)



        #Front Door status

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Front Door'")
        result, = cursor.fetchone()
        if result <> self.label7:
            self.label7 = result
            labelland = Label(self, background = "white",font=self.customFont, text= "Front Door "+ result + '  ')
            labelland.place(x=346, y=380)

        
       
        #RW Office Temp

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'RW_Office'")
        result, = cursor.fetchone()
        cursor.execute("SELECT ID FROM petstatus WHERE Name = 'RW_Office'")
        bc, = cursor.fetchone()
        if bc == "On":
            bc = "red"   
        else:
            bc = "white"

        if result <> self.label6 or bc <> self.result25:
            self.label6 = result
            self.result25 = bc
            labelland = Label(self, background = bc,font=self.customFont, text= result + 'c    ')
            labelland.place(x=665, y=427)


        #Conservatory Temp

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Con Heat'")
        result, = cursor.fetchone()
        cursor.execute("SELECT ID FROM petstatus WHERE Name = 'Con Heat'")
        bc, = cursor.fetchone()
        if bc == "On":
            bc = "red"
        else:
            bc = "white"


        if result <> self.label20 or bc <>self.result30:
            self.label20 = result
            self.result30 = bc
            labelland = Label(self, background = bc,font=self.customFont, text= result + 'c  ')
            labelland.place(x=215, y=250)
        
       
        #Kitchen Temp

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Kitchen'")
        result, = cursor.fetchone()
        cursor.execute("SELECT ID FROM petstatus WHERE Name = 'Kitchen'")
        bc, = cursor.fetchone()
        if bc == "On":
            bc = "red"
        else:
            bc = "white"


        if result <> self.label15 or bc <>self.result26:
            self.label15 = result
            self.result26 = bc 
            labelland = Label(self, background = bc,font=self.customFont, text= result + 'c  ')
            labelland.place(x=380, y=195)

        
        #Lounge Temp

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Lounge'")
        result, = cursor.fetchone()

        cursor.execute("SELECT ID FROM petstatus WHERE Name = 'Lounge'")
        bc, = cursor.fetchone()
        if bc == "On":
            bc = "red"
        else:
            bc = "white"

        if result <> self.label16 or bc <> self.result27:
            self.label16 = result
            self.result27 = bc
            labelland = Label(self, background = bc,font=self.customFont, text= result + 'c   ')
            labelland.place(x=550, y=350)
        
        #EW Office Temp

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'EW_Office'")
        result, = cursor.fetchone()
        cursor.execute("SELECT ID FROM petstatus WHERE Name = 'EW_Office'")
        bc, = cursor.fetchone()
        if bc == "On":
            bc = "red"
        else:
            bc = "white"


        if result <> self.label17 or bc <> self.result28:
            self.label17 = result
            self.result28 = bc
            labelland = Label(self, background = bc,font=self.customFont, text= result + 'c  ')
            labelland.place(x=350, y=310)
        
        #Hall Temp

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Hall'")
        result, = cursor.fetchone()
        cursor.execute("SELECT ID FROM petstatus WHERE Name = 'Hall'")
        bc, = cursor.fetchone()
        if bc == "On":
            bc = "red"
        else:
            bc = "white"


        if result <> self.label23 or bc <> self.result35:
            self.label23 = result
            self.result35 = bc
            labelland = Label(self, background = bc,font=self.customFont, text= result + 'c  ')
            labelland.place(x=430, y=250)

 




       #Bathroom Temp

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Bathroom'")
        result, = cursor.fetchone()
        cursor.execute("SELECT ID FROM petstatus WHERE Name = 'Bathroom'")
        bc, = cursor.fetchone()
        if bc == "On":
            bc = "red"
        else:
            bc = "white"


        if result <> self.label22 or bc <> self.result33:
            self.label22 = result
            self.result33 = bc
            labelland = Label(self, background = bc,font=self.customFont, text= result + 'c  ')
            labelland.place(x=635, y=308)
 
      
        #Back Door Status

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Back Door'")
        result, = cursor.fetchone()
        if result <> self.label8:
            self.label8 = result
            labelland = Label(self, background = "white",font=self.customFont, text= "Back Door "+ result + '  ')
            labelland.place(x=450, y=60)
        
        
        #Alarm State

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Email'")
        result, = cursor.fetchone()
        if result <> self.label9:
            self.label9 = result
            labelland = Label(self, background = "white",font=self.customFont, text= "Email "+ result + '    ')
            labelland.place(x=900, y=500)
       
  
        #Computer Alarm

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Alarm state'")
        result, = cursor.fetchone()
        if result <> self.label10:
            self.label10 = result
            labelland = Label(self, background = "white",font=self.customFont, text= "Computer Alarm "+ result + '      ')
            labelland.place(x=900, y=525)
               
       

        #Utility Temp

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Utility_Room'")
        result, = cursor.fetchone()
        cursor.execute("SELECT ID FROM petstatus WHERE Name = 'Utility_Room'")
        bc, = cursor.fetchone()
        if bc == "On":
            bc = "red"
        else:
            bc = "white"


        if result <> self.label11 or bc <> self.result29:
            self.label11 = result
            self.result29 = bc
            labelland = Label(self, background = bc,font=self.customFont, text= result + 'c  ')
            labelland.place(x=770, y=190)

        

        #Exterior Temp
        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Exterior Temp'")
        result, = cursor.fetchone()
        if result <> self.label12:
            self.label12 = result
            labelland = Label(self, background = "white",font=self.customFont, text= "Exterior Temp "+ result + 'c    ')
            labelland.place(x=900, y=550)
        
        #Hot Water HP

        cursor.execute("SELECT ID FROM petstatus WHERE Name = 'Hot Water HP'")
        result, = cursor.fetchone()
        if result <> self.label13:
            self.label13 = result
            labelland = Label(self, background = "white",font=self.customFont, text= result + 'w   ')
            labelland.place(x=600, y=110)
        """
        #Forecast

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Forecast'")
        result, = cursor.fetchone()
        if result <> self.label14:
            self.label14 = result
            labelland = Label(self, background = "white",font=self.customFont, text= "Forecast: "+ result + '      ')
            #labelland.place(x=250, y=470)
        """
        #Pool Temp

        cursor.execute("SELECT state FROM petstatus WHERE Name = 'Pool Temp'")
        result, = cursor.fetchone()
        if result <> self.label3:
            self.label3 = result
            labelland = Label(self, background = "light blue",font=self.customFont, text= result + " c        ")
            labelland.place(x=1000, y=185)  
  
        



        self.root.after(50, self.refresh)

if __name__ == '__main__':


    db = MySQLdb.connect(host='192.168.0.220', user='roger', db='pet')
    db.autocommit(True)
    app = App(db)
    app.mainloop()
    

    
