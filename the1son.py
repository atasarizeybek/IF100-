# -*- coding: utf-8 -*-
"""THE1SON

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w73E2RAXu_436y7f5Oi4Inz7KCw1oY8d
"""

userHour = int(input("Please enter the maintenance starting hour: "))
sHour = userHour

userMin = int(input("Please enter the maintenance starting minute: "))
sMin = userMin

userSec = int(input("Please enter the maintenance starting second: "))
sSec = userSec

#robotTimer = float(input("Please enter the maintenance duration in second(s) according to Perseverance's timer: "))

TotalMarsSec=24*60*60+37*60
TotalEarthSec=24*60*60
MarstoEarthConvRatio=TotalMarsSec/TotalEarthSec
EarthTimeInSec = robotTimer * MarstoEarthConvRatio   

seconds=EarthTimeInSec%60
EarthTimeInMinutes=(EarthTimeInSec-seconds)/60
minutes=EarthTimeInMinutes%60
hours=(EarthTimeInMinutes-minutes)/60


marshour=userHour+hours
marsminutes=userMin+minutes
marsseconds=userSec+seconds

actualsecs=marsseconds%60
actualminutes=(marsseconds-actualsecs)/60
actualminutes+=marsminutes

m=actualminutes%60

h=actualminutes%60
actualhours=(actualminutes-h)/60
actualhours+=marshour

actualhours=actualhours%24



print(int(actualhours), ":", int(m), ":", "%.2f" % (actualsecs), sep = "")