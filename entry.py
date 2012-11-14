import kookoo
from string import index
import random
from dataBase import *
import datetime


def welcome():
    r = kookoo.Response()
    r.addPlayText("welcome to expense management system.") # change to app name
    g = r.append(kookoo.CollectDtmf(maxDigits=1))
    g.append(kookoo.PlayText("Press 1 for adding an expense entry"))
    g.append(kookoo.PlayText("Press 2 for analysis"))
    g.append(kookoo.PlayText("Press 3 for transaction"))
    return r

def addEntry():
    r = kookoo.Response()
    r.addPlayText("What category did you spend on")
    g = r.append(kookoo.CollectDtmf(maxDigits=1))
    g.append(kookoo.PlayText("Press 1 for food"))
    g.append(kookoo.PlayText("Press 2 for transport"))
    g.append(kookoo.PlayText("Press 3 for shopping"))
    g.append(kookoo.PlayText("Press 4 for entertainment"))
    g.append(kookoo.PlayText("Press 5 for heathcare"))
    g.append(kookoo.PlayText("Press 6 for education"))
    g.append(kookoo.PlayText("Press 7 for others"))
    
    return r
    
def enterAmount():
    r = kookoo.Response()
    g = r.append(kookoo.CollectDtmf())
    g.append(kookoo.PlayText("How much did you spend"))
    return r


def getCategoryFromNumber(x):
    if x == 1:return 'food'
    if x == 2:return 'transport'
    if x == 3:return 'shopping'
    if x == 4:return 'entertainment'
    if x == 5:return 'heathcare'
    if x == 6:return 'education'
    else : return 'others'
    
       
    
    
    
def updateDB(cid, category, amount):
    category = getCategoryFromNumber(int(category))
    record = userDB(cid = cid,amount = amount, category = category)
    record.put()
    r = kookoo.Response()
    r.addPlayText("Your entry was successfully added")
    return r


