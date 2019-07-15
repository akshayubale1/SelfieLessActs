import sqlite3
import time
import datetime
import random
import json
import re
import hashlib
import base64
import binascii
from flask import Flask,jsonify,request,make_response,Response,abort,Response





app = Flask(__name__)

"""
from flask_cors import CORS
cors=CORS(app)
"""


@app.errorhandler(404)
def not_found(error):
     return make_response(jsonify({'error':'Not found'}),404)



@app.route('/api/v1/users',methods=['POST'])
def add_user():
     conn10 = sqlite3.connect("users.db")
     c10 = conn10.cursor()
     c10.execute("select *from  _count")
     count=0
     for row in c10.fetchall():
         #print(row[0])
         count=row[0]
     count=count+1
     print(count)
     c10.execute('UPDATE _count set count=(?) ',(count,))
     conn10.commit()    
     c10.close()
     conn10.close()
     
     if not request.json:
          abort(400)
     conn = sqlite3.connect("users.db")
     c = conn.cursor()
     data = request.json
     try:
          if(data["username"]):
               print("")
     except:
          return make_response(jsonify("username"),400)
     
     try:
          if(data["password"]):
               print("")
     except:
          return make_response(jsonify("password"),400)
     row = (data['username'],data['password'])
     c.execute("SELECT * FROM users")
     for row1 in c.fetchall():
               if(row1[0]==row[0]):
                  return make_response(jsonify("username"),400)
              
     hexval=data["password"]
     #print(type(hexval))
     pattern = re.compile(r'\b[0-9a-f]{40}\b')
     match = re.match(pattern,hexval)
     
     #print(type(match))              
     time.sleep(4)
     try:
        if(match.group(0)==hexval):
          c.execute('INSERT INTO users(username,password) VALUES (?,?)',row)
          conn.commit()    
          c.close()
          conn.close()
          return jsonify({}),201
     except:
        return make_response(jsonify("password"),400)
     
     
     
   



@app.route('/api/v1/users/<string:username>',methods=['DELETE'])
def delete_user(username):
    conn10 = sqlite3.connect("users.db")
    c10 = conn10.cursor()
    c10.execute("select *from  _count")
    count=0
    for row in c10.fetchall():
       #print(row[0])
       count=row[0]
    count=count+1
    print(count)
    c10.execute('UPDATE _count set count=(?) ',(count,))
    conn10.commit()    
    c10.close()
    conn10.close()    
    
    conn = sqlite3.connect("users.db")
    c = conn.cursor()       
    c.execute("SELECT * FROM users ")
    flag=0
    try:
          if(username):
              print("akshay")
    except:
         return make_response(jsonify("username"),400)
    for row in c.fetchall():
         if(row[0]==username):
               flag=1
    if(flag==1):
             c.execute('DELETE FROM users WHERE username=(?)',(username,))             
             conn.commit()    
             c.close()
             conn.close()
             return make_response(jsonify(),200)
    if(flag==0):
             return make_response(jsonify(),400)
             


@app.route('/api/v1/users',methods=['GET'])
def list_all_users():
    conn10 = sqlite3.connect("users.db")
    c10 = conn10.cursor()
    c10.execute("select *from  _count")
    count=0
    for row in c10.fetchall():
       #print(row[0])
       count=row[0]
    count=count+1
    print(count)
    c10.execute('UPDATE _count set count=(?) ',(count,))
    conn10.commit()    
    c10.close()
    conn10.close()

    
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users")    
    #data = c.fetchall()
    #print(data)
    #row = c.fetchall()
    userslist=list()    
    for row in c.fetchall():                         
            userslist.append(row[0])
    
    #catlist={}
    if(userslist==[]):
         return make_response(jsonify("users"),204)
    conn.commit()    
    c.close()
    conn.close()    
    return  Response(json.dumps(userslist), mimetype='application/json')






@app.route('/api/v1/_count',methods=['GET'])
def count_requests():
    conn10 = sqlite3.connect("users.db")
    c10 = conn10.cursor()
    c10.execute("select *from _count")
    count=0
    for row in c10.fetchall():
        count=row[0]
    conn10.commit()    
    c10.close()
    conn10.close()    
    l=list()
    l.append(count)
    return  Response(json.dumps(l), mimetype='application/json')                       







@app.route('/api/v1/_count',methods=['DELETE'])
def resest_count_requests():
    conn10 = sqlite3.connect("users.db")
    c10 = conn10.cursor()
    count=0
    c10.execute('UPDATE _count set count=(?) ',(count,))
    conn10.commit()    
    c10.close()
    conn10.close()
    l1=dict()
    return  Response(json.dumps(l1), mimetype='application/json')




if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=80)



