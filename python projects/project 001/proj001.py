#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 2018

@author: linbarrybear

#############
#computer project 01 
#Algorithm
# Input a number
# translate it to float
# convet its unit by math 
# print them
##########
num_1=input("Input rods: ")   #input a number as your distance
n=float(num_1)#translate the input str into a float str
you_input=n
print("You input",you_input,"rods.\n")#print your input
print("Conversions")#conserve the unit to meter, feet, miles, furlongs and minutes to walk 
meter=n*5.0292 #convert rod to meter
furlongs=n/40  #convert rod to furlong
miles=(n*5.0292)/1609.34  #convert rod to miles
feet=(n*5.0292)/0.3048    #convert rod to feet
minutes_to_walk =(((n*5.0292)/1609.34)/(3.1/60))  #calculate the minutes to walk
print("Meters:",round(meter,3))  #convert it to a round 3 digit number
print("Feet:",round(feet,3))     #convert it to a round 3 digit number
print("Miles:",round(miles,3))   #convert it to a round 3 digit number
print("Furlongs:",round(furlongs,3))#convert it to a round 3 digit number
print("Minutes to walk",n,"rods:",round(minutes_to_walk,3))
