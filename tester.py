import httplib

#host = "localhost:8080"
host = "ex-opti.appspot.com"
def NewCallTest():
    conn = httplib.HTTPConnection(host)
    conn.request("GET", "/?event=NewCall&cid=9602904775&called_number=914466949325&sid=413477837012464&circle=RAJASTHAN&operator=AIRTEL")
    r1 = conn.getresponse()
    data = r1.read()
    print data
def GotDTMFAddEntryTest():
    conn = httplib.HTTPConnection(host)
    conn.request("GET", "/?event=GotDTMF&sid=413477837012464&data=1")
    r1 = conn.getresponse()
    data = r1.read()
    print data

def GotDTMFCategoryTest():
    conn = httplib.HTTPConnection(host)
    conn.request("GET", "/?event=GotDTMF&sid=413477837012464&data=1")
    r1 = conn.getresponse()
    data = r1.read()
    print data
    
def AmountDTMFTest():
    conn = httplib.HTTPConnection(host)
    conn.request("GET", "/?event=GotDTMF&sid=413477837012464&data=1600")
    r1 = conn.getresponse()
    data = r1.read()
    print data

def GotDTMFSpendingTest():
    conn = httplib.HTTPConnection(host)
    conn.request("GET", "/?event=GotDTMF&sid=413477837012464&data=2")
    r1 = conn.getresponse()
    data = r1.read()
    print data

def GotDTMFDetailAnalyticsTest():
    conn = httplib.HTTPConnection(host)
    conn.request("GET", "/?event=GotDTMF&sid=413477837012464&data=2")
    r1 = conn.getresponse()
    data = r1.read()
    print data
    
    
def GotDTMFShortAnalyticsTest():
    conn = httplib.HTTPConnection(host)
    conn.request("GET", "/?event=GotDTMF&sid=413477837012464&data=1")
    r1 = conn.getresponse()
    data = r1.read()
    print data
    
def GotDTMFThisMonthAnalyticsTest():
    conn = httplib.HTTPConnection(host)
    conn.request("GET", "/?event=GotDTMF&sid=413477837012464&data=2")
    r1 = conn.getresponse()
    data = r1.read()
    print data
    


#conn = httplib.HTTPConnection(host)
def option1():
    NewCallTest()
    GotDTMFAddEntryTest()
    GotDTMFCategoryTest()
    AmountDTMFTest()
    
def option2():
    print 'option2 is selcted'
    NewCallTest()
    GotDTMFSpendingTest()
    GotDTMFShortAnalyticsTest()
    #GotDTMFThisMonthAnalyticsTest()
    
    
    
option2()