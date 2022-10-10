# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json
import pandas
from math import expm1
import sys
import csv
from uszipcode import SearchEngine
import pyap
from commonregex import CommonRegex
import os
import zipcodes
import re
import inspect
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
#f = open('/home/rob/Downloads/Telegram Desktop/August/ChatExport_2022-08-15 (1)/result.json')
f = open('C:/Users/tnsan/Desktop/parsers/Jsonfiles/result.json',encoding = 'utf-8')
data = json.load(f)
userslist=[]
for i in data['messages']:
    for j in (i["text"]):
        if(isinstance(j, str)):
            user={"Fname":"","Lname":"","Address":"","City":"","State":"","Zip":"","Country":"", "Phone":"", "Cvv":"", "Expm":"", "Expy":"","Email":"","Dob":"", "Ssn":"", "text":"", "Dl":""}
            j=j.split("\n")
            for line in j:
                if(("Fname" in line) or ("Name" in line)):
                   line=line.replace("Fname","")
                   line=line.replace("Name","")
                   line=line.replace(":","")
                   line=line.replace("\xa0","")
                   line=line.replace(" ","")
                   user["Fname"]=line

                
                if(("Lname" in line) or ("Name" in line)):
                    line=line.replace("Lname","")
                    line=line.replace("Name","")
                    line=line.replace(":","")
                    line=line.replace("\xa0","")
                    line=line.replace(" ","")
                    user["Lname"]=line
                    
              
                if("Address" in line):
                    line=line.replace("Address","")
                    line=line.replace(":","")
                    line=line.replace("\xa0","")
                    line=line.replace(" ","")
                    user["Address"]=line
                else:
                    line=line.replace("NA","")    
                    
               
                if("City" in line):
                    line=line.replace("City","")
                    line=line.replace(":","")
                    line=line.replace("\xa0","")
                    line=line.replace(" ","")
                    user["City"]=line
                    
                if("State" in line):
                    line=line.replace("State","")
                    line=line.replace(":","")
                    line=line.replace("\xa0","")
                    line=line.replace(" ","")
                    user["State"]=line
                   
                if("Zip" in line):
                    line=line.replace("Zip","")
                    line=line.replace(":","")
                    line=line.replace("\xa0","")
                    line=line.replace(" ","")
                    user["Zip"]=line

                if("Country" in line):
                    line=line.replace("Country","")
                    line=line.replace(":","")
                    line=line.replace("\xa0","")
                    line=line.replace(" ","")
                    user["Country"]=line

                if("Phone" in line):
                    line=line.replace("Phone","")
                    line=line.replace(":","")
                    line=line.replace("\xa0","")
                    line=line.replace(" ","")
                    user["Phone"]=line 

                if("Cvv" in line):
                    line=line.replace("Cvv","")
                    line=line.replace(":","")
                    line=line.replace("\xa0","")
                    line=line.replace(" ","")
                    user["Cvv"]=line    

                if("Expm" in line):
                    line=line.replace("Expm","")
                    line=line.replace(":","")
                    line=line.replace("\xa0","")
                    line=line.replace(" ","")
                    user["Expm"]=line    

                if("Expy" in line):
                    line=line.replace("Expy","")
                    line=line.replace(":","")
                    line=line.replace("\xa0","")
                    line=line.replace(" ","")
                    user["Expy"]=line  

                if("Email" in line):
                    line=line.replace("Email","")
                    line=line.replace(":","")
                    line=line.replace("\xa0","")
                    line=line.replace(" ","")
                    user['Email']=line  

                if("Dob" in line):
                    line=line.replace("Dob","")
                    line=line.replace(":","")
                    line=line.replace("\xa0","")
                    line=line.replace(" ","")
                    user["Dob"]=line  

                if("Ssn" in line):
                    line=line.replace("Ssn","")
                    line=line.replace(":","")
                    line=line.replace("\xa0","")
                    line=line.replace(" ","")
                    user["Ssn"]=line

                    if("text" in line):

                        line=line.replace("text","")
                        line=line.replace(":","")
                        line=line.replace("\xa0","")
                        line=line.replace(" ","")
                        user["text"]=line          

                if("Dl" in line):
                    line=line.replace("Dl","")
                    line=line.replace(":","")
                    line=line.replace("\xa0","")
                    line=line.replace(" ","")
                    user["Dl"]=line        



                    
            userslist.append(user)      
            
print(userslist)
keys = userslist[0].keys()
print("********************")
print(keys)
 
with open("Dragons_incorporated.csv", "w", encoding = 'utf-8', newline ='' ) as file:
    csvwriter = csv.DictWriter(file, keys)
    csvwriter.writeheader()
    csvwriter.writerows(userslist)
f.close()
