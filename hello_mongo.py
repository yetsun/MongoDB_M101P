import bottle
import pymongo


@bottle.route("/")
def index():
    
    conn = pymongo.MongoClient('localhost', 27017)
    
    db = conn.test
    
    names = db.names.find()
    
    result = ''
    
    for name in names:
        result += '<b>Hello ' + name['first_name'] + ' ' + name['last_name'] + '</b><p>'
        
    return result
    
    
bottle.run(host='localhost', port=8080)