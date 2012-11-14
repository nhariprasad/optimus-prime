from google.appengine.ext import db
import kookoo
import datetime
import operator


def getSpendingDetails():
    r = kookoo.Response()
    g = r.append(kookoo.CollectDtmf(maxDigits=1))
    g.append(kookoo.PlayText("Press 1 for quick analytics"))
    g.append(kookoo.PlayText("Press 2 for detailed analytics"))
    return r


def shortAnalytics(cid):
    sum=0
    records = db.GqlQuery('SELECT * FROM userDB WHERE cid = \'' + cid + '\' AND date = DATE(\'' + str(datetime.datetime.now().date()) + '\')')
    for x in records:
        sum = sum + int(x.amount)
    r = kookoo.Response()
    r.addPlayText("Todays total spending amount is " + str(sum))
    return r

def detailAnalytics(cid):
    r = kookoo.Response()
    g = r.append(kookoo.CollectDtmf(maxDigits=1))
    g.append(kookoo.PlayText("Press 1 for this week"))
    g.append(kookoo.PlayText("Press 2 for this month"))
    g.append(kookoo.PlayText("Press 3 for this year"))
    return r

def thisMonthAnalytics(cid):
    sum = {}
    firstday = datetime.date(int(datetime.datetime.now().year),int(datetime.datetime.now().month),1)
    records = db.GqlQuery('SELECT * FROM userDB WHERE cid = \'' + cid + '\' AND date >= DATE(\'' + str(firstday) + '\')' )
    for x in records:
        if str(x.category) not in sum.keys(): sum[str(x.category)]=0
        sum[str(x.category)] = sum[str(x.category)] + int(x.amount)
        
        
    sum = sorted(sum.iteritems(), key=operator.itemgetter(1), reverse = True)
    r = kookoo.Response()
    total = 0
    for x,y in sum:
        total = total + y
    r.addPlayText("this months total amount is " + str(total))
    r.addPlayText("the top categories of spending are")
    i = 1
    for key in sum: 
        r.addPlayText(str(key))
        if i >= 5 :break
        i = i+1;
    return r



def thisWeekAnalytics(cid):
    sum = {}
    
    firstday = (datetime.datetime.now() - datetime.timedelta(days = 7)).date()
    
    records = db.GqlQuery('SELECT * FROM userDB WHERE cid = \'' + cid + '\' AND date >= DATE(\'' + str(firstday) + '\')' )
    for x in records:
        if str(x.category) not in sum.keys(): sum[str(x.category)]=0
        sum[str(x.category)] = sum[str(x.category)] + int(x.amount)

        
        
    sum = sorted(sum.iteritems(), key=operator.itemgetter(1), reverse = True)
    r = kookoo.Response()
    r.addPlayText("this weeks total amount is " + str(sum))
    r.addPlayText("the top categories of spending are")
    i = 1
    for key in sum: 
        r.addPlayText(str(key))
        if i >= 5 :break
        i = i+1;
    return r




def yearAnalytics(cid):
    sum = {}
    firstdate = date(1,1,datetime.datetime.now().year)
    records = db.GqlQuery('SELECT * FROM userDB WHERE cid = \'' + cid + '\' AND date >= DATE(\'' + str(firstdate) + '\')' )
    for x in records:
        if str(x.category) not in sum.keys(): sum[str(x.category)]=0
        sum[str(x.category)] = sum[str(x.category)] + int(x.amount)

        
        
    sum = sorted(sum.iteritems(), key=operator.itemgetter(1), reverse = True)
    r = kookoo.Response()
    r.addPlayText("this years total amount is " + str(sum))
    r.addPlayText("the top categories of spending are")
    i = 1
    for key in sum: 
        r.addPlayText(str(key))
        if i >= 5 :break
        i = i+1;
    return r
    
    
    