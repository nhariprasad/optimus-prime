from google.appengine.ext import db

class userDB(db.Model):
    cid = db.StringProperty()
    date = db.DateProperty(auto_now_add=True)
    amount = db.StringProperty()
    category = db.StringProperty()
