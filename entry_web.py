from dataBase import *
import datetime


def updateDB_web(cid, category, amount):
    record = userDB(cid = cid,amount = amount, category = category)
    record.put()
    
def makeDailyPie(cid):
    sum = {}
    
    records = db.GqlQuery('SELECT * FROM userDB WHERE cid = \'' + cid + '\' AND date = DATE(\'' + str(datetime.datetime.now().date()) + '\')')
    for x in records:
        if str(x.category) not in sum.keys(): sum[str(x.category)]=0
        sum[str(x.category)] = sum[str(x.category)] + int(x.amount)
        
    list = ['food' ,'transport','shopping','entertainment','healthcare','education','others']
    for x in list:
        if x  not in sum.keys():
            sum[x] = 0
    
    return sum

def makeWeekPie(cid):
    sum = {}
    firstday = (datetime.datetime.now() - datetime.timedelta(days = 7)).date()
    
    records = db.GqlQuery('SELECT * FROM userDB WHERE cid = \'' + cid + '\' AND date >= DATE(\'' + str(firstday) + '\')' )
    for x in records:
        if str(x.category) not in sum.keys(): sum[str(x.category)]=0
        sum[str(x.category)] = sum[str(x.category)] + int(x.amount)
        
    list = ['food' ,'transport','shopping','entertainment','healthcare','education','others']
    for x in list:
        if x  not in sum.keys():
            sum[x] = 0
    
    return sum

def makeMonthPie(cid):
    sum = {}
    
    firstday = datetime.date(int(datetime.datetime.now().year),int(datetime.datetime.now().month),1)
    records = db.GqlQuery('SELECT * FROM userDB WHERE cid = \'' + cid + '\' AND date >= DATE(\'' + str(firstday) + '\')' )
    for x in records:
        if str(x.category) not in sum.keys(): sum[str(x.category)]=0
        sum[str(x.category)] = sum[str(x.category)] + int(x.amount)
        
    list = ['food' ,'transport','shopping','entertainment','healthcare','education','others']
    for x in list:
        if x  not in sum.keys():
            sum[x] = 0
    
    return sum

def makeYearPie(cid):
    sum = {}
    firstdate = datetime.date(int(datetime.datetime.now().year),1,1)
    records = db.GqlQuery('SELECT * FROM userDB WHERE cid = \'' + cid + '\' AND date >= DATE(\'' + str(firstdate) + '\')' )
    for x in records:
        if str(x.category) not in sum.keys(): sum[str(x.category)]=0
        sum[str(x.category)] = sum[str(x.category)] + int(x.amount)
        
    list = ['food' ,'transport','shopping','entertainment','healthcare','education','others']
    for x in list:
        if x  not in sum.keys():
            sum[x] = 0
    
    return sum

def makeDailyTable(cid):
    return  db.GqlQuery('SELECT * FROM userDB WHERE cid = \'' + cid + '\' AND date = DATE(\'' + str(datetime.datetime.now().date()) + '\')')
    
def makeWeekTable(cid):
    firstday = (datetime.datetime.now() - datetime.timedelta(days = 7)).date()
    return db.GqlQuery('SELECT * FROM userDB WHERE cid = \'' + cid + '\' AND date >= DATE(\'' + str(firstday) + '\')' )
    
def makeMonthTable(cid):
    firstday = datetime.date(int(datetime.datetime.now().year),int(datetime.datetime.now().month),1)
    return db.GqlQuery('SELECT * FROM userDB WHERE cid = \'' + cid + '\' AND date >= DATE(\'' + str(firstday) + '\')' )
    
def makeYearTable(cid):
    firstdate = datetime.date(int(datetime.datetime.now().year),1,1)
    return db.GqlQuery('SELECT * FROM userDB WHERE cid = \'' + cid + '\' AND date >= DATE(\'' + str(firstdate) + '\')' )

def getRecords(value,cid):
    sum ={}
    prevDate = (datetime.datetime.now() - datetime.timedelta(days = int(value))).date()
    records = db.GqlQuery('SELECT * FROM userDB WHERE cid = \'' + cid + '\' AND date >= DATE(\'' + str(prevDate) + '\')' )
    for x in records:
        if str(x.category) not in sum.keys(): sum[str(x.category)]=0
        sum[str(x.category)] = sum[str(x.category)] + int(x.amount)
        
    list = ['food' ,'transport','shopping','entertainment','healthcare','education','others']
    for x in list:
        if x  not in sum.keys():
            sum[x] = 0
    
    return {'sum':sum,'records':records}
