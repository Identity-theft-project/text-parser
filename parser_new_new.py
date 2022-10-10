# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json
import csv
from uszipcode import SearchEngine
import pyap
from commonregex import CommonRegex
import os
import zipcodes
import re
import json
import inspect
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
f = open('C:/Users/tnsan/Desktop/parsers/json-files_new/json-files/result.json', encoding = 'utf-8')
data = json.load(f)
userslist=[]
for i in data['messages']:
    for j in (i["text"]):
        if(isinstance(j, str)):
            user={"Fname":"","Lname":"","Address":"","City":"","State":"","Zip":"","card_number":"","Country":"","BANK":"","BIN":"","TIME":"", "Phone":"", "Cvv":"", "Expm":"", "Expy":"","Email":"","Dob":"", "Ssn":"", "text":"", "type":"", "Dl":"","COUNTRY":""}
            for item in re.finditer(r'(?!\A)\b\d{5}(?:-\d{4})?\b', j):
                if zipcodes.is_real(item.group()):
                    user["Zip"]=item.group()
                       
            j=j.replace(":","")
            j=j.replace("\xa0","")
            j=j.replace("|"," ")
            j=j.replace(" ","")
            adresses=CommonRegex(j)
            print("***************")
            print(adresses)
            j=j.split("\n")
            for line in j:
                if("Fname" in line):
                   line=line.replace("Fname","")
                   line=line.replace(":","")
                   line=line.replace("\xa0","")
                   line=line.replace(" ","")
                   user["Fname"]=line
                
                if("Lname" in line):
                    line=line.replace("Lname","")
                    line=line.replace(":","")
                    line=line.replace("\xa0","")
                    line=line.replace(" ","")
                    user["Lname"]=line
                    
               
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

                if("Country" in line):
                    line=line.replace("Country","")
                    line=line.replace(":","")
                    line=line.replace("\xa0","")
                    line=line.replace(" ","")
                    user["Country"]=line   
                else:
                    if ("COUNTRY" in line):
                        line=line.replace("COUNTRY","")
                        line=line.replace(":","")
                        line=line.replace("\xa0","")
                        line=line.replace(" ","")
                        line=line.replace("|","")
                        user["COUNTRY"]=line     

                    

                if("BANK" in line):
                    line=line.replace("BANK","")
                    line=line.replace(":","")
                    line=line.replace("|"," ")
                    line=line.replace("\xa0","")
                    line=line.replace(" ","")
                    user["BANK"]=line 

                if("BIN" in line):
                    line=line.replace("BIN","")
                    line=line.replace(":","")
                    line=line.replace("|"," ")
                    line=line.replace(" ","")
                    user["BIN"]=line 

                if("TIME" in line):
                    line=line.replace("BIN","")
                    line=line.replace(":","")
                    line=line.replace("|"," ")
                    line=line.replace("\xa0","")
                    line=line.replace(" ","")
                    user["TIME"]=line            


                if("Phone" in line):
                    line=line.replace("Phone","")
                    line=line.replace(":","")
                    line=line.replace("\xa0","")
                    line=line.replace(" ","")
                    user["Phone"]=line 

                if("type" in line):
                    line=line.replace("type","")
                    line=line.replace(":","")
                    line=line.replace("\xa0","")
                    line=line.replace(" ","")
                    user["type"]=line 


                #if("Cvv" in line):
    

                #if("Expm" in line): 

                #if("Expy" in line):
      

                            

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
                    line=line.replace("/","")
                    user["Dob"]=line  
                            
                if("Ssn" in line):
                    line=line.replace("Ssn","")
                    line=line.replace(":","")
                    line=line.replace("\xa0","")
                    line=line.replace(" ","")
                    user["Ssn"]=line
                

                if("Dl" in line):
                    line=line.replace("Dl","")
                    line=line.replace(":","")
                    line=line.replace("\xa0","")
                    line=line.replace(" ","")
                    user["Dl"]=line   
            
                    
            userslist.append(user)
            
                    
            

keys = userslist[0].keys()

with open("users2new.csv", "w", encoding = 'utf-8', newline ='') as file:
 csvwriter = csv.DictWriter(file, keys)
 csvwriter.writeheader()
 csvwriter.writerows(userslist)
# Closing file
f.close()
