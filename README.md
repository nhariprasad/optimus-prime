eX-Opti
=======
-------

eX-Opti is a multi-platform expense management system built on the cloud and hosted on Google App Engine. It can be accessed either through a PC or a mobile web browser or through telephony.


THE INTERFACE:
==============

1) WEBSITE (Mobile Browser Optimized) - http://ex-opti.appspot.com
=====================================

User logs in using his mobile number and a password. A tabbed interface provides the user with options to add a new entry(category of spending and amount), view analytics of existing entries (by current day, week, month, year or a custom no. of days) and perform transactions. 


2) TELEPHONY - Call +91-4466949325
==================================
User calls a number (provided by Kookoo API) and responds to a set of queries. First he is presented with a main menu where he selects whether he wants to add a new entry, obtain analytics of previous spendings or make a transaction using the ZAP API.

Adding a new entry:
He is asked to choose the category of spending and then enter the amount spent using the keypad. The caller id, amount, category and date are then stored on the App Engine Datastore. 

Analytics of previous spendings:
Quick Analysis: The day's total Spending
Detailed Analysis: Total spending (current week, current month, current year)

Make transactions:
Will be done using ZAP API


THE IMPLEMENTATION:
===================
Both the website as well as the telephony app were implemented in Python (Version 2.7).  It uses the following APIs:

1) Kookoo API (www.kookoo.in) <br>
2) Google Charts API <br>


TODO List Of Features:
======================

1) Password Authentication - Since we were not clear about what details the ZAP API wanted for user authentication. <br>
2) Make Transactions - Due to unavailability of ZAP API access. <br>

TEAM:
=====
Aayush Ahuja - aayushahuja@gmail.com<br>
N Hari Prasad - hari.excellence@gmail.com
