def getCategoryFromTextToNumber(x):
    if x == 'food': return 1
    else : return 0
    
def getSpeechToText(recordURL):
    return 'pasta'
       
def getCategory(category):
    #add speech to text of the file in record URL and return the category
    category = getCategoryFromNumber(category)
    return category


def findInFile(x,text):
    f = open(x,'r')
    while f:
        if f.readline().split()[0] == text:return 1
    return 0  

def getCategoryFromText(text):
    found = 0
    category = 'others'
    list = ['category-db/db-food.txt','category-db/db-transport.txt']
    categoryNumber = 0
    i = 0 
    for x in list:
        found = findInFile(x,text)
        if found == 1:
            categoryNumber = i + 1
            break
        i = i+1
    category = getCategoryFromNumber(categoryNumber)
    return category
    #TODO implement for other categories
         