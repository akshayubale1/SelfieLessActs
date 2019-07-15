import sqlite3
import time
import datetime
import random
import sqlite3
import time
import datetime
import random
import json
import re
import hashlib
import base64
import binascii
import commands
import os
from flask import Flask,jsonify,request,make_response,Response,abort,Response
import requests

app = Flask(__name__)

"""
from flask_cors import CORS
cors=CORS(app)
"""

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}),404)





@app.route('/api/v1/categories',methods=['GET'])
def list_all_category():
     conn1= sqlite3.connect("orchestration.db")
     c1 = conn1.cursor() 
     c1.execute("select *from _count") 
     count=0
     for row in c1.fetchall():
             count=row[0]
     count=count+1
     #print(count)
     conn1.commit()    
     c1.close()
     conn1.close()

     conn2= sqlite3.connect("orchestration.db")
     c2 = conn2.cursor()      
     c2.execute('UPDATE  _count set count=(?)',(count,)) 
     conn2.commit()    
     c2.close()
     conn2.close()
     
     conn1= sqlite3.connect("orchestration.db")
     c1 = conn1.cursor() 
     portno=0
     c1.execute("select *from container") 
     store=c1.fetchall()
     print(store)
     for row in store:
              if(row[2]==1):
                   portno=row[1]
                   break
     c=0
     for row in store:
               c=c+1
     #print(c)
     if(c==1):
                req='http://localhost:'+str(portno)+'/api/v1/categories'
                resp=requests.get(req)
                try:  
                   resp1=resp.json()
                except:
                   resp1=[]
                conn1.commit()    
                c1.close()
                conn1.close()
                return make_response(jsonify(resp1),resp.status_code)
     
     else:
         nxtportno=8000+((portno+1)%c)
         for row in store:
                 print(row[2])
                 if(row[1]==portno):
                          conn1= sqlite3.connect("orchestration.db")
                          c1 = conn1.cursor()                           
                          c1.execute("update container set rr=(?) where port=(?)",(0,portno)) 
                          conn1.commit()    
                          c1.close()
                          conn1.close()
                 
                 if(row[1]==nxtportno):
                          conn1= sqlite3.connect("orchestration.db")
                          c1 = conn1.cursor()                           
                          c1.execute("update container set rr=(?) where port=(?)",(1,nxtportno)) 
                          conn1.commit()    
                          c1.close()
                          conn1.close()

         req="http://localhost:"+str(portno)+"/api/v1/categories"
         print(portno)
         resp=requests.get(req)
         try:  
              resp1=resp.json()
         except:
              resp1=[]
         return make_response(jsonify(resp1),resp.status_code)



@app.route('/api/v1/acts',methods=['GET'])
def count_acts():
     conn1= sqlite3.connect("orchestration.db")
     c1 = conn1.cursor() 
     c1.execute("select *from _count") 
     count=0
     for row in c1.fetchall():
             count=row[0]
     count=count+1
     #print(count)
     conn1.commit()    
     c1.close()
     conn1.close()

     conn2= sqlite3.connect("orchestration.db")
     c2 = conn2.cursor()      
     c2.execute('UPDATE  _count set count=(?)',(count,)) 
     conn2.commit()    
     c2.close()
     conn2.close()
     
     conn1= sqlite3.connect("orchestration.db")
     c1 = conn1.cursor() 
     portno=0
     c1.execute("select *from container") 
     store=c1.fetchall()
     print(store)
     for row in store:
              if(row[2]==1):
                   portno=row[1]
                   break
     c=0
     for row in store:
               c=c+1
     #print(c)
     if(c==1):
                req='http://localhost:'+str(portno)+'/api/v1/categories'
                resp=requests.get(req)
                try:  
                   resp1=resp.json()
                except:
                   resp1=[]
                conn1.commit()    
                c1.close()
                conn1.close()
                return make_response(jsonify(resp1),resp.status_code)
     
     else:
         nxtportno=8000+((portno+1)%c)
         for row in store:
                 print(row[2])
                 if(row[1]==portno):
                          conn1= sqlite3.connect("orchestration.db")
                          c1 = conn1.cursor()                           
                          c1.execute("update container set rr=(?) where port=(?)",(0,portno)) 
                          conn1.commit()    
                          c1.close()
                          conn1.close()
                 
                 if(row[1]==nxtportno):
                          conn1= sqlite3.connect("orchestration.db")
                          c1 = conn1.cursor()                           
                          c1.execute("update container set rr=(?) where port=(?)",(1,nxtportno)) 
                          conn1.commit()    
                          c1.close()
                          conn1.close()

     req="http://localhost:"+str(portno)+"/api/v1/categories"
     print(portno)
     resp=requests.get(req)
     try:  
            resp1=resp.json()
     except:
            resp1=[]
     
     return make_response(jsonify(resp1),resp.status_code)



@app.route('/api/v1/acts',methods=['POST'])
def upload_an_act():
     conn1= sqlite3.connect("orchestration.db")
     c1 = conn1.cursor() 
     c1.execute("select *from _count") 
     count=0
     for row in c1.fetchall():
             count=row[0]
     count=count+1
     #print(count)
     conn1.commit()    
     c1.close()
     conn1.close()

     conn2= sqlite3.connect("orchestration.db")
     c2 = conn2.cursor()      
     c2.execute('UPDATE  _count set count=(?)',(count,)) 
     conn2.commit()    
     c2.close()
     conn2.close()
     
     conn1= sqlite3.connect("orchestration.db")
     c1 = conn1.cursor() 
     portno=0
     c1.execute("select *from container") 
     store=c1.fetchall()
     print(store)
     for row in store:
              if(row[2]==1):
                   portno=row[1]
                   break
     c=0
     for row in store:
               c=c+1
     #print(c)
     if(c==1):
                req='http://localhost:'+str(portno)+'/api/v1/categories'
                resp=requests.get(req)
                try:  
                   resp1=resp.json()
                except:
                   resp1=[]
                conn1.commit()    
                c1.close()
                conn1.close()
                return make_response(jsonify(resp1),resp.status_code)
     
     else:
         nxtportno=8000+((portno+1)%c)
         for row in store:
                 print(row[2])
                 if(row[1]==portno):
                          conn1= sqlite3.connect("orchestration.db")
                          c1 = conn1.cursor()                           
                          c1.execute("update container set rr=(?) where port=(?)",(0,portno)) 
                          conn1.commit()    
                          c1.close()
                          conn1.close()
                 
                 if(row[1]==nxtportno):
                          conn1= sqlite3.connect("orchestration.db")
                          c1 = conn1.cursor()                           
                          c1.execute("update container set rr=(?) where port=(?)",(1,nxtportno)) 
                          conn1.commit()    
                          c1.close()
                          conn1.close()

     req="http://localhost:"+str(portno)+"/api/v1/categories"
     print(portno)
     resp=requests.get(req)
     
     return make_response(jsonify({}),resp.status_code)





@app.route('/api/v1/_crash',methods=['post'])
def crashserver():
     conn1= sqlite3.connect("orchestration.db")
     c1 = conn1.cursor() 
     c1.execute("select *from _count") 
     count=0
     for row in c1.fetchall():
             count=row[0]
     count=count+1
     #print(count)
     conn1.commit()    
     c1.close()
     conn1.close()

     conn2= sqlite3.connect("orchestration.db")
     c2 = conn2.cursor()      
     c2.execute('UPDATE  _count set count=(?)',(count,)) 
     conn2.commit()    
     c2.close()
     conn2.close()
     
     conn1= sqlite3.connect("orchestration.db")
     c1 = conn1.cursor() 
     portno=0
     c1.execute("select *from container") 
     store=c1.fetchall()
     print(store)
     for row in store:
              if(row[2]==1):
                   portno=row[1]
                   break
     c=0
     for row in store:
               c=c+1
     #print(c)
     if(c==1):
                req='http://localhost:'+str(portno)+'/api/v1/categories'
                resp=requests.get(req)
                try:  
                   resp1=resp.json()
                except:
                   resp1=[]
                conn1.commit()    
                c1.close()
                conn1.close()
                return make_response(jsonify(resp1),resp.status_code)
     
     else:
         nxtportno=8000+((portno+1)%c)
         for row in store:
                 print(row[2])
                 if(row[1]==portno):
                          conn1= sqlite3.connect("orchestration.db")
                          c1 = conn1.cursor()                           
                          c1.execute("update container set rr=(?) where port=(?)",(0,portno)) 
                          conn1.commit()    
                          c1.close()
                          conn1.close()
                 
                 if(row[1]==nxtportno):
                          conn1= sqlite3.connect("orchestration.db")
                          c1 = conn1.cursor()                           
                          c1.execute("update container set rr=(?) where port=(?)",(1,nxtportno)) 
                          conn1.commit()    
                          c1.close()
                          conn1.close()

     req="http://localhost:"+str(portno)+"/api/v1/categories"
     print(portno)
     resp=requests.get(req)
     return make_response(jsonify({}),resp.status_code)








@app.route('/api/v1/_health',methods=['get'])
def check_health():

     conn1= sqlite3.connect("orchestration.db")
     c1 = conn1.cursor() 
     c1.execute("select *from _count") 
     count=0
     for row in c1.fetchall():
             count=row[0]
     count=count+1
     #print(count)
     conn1.commit()    
     c1.close()
     conn1.close()

     conn2= sqlite3.connect("orchestration.db")
     c2 = conn2.cursor()      
     c2.execute('UPDATE  _count set count=(?)',(count,)) 
     conn2.commit()    
     c2.close()
     conn2.close()
     
     conn1= sqlite3.connect("orchestration.db")
     c1 = conn1.cursor() 
     portno=0
     c1.execute("select *from container") 
     store=c1.fetchall()
     print(store)
     for row in store:
              if(row[2]==1):
                   portno=row[1]
                   break
     c=0
     for row in store:
               c=c+1
     #print(c)
     if(c==1):
                req='http://localhost:'+str(portno)+'/api/v1/categories'
                resp=requests.get(req)
                try:  
                   resp1=resp.json()
                except:
                   resp1=[]
                conn1.commit()    
                c1.close()
                conn1.close()
                return make_response(jsonify(resp1),resp.status_code)
     
     else:
         nxtportno=8000+((portno+1)%c)
         for row in store:
                 print(row[2])
                 if(row[1]==portno):
                          conn1= sqlite3.connect("orchestration.db")
                          c1 = conn1.cursor()                           
                          c1.execute("update container set rr=(?) where port=(?)",(0,portno)) 
                          conn1.commit()    
                          c1.close()
                          conn1.close()
                 
                 if(row[1]==nxtportno):
                          conn1= sqlite3.connect("orchestration.db")
                          c1 = conn1.cursor()                           
                          c1.execute("update container set rr=(?) where port=(?)",(1,nxtportno)) 
                          conn1.commit()    
                          c1.close()
                          conn1.close()

     req="http://localhost:"+str(portno)+"/api/v1/categories"
     print(portno)
     resp=requests.get(req)
     return make_response(jsonify({}),resp.status_code)



@app.route('/api/v1/acts/<int:actId>',methods=['DELETE'])
def remove_an_act(actId):

     conn1= sqlite3.connect("orchestration.db")
     c1 = conn1.cursor() 
     c1.execute("select *from _count") 
     count=0
     for row in c1.fetchall():
             count=row[0]
     count=count+1
     #print(count)
     conn1.commit()    
     c1.close()
     conn1.close()

     conn2= sqlite3.connect("orchestration.db")
     c2 = conn2.cursor()      
     c2.execute('UPDATE  _count set count=(?)',(count,)) 
     conn2.commit()    
     c2.close()
     conn2.close()
     
     conn1= sqlite3.connect("orchestration.db")
     c1 = conn1.cursor() 
     portno=0
     c1.execute("select *from container") 
     store=c1.fetchall()
     print(store)
     for row in store:
              if(row[2]==1):
                   portno=row[1]
                   break
     c=0
     for row in store:
               c=c+1
     #print(c)
     if(c==1):
                req='http://localhost:'+str(portno)+'/api/v1/categories'
                resp=requests.get(req)
                try:  
                   resp1=resp.json()
                except:
                   resp1=[]
                conn1.commit()    
                c1.close()
                conn1.close()
                return make_response(jsonify(resp1),resp.status_code)
     
     else:
         nxtportno=8000+((portno+1)%c)
         for row in store:
                 print(row[2])
                 if(row[1]==portno):
                          conn1= sqlite3.connect("orchestration.db")
                          c1 = conn1.cursor()                           
                          c1.execute("update container set rr=(?) where port=(?)",(0,portno)) 
                          conn1.commit()    
                          c1.close()
                          conn1.close()
                 
                 if(row[1]==nxtportno):
                          conn1= sqlite3.connect("orchestration.db")
                          c1 = conn1.cursor()                           
                          c1.execute("update container set rr=(?) where port=(?)",(1,nxtportno)) 
                          conn1.commit()    
                          c1.close()
                          conn1.close()

     req="http://localhost:"+str(portno)+"/api/v1/categories"
     print(portno)
     resp=requests.get(req)
     
     return make_response(jsonify({}),resp.status_code)




          

@app.route('/api/v1/acts/upvote',methods=['POST'])
def upvote_an_act():
     conn1= sqlite3.connect("orchestration.db")
     c1 = conn1.cursor() 
     c1.execute("select *from _count") 
     count=0
     for row in c1.fetchall():
             count=row[0]
     count=count+1
     #print(count)
     conn1.commit()    
     c1.close()
     conn1.close()

     conn2= sqlite3.connect("orchestration.db")
     c2 = conn2.cursor()      
     c2.execute('UPDATE  _count set count=(?)',(count,)) 
     conn2.commit()    
     c2.close()
     conn2.close()
     
     conn1= sqlite3.connect("orchestration.db")
     c1 = conn1.cursor() 
     portno=0
     c1.execute("select *from container") 
     store=c1.fetchall()
     print(store)
     for row in store:
              if(row[2]==1):
                   portno=row[1]
                   break
     c=0
     for row in store:
               c=c+1
     #print(c)
     if(c==1):
                req='http://localhost:'+str(portno)+'/api/v1/categories'
                resp=requests.get(req)
                try:  
                   resp1=resp.json()
                except:
                   resp1=[]
                conn1.commit()    
                c1.close()
                conn1.close()
                return make_response(jsonify(resp1),resp.status_code)
     
     else:
         nxtportno=8000+((portno+1)%c)
         for row in store:
                 print(row[2])
                 if(row[1]==portno):
                          conn1= sqlite3.connect("orchestration.db")
                          c1 = conn1.cursor()                           
                          c1.execute("update container set rr=(?) where port=(?)",(0,portno)) 
                          conn1.commit()    
                          c1.close()
                          conn1.close()
                 
                 if(row[1]==nxtportno):
                          conn1= sqlite3.connect("orchestration.db")
                          c1 = conn1.cursor()                           
                          c1.execute("update container set rr=(?) where port=(?)",(1,nxtportno)) 
                          conn1.commit()    
                          c1.close()
                          conn1.close()

     req="http://localhost:"+str(portno)+"/api/v1/categories"
     print(portno)
     resp=requests.get(req)
     
     return make_response(jsonify({}),resp.status_code)





@app.route('/api/v1/categories/<string:cat1name>/acts',methods=['GET'])
def no_of_acts_in_a_range(cat1name):
     conn1= sqlite3.connect("orchestration.db")
     c1 = conn1.cursor() 
     c1.execute("select *from _count") 
     count=0
     for row in c1.fetchall():
             count=row[0]
     count=count+1
     #print(count)
     conn1.commit()    
     c1.close()
     conn1.close()

     conn2= sqlite3.connect("orchestration.db")
     c2 = conn2.cursor()      
     c2.execute('UPDATE  _count set count=(?)',(count,)) 
     conn2.commit()    
     c2.close()
     conn2.close()
     
     conn1= sqlite3.connect("orchestration.db")
     c1 = conn1.cursor() 
     portno=0
     c1.execute("select *from container") 
     store=c1.fetchall()
     print(store)
     for row in store:
              if(row[2]==1):
                   portno=row[1]
                   break
     c=0
     for row in store:
               c=c+1
     #print(c)
     if(c==1):
                req='http://localhost:'+str(portno)+'/api/v1/categories'
                resp=requests.get(req)
                try:  
                   resp1=resp.json()
                except:
                   resp1=[]
                conn1.commit()    
                c1.close()
                conn1.close()
                return make_response(jsonify(resp1),resp.status_code)
     
     else:
         nxtportno=8000+((portno+1)%c)
         for row in store:
                 print(row[2])
                 if(row[1]==portno):
                          conn1= sqlite3.connect("orchestration.db")
                          c1 = conn1.cursor()                           
                          c1.execute("update container set rr=(?) where port=(?)",(0,portno)) 
                          conn1.commit()    
                          c1.close()
                          conn1.close()
                 
                 if(row[1]==nxtportno):
                          conn1= sqlite3.connect("orchestration.db")
                          c1 = conn1.cursor()                           
                          c1.execute("update container set rr=(?) where port=(?)",(1,nxtportno)) 
                          conn1.commit()    
                          c1.close()
                          conn1.close()

         req="http://localhost:"+str(portno)+"/api/v1/categories"
         print(portno)
         resp=requests.get(req)
         try:  
              resp1=resp.json()
         except:
              resp1=[]
         return make_response(jsonify(resp1),resp.status_code)





@app.route('/api/v1/categories/<string:catname>/acts/size',methods=['GET'])
def no_of_acts(catname):

     conn1= sqlite3.connect("orchestration.db")
     c1 = conn1.cursor() 
     c1.execute("select *from _count") 
     count=0
     for row in c1.fetchall():
             count=row[0]
     count=count+1
     #print(count)
     conn1.commit()    
     c1.close()
     conn1.close()

     conn2= sqlite3.connect("orchestration.db")
     c2 = conn2.cursor()      
     c2.execute('UPDATE  _count set count=(?)',(count,)) 
     conn2.commit()    
     c2.close()
     conn2.close()
     
     conn1= sqlite3.connect("orchestration.db")
     c1 = conn1.cursor() 
     portno=0
     c1.execute("select *from container") 
     store=c1.fetchall()
     print(store)
     for row in store:
              if(row[2]==1):
                   portno=row[1]
                   break
     c=0
     for row in store:
               c=c+1
     #print(c)
     if(c==1):
                req='http://localhost:'+str(portno)+'/api/v1/categories'
                resp=requests.get(req)
                try:  
                   resp1=resp.json()
                except:
                   resp1=[]
                conn1.commit()    
                c1.close()
                conn1.close()
                return make_response(jsonify(resp1),resp.status_code)
     
     else:
         nxtportno=8000+((portno+1)%c)
         for row in store:
                 print(row[2])
                 if(row[1]==portno):
                          conn1= sqlite3.connect("orchestration.db")
                          c1 = conn1.cursor()                           
                          c1.execute("update container set rr=(?) where port=(?)",(0,portno)) 
                          conn1.commit()    
                          c1.close()
                          conn1.close()
                 
                 if(row[1]==nxtportno):
                          conn1= sqlite3.connect("orchestration.db")
                          c1 = conn1.cursor()                           
                          c1.execute("update container set rr=(?) where port=(?)",(1,nxtportno)) 
                          conn1.commit()    
                          c1.close()
                          conn1.close()

         req="http://localhost:"+str(portno)+"/api/v1/categories"
         print(portno)
         resp=requests.get(req)
         try:  
              resp1=resp.json()
         except:
              resp1=[]
         return make_response(jsonify(resp1),resp.status_code)



@app.route('/api/v1/categories/<string:catname>',methods=['DELETE'])
def delete_category(catname):
     conn1= sqlite3.connect("orchestration.db")
     c1 = conn1.cursor() 
     c1.execute("select *from _count") 
     count=0
     for row in c1.fetchall():
             count=row[0]
     count=count+1
     #print(count)
     conn1.commit()    
     c1.close()
     conn1.close()

     conn2= sqlite3.connect("orchestration.db")
     c2 = conn2.cursor()      
     c2.execute('UPDATE  _count set count=(?)',(count,)) 
     conn2.commit()    
     c2.close()
     conn2.close()
     
     conn1= sqlite3.connect("orchestration.db")
     c1 = conn1.cursor() 
     portno=0
     c1.execute("select *from container") 
     store=c1.fetchall()
     print(store)
     for row in store:
              if(row[2]==1):
                   portno=row[1]
                   break
     c=0
     for row in store:
               c=c+1
     #print(c)
     if(c==1):
                req='http://localhost:'+str(portno)+'/api/v1/categories'
                resp=requests.get(req)
                try:  
                   resp1=resp.json()
                except:
                   resp1=[]
                conn1.commit()    
                c1.close()
                conn1.close()
                return make_response(jsonify(resp1),resp.status_code)
     
     else:
         nxtportno=8000+((portno+1)%c)
         for row in store:
                 print(row[2])
                 if(row[1]==portno):
                          conn1= sqlite3.connect("orchestration.db")
                          c1 = conn1.cursor()                           
                          c1.execute("update container set rr=(?) where port=(?)",(0,portno)) 
                          conn1.commit()    
                          c1.close()
                          conn1.close()
                 
                 if(row[1]==nxtportno):
                          conn1= sqlite3.connect("orchestration.db")
                          c1 = conn1.cursor()                           
                          c1.execute("update container set rr=(?) where port=(?)",(1,nxtportno)) 
                          conn1.commit()    
                          c1.close()
                          conn1.close()

     req="http://localhost:"+str(portno)+"/api/v1/categories"
     print(portno)
     resp=requests.get(req)
     return make_response(jsonify({}),resp.status_code)



@app.route('/api/v1/categories',methods=['POST'])
def add_category():
     conn1= sqlite3.connect("orchestration.db")
     c1 = conn1.cursor() 
     c1.execute("select *from _count") 
     count=0
     for row in c1.fetchall():
             count=row[0]
     count=count+1
     #print(count)
     conn1.commit()    
     c1.close()
     conn1.close()

     conn2= sqlite3.connect("orchestration.db")
     c2 = conn2.cursor()      
     c2.execute('UPDATE  _count set count=(?)',(count,)) 
     conn2.commit()    
     c2.close()
     conn2.close()
     
     conn1= sqlite3.connect("orchestration.db")
     c1 = conn1.cursor() 
     portno=0
     c1.execute("select *from container") 
     store=c1.fetchall()
     print(store)
     for row in store:
              if(row[2]==1):
                   portno=row[1]
                   break
     c=0
     for row in store:
               c=c+1
     #print(c)
     if(c==1):
                req='http://localhost:'+str(portno)+'/api/v1/categories'
                resp=requests.get(req)
                try:  
                   resp1=resp.json()
                except:
                   resp1=[]
                conn1.commit()    
                c1.close()
                conn1.close()
                return make_response(jsonify(resp1),resp.status_code)
     
     else:
         nxtportno=8000+((portno+1)%c)
         for row in store:
                 print(row[2])
                 if(row[1]==portno):
                          conn1= sqlite3.connect("orchestration.db")
                          c1 = conn1.cursor()                           
                          c1.execute("update container set rr=(?) where port=(?)",(0,portno)) 
                          conn1.commit()    
                          c1.close()
                          conn1.close()
                 
                 if(row[1]==nxtportno):
                          conn1= sqlite3.connect("orchestration.db")
                          c1 = conn1.cursor()                           
                          c1.execute("update container set rr=(?) where port=(?)",(1,nxtportno)) 
                          conn1.commit()    
                          c1.close()
                          conn1.close()

     req="http://localhost:"+str(portno)+"/api/v1/categories"
     print(portno)
     resp=requests.get(req)
     return make_response(jsonify({}),resp.status_code)




if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")


