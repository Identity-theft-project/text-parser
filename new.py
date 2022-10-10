import json
#from tqdm import tqdm
f = open('C:/Users/tnsan/Desktop/parsers/json-files_new/json-files/result(1).json', encoding = 'utf-8')
data = json.load(f)
userslist=[]
for i in data['messages']:
    #print("message : ",i)
    user={"id":i["id"],"Fname":"","Lname":"","Address":"","City":"","State":"","Zip":"","card_number":"","Country":"","BANK":"","BIN":"","TIME":"", "Phone":"", "Cvv":"", "Expm":"", "Expy":"","Email":"","Dob":"", "Ssn":"", "text":"", "type":"", "Dl":""}
    for k in i["text"]:
        #print(type(k))
        #print(k)
        if(isinstance(k, str)):
            if "|" in str(k):
                #print(k)
                s=k.split("|")
                user["Expm"]=s[1]
                user["Expy"]=s[2]
                user["Cvv"]=s[3]
            elif "\n" in str(k):
                s=k.split("\n")
                for l in s:
                    ll = l.split("-»")
                    if ll[0].strip() =="Bin":
                        user["BIN"]=ll[1]
                    elif ll[0].strip()=="Bank":
                        user["BANK"]=ll[1]
                    elif ll[0].strip()=="Country":
                        user["Country"]=ll[1]
                    
        if isinstance(k,dict):
            if k.get("type") =="bank_card":
                #print(k.get("text"))
                user["card_number"] = k.get("text")
            elif k.get("type")=="code":
                #print(k.get("text"))
                s=k.get("text").split("|")
                user["card_number"]=s[0]
                user["Expm"]=s[1]
                user["Expy"]=s[2]
                user["Cvv"]=s[3]
            '''elif if " " in str(k):
                s=k.split("  ")
                for l in s:
                    l1 = l.split(" ")
                    user["BANK"]=l1[1]
                    user["Country"]=l1[5]'''
    
    #for j in i["text_enities"]:

    userslist.append(user)
        #print(user)

from tabulate import tabulate
import pandas as pd
df = pd.DataFrame(userslist)
df.to_csv("resultoldjson.csv")
print(tabulate(df,headers="keys",tablefmt="psql"))
                    
