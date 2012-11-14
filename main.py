#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import webapp2
import wsgiref.handlers
from google.appengine.ext.webapp import template
from session_module import *

from entry import *
from analytics import *
from dataBase import *
from entry_web import *
from pygooglechart import PieChart3D


from math import pow,ceil
import datetime


last = ''
cid = ''

class LoginHandler(BaseHandler):  
    def get(self):
        self.response.out.write(template.render('templates/loginpage/app.html',{}))
    def post(self):
        self.session["cid"] = self.request.get("cid")
        self.session["pin"] = self.request.get("pin")
        if str(self.session.get("pin")) == '' and str(self.session.get("cid")) == '':   #TODO CONVERT TO OR
            self.response.out.write(template.render('templates/loginpage/app.html',{
                                    'error':'Specify Account Details'
                                    })) 
        else: self.response.out.write(template.render('templates/addentrypage/app.html',{
                                                                                         }))  
       
class MainHandler(BaseHandler):
    def get(self):
        event = str(self.request.get('event'))
        if not event:
            if not self.session.get("cid"): self.redirect("/login")
            else:self.redirect("/addentry/") 
        else:
            if event == 'NewCall' :
                global cid
                cid = self.request.get('cid')
                r = welcome()
                self.response.out.write(r)
                global last
                last = 'MainMenu'
            elif event == 'GotDTMF' and last == 'MainMenu':
                global last
                choice = self.request.get('data')
                
                if choice == '1':
                    r = addEntry()
                    self.response.out.write(r)
                    global last 
                    last = 'addEntry'
                    
                elif choice == '2':
                    r = getSpendingDetails()
                    self.response.out.write(r)
                    global last
                    last = 'getSpendingDetails'
                    
                elif choice == '3':
                    
                    makeTransaction()
                    global last
                    last = 'makeTransaction'
                    
                    
            elif event == 'GotDTMF' and last == 'addEntry':
                global category
                category = self.request.get('data')
                r = enterAmount()
                self.response.out.write(r)
                global last
                last = 'enterAmount'
            elif event == 'GotDTMF' and last == 'enterAmount':
                amount = self.request.get('data')
                global cid
                global category
                updateDB(cid, category, amount)
                global last
                last = 'updateDB'
                    
            elif event == 'GotDTMF' and last == 'getSpendingDetails':
                choice = self.request.get('data')
                global cid
                if choice == '1': 
                    r = shortAnalytics(cid)
                    self.response.out.write(r)
                    global last
                    last = 'shortAnalytics'
                    
                else : 
                    r = detailAnalytics(cid)
                    self.response.out.write(r)
                    global last
                    last = 'detailAnalytics'
                    
            elif event == 'GotDTMF' and last == 'detailAnalytics':
                choice = self.request.get('data')
                global cid
                if choice == '2': 
                    r = thisMonthAnalytics(cid)
                    self.response.out.write(r)
                    global last
                    last = 'detailAnalytics'
                    
                if choice == '1': 
                    r = thisWeekAnalytics(cid)
                    self.response.out.write(r)
                    global last
                    last = 'detailAnalytics'
                    
                    r = yearAnalytics(cid)
                    self.response.out.write(r)
                    global last
                    last = 'detailAnalytics'
                    
            elif last=='detailAnalytics' or last == 'shortAnalytics' or last =='updateDB':
                r = welcome()
                self.response.out.write(r)
                global last
                last = 'MainMenu'
                
            
class AddEntryHandler(BaseHandler):  
    def get(self):
        self.response.out.write(template.render('templates/addentrypage/app.html',{}))
        
    def post(self):
        choice = self.request.get("category")
        amount = self.request.get("amount")
         
        updateDB_web(str(self.session.get("cid")),choice,amount)
        self.response.out.write(template.render('templates/analyticspage/app.html',{}))
            
        
                 
class AnalysisHandler(BaseHandler): 
    def get(self):
        self.response.out.write(template.render('templates/analyticspage/app.html',{
                                        }))       
        
class AnalysisViewHandler(BaseHandler):   
    def get(self):
        time1 = self.request.get('time')
        if time1 == 'today':
            sum = makeDailyPie(str(self.session.get("cid")))
            table = makeDailyTable(str(self.session.get("cid")))
            desctable ='All Spendings'
        if time1 == 'week':
            sum = makeWeekPie(str(self.session.get("cid")))
            table = []
            for x,y in sum.items():
                table.append(userDB(amount = str(y),category = str(x)))
            desctable = 'Category wise Spending'
        if time1 == 'month':
            sum = makeMonthPie(str(self.session.get("cid")))
            table = []
            for x,y in  sum.items():
                table.append(userDB(amount = str(y),category = str(x)))
            desctable = 'Category wise Spending'
        if time1 == 'year':
            sum = makeYearPie(str(self.session.get("cid")))
            table = []
            for x,y in sum.items():
                table.append(userDB(amount = str(y),category = str(x)))
            desctable = 'Category wise Spending'
        # Create a chart object of 250x100 pixels
        chart = PieChart3D(325, 100)

        # Add some data
        categoryvalues = []
        for x in sum.values():
            if x : categoryvalues.append(x)
        chart.add_data(categoryvalues)
        
        # Assign the labels to the pie data
        categorykey=[]
        for x in sum.keys():
            if sum[x]: categorykey.append(x)
        chart.set_pie_labels(categorykey)
        
        totalSum = 0
        for x in sum.values():
            totalSum = totalSum + x
        
        # Print the chart URL
        pieURL =  chart.get_url()
        self.response.out.write(template.render('templates/analysisview/app.html',{
                                    'pieURL':pieURL,
                                    'descpie':'Relative Spendings',
                                    'desctable':desctable,
                                    'total':totalSum,
                                    'table':table,
                                    }))       
        
class CreditsHandler(BaseHandler): 
    def get(self):
        self.response.out.write(template.render('templates/credits/app.html',{
                                        })) 
        
class AboutHandler(BaseHandler): 
    def get(self):
        self.response.out.write(template.render('templates/aboutpage/app.html',{
                                        })) 
        
class CustomHandler(BaseHandler):
    def get(self):   
        self.response.out.write(template.render('templates/custom/app.html',{
                                        })) 
    def post(self):
        value = self.request.get('slider')
         
        rec = getRecords(value,str(self.session.get("cid")))
        table = rec['records']
        sum = rec['sum']
        chart = PieChart3D(325, 100)
        categoryvalues = []
        for x in sum.values():
            if x : categoryvalues.append(x)
        chart.add_data(categoryvalues)
        
        # Assign the labels to the pie data
        categorykey=[]
        for x in sum.keys():
            if sum[x]: categorykey.append(x)
        chart.set_pie_labels(categorykey)
        
        totalSum = 0
        for x in sum.values():
            totalSum = totalSum + x
        
        # Print the chart URL
        pieURL =  chart.get_url()
        self.response.out.write(template.render('templates/analysisview/app.html',{
                                    'pieURL':pieURL,
                                    'descpie':'Relative Spendings',
                                    'desctable':'Category Wise Spendings',
                                    'total':totalSum,
                                    'table':table,
                                    }))       
        
class TransactionHandler(BaseHandler):
    def get(self):
        self.response.out.write(template.render('templates/transactionpage/app.html',{}))
        
        
class LogoutHandler(BaseHandler):
    def get(self):
        self.session["cid"] = ""
        self.session["pin"] = ""
        self.response.out.write(template.render('templates/logoutpage/app.html',{
                                        })) 


        
app = webapp2.WSGIApplication([('/', MainHandler),
                               ('/login', LoginHandler),
                               ('/logout', LogoutHandler),
                               ('/addentry/',AddEntryHandler),
                               ('/analysis/',AnalysisHandler),
                               ('/analysisview/',AnalysisViewHandler),
                               ('/about', AboutHandler),
                               ('/custom/', CustomHandler),
                               ('/credits', CreditsHandler),
                               ('/transaction/',TransactionHandler),
                               ],
                              debug=True, config=config)
