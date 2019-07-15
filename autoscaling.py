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

def getcontainerID(port):          
          #result1=[]

          result = commands.getoutput("sudo docker ps -a")
          res=result.split("\n")
          res=res[1:]
          #print(res)         
          port=str(port)
          #port=list.append(port)
          for row in res:              
               #print(row)            
               portno = re.findall(port,row)               
               #print(portno)
               for n in portno:
                  if(n==port):
                      #print("inside")
                      containerID=row.split()[0]
                      return containerID
                      
 
def stopcontainer():
           conn10 = sqlite3.connect("orchestration.db")
           c10 = conn10.cursor()
           c10.execute("select *from  container")
   	   count1=0
           i=0
           store=c10.fetchall()
           for row in store:                             
                   count1=count1+1
           print(count1)
           print("inside0")
           for row in store:
                   i=i+1
                   print("inside1")
                   if(i==count1):
                        portno=row[1]                               
                        containerID=getcontainerID(portno)
                        containerID=str(containerID)
                        cmnd="sudo docker stop "+containerID
                        cmnd1="sudo docker rm "+containerID
                        j=0
                        if(row[2]==1):
                                for row1 in store:
                                          if(j==0):
                                               conn1= sqlite3.connect("orchestration.db")
                                               c1 = conn1.cursor()                           
                                               c1.execute("update container set rr=(?) where port=(?)",(1,row1[1])) 
                                               conn1.commit()    
                                               c1.close()
                                               conn1.close()
                        print("inside2")            
                        conn1 = sqlite3.connect("orchestration.db")
                        c1 = conn1.cursor()                
                        c1.execute("DELETE from  container where port=(?)",(portno,))
                        os.system(cmnd)
                        os.system(cmnd1)
                        conn1.commit()    
                        c1.close()
                        conn1.close()
                   
           conn10.commit()    
           c10.close()
           conn10.close()           
            






while(1):
    time.sleep(120)
    conn10 = sqlite3.connect("orchestration.db")
    c10 = conn10.cursor()
    c10.execute("select *from  _count")
    count=0
    for row in c10.fetchall():
       #print(row[0])
       count=row[0]
    print(count)    
    conn10.commit()    
    c10.close()
    conn10.close() 
    if(count==0):
           conn10 = sqlite3.connect("orchestration.db")
           c10 = conn10.cursor()
           c10.execute("select *from  container")
   	   count1=0
           for row in c10.fetchall():                             
                   count1=count1+1
           #print(count1)
           conn10.commit()    
           c10.close()
           conn10.close() 
           while(count1!=0):
               stopcontainer()
               count1=count1-1
    if(count>=1 and count<20):
           #print("inside")
           conn10 = sqlite3.connect("orchestration.db")
           c10 = conn10.cursor()
           c10.execute("select *from  container")
   	   count1=0
           for row in c10.fetchall():                             
                   count1=count1+1
           print(count1)
           conn10.commit()    
           c10.close()
           conn10.close() 
           if(count1==1):
              print("done")
              conn2= sqlite3.connect("orchestration.db")
              c2 = conn2.cursor() 
              c2.execute('UPDATE  _count set count=(?)',(0,)) 
              print("updated")
              conn2.commit()    
              c2.close()
              conn2.close()
              continue
           if(count1==0): 
              port=8000   
              print("ubale")
              cmnd="sudo docker run -d -p "+str(port)+":80 acts:latest"
              os.system(cmnd)
              conn1= sqlite3.connect("orchestration.db")
              c1 = conn1.cursor()              
              c1.execute('INSERT INTO container(containerID,port,rr) VALUES(?,?,?)',(1,port,1))
              conn1.commit()    
              c1.close()
              conn1.close()

              conn2= sqlite3.connect("orchestration.db")
              c2 = conn2.cursor() 
              c2.execute('UPDATE  _count set count=(?)',(0,)) 
              print("updated")
              conn2.commit()    
              c2.close()
              conn2.close()
              cout1=counnt1+1              
           if(count1>1):
                 #print("inside")
                 while(count1!=1):
                      stopcontainer()
                      count1=count1-1
                 if(count1==1):
                      conn3= sqlite3.connect("orchestration.db")
                      c3 = conn3.cursor() 
                      c3.execute("update _count set count=(?)",(0,))
                      conn3.commit()    
                      c3.close()
                      conn3.close()

    
  
    if(count>=20 and count<40):
           print(count)
           print("inside2")
           conn10 = sqlite3.connect("orchestration.db")
           c10 = conn10.cursor()
           c10.execute("select *from  container")
   	   count1=0
           for row in c10.fetchall():                             
                   count1=count1+1
           
           conn10.commit()    
           c10.close()
           conn10.close() 
           print(count1)
           if(count1==2):
              print("done1")
              conn2= sqlite3.connect("orchestration.db")
              c2 = conn2.cursor() 
              c2.execute('UPDATE  _count set count=(?)',(0,)) 
              print("updated")
              conn2.commit()    
              c2.close()
              conn2.close()
              continue
           if(count1<2):
                
                while(count1!=2):
                    if(count1==0):
                         print("ubale")
                         port=8000                                 
                         cmnd="sudo docker run -d -p "+str(port)+":80 acts:latest"
                         os.system(cmnd)
                         conn1= sqlite3.connect("orchestration.db")
                         c1 = conn1.cursor()              
                         c1.execute('INSERT INTO container(containerID,port,rr) VALUES(?,?,?)',(1,port,1))
                         conn1.commit()    
                         c1.close()
                         conn1.close()
                         count1=count1+1 
                    else:            
                         print("ubale1") 
                         conn1= sqlite3.connect("orchestration.db")
                         c1 = conn1.cursor() 
                         c1.execute("select *from container")                   
                         port=0

                         for row in c1.fetchall():
                              containerID=row[0]
                              port=row[1]  
                         port=port+1 
                         containerID=containerID+1
                         cmnd="sudo docker run -d -p "+str(port)+":80 acts:latest"
                         os.system(cmnd)
                         count1=count1+1                               
                         c1.execute('INSERT INTO container(containerID,port,rr) VALUES(?,?,?)',(containerID,port,0))
                         
                         conn1.commit()    
                         c1.close()
                         conn1.close()

                         conn2= sqlite3.connect("orchestration.db")
                         c2 = conn2.cursor() 
                         c=0
                         c2.execute('UPDATE  _count set count=(?)',(c,)) 
                         conn2.commit()    
                         c2.close()
                         conn2.close()
           if(count1>2):
                while(count1!=2):
                    stopcontainer()
                    count1=count1-1
                if(count1==2):
                      conn3= sqlite3.connect("orchestration.db")
                      c3 = conn3.cursor() 
                      c3.execute("update _count set count=(?)",(0,))
                      conn3.commit()    
                      c3.close()
                      conn3.close()
    if(count>=40 and count<60):
           conn10 = sqlite3.connect("orchestration.db")
           c10 = conn10.cursor()
           c10.execute("select *from  container")
   	   count1=0
           for row in c10.fetchall():             
                   count1=count1+1
           print(count1)
           conn10.commit()    
           c10.close()
           conn10.close() 
           if(count1==3):
              print("done1")
              conn2= sqlite3.connect("orchestration.db")
              c2 = conn2.cursor() 
              c2.execute('UPDATE  _count set count=(?)',(0,)) 
              print("updated")
              conn2.commit()    
              c2.close()
              conn2.close()
              continue
           if(count1<3):
             while(count1!=3):  
                if(count1==0): 
                       port=8000                    
                       cmnd="sudo docker run -d -p "+str(port)+":80 acts:latest"
                       os.system(cmnd)
                       conn1= sqlite3.connect("orchestration.db")
                       c1 = conn1.cursor()              
                       c1.execute('INSERT INTO container(containerID,port,rr) VALUES(?,?,?)',(1,port,1))
                       conn1.commit()    
                       c1.close()
                       conn1.close()
                       count1=count1+1 
                else:             
                       conn1= sqlite3.connect("orchestration.db")
                       c1 = conn1.cursor() 
                       c1.execute("select *from container") 
                  
                       port=0
                       containerID=0
                       for row in c1.fetchall():
                          containerID=row[0]
                          port=row[1]  
                       port=port+1
                       containerID=containerID+1
                       cmnd="sudo docker run -d -p "+str(port)+":80 acts:latest"
                       os.system(cmnd)
                       count1=count1+1
                       c1.execute('INSERT INTO container(containerID,port,rr) VALUES(?,?,?)',(containerID,port,0))
                       conn1.commit()    
                       c1.close()
                       conn1.close()
                       conn2= sqlite3.connect("orchestration.db")
                       c2 = conn2.cursor() 
                       c=0
                       c2.execute('UPDATE  _count set count=(?)',(c,)) 
                       conn2.commit()    
                       c2.close()
                       conn2.close()
           if(count1>3):
                while(count1!=3):
                       stopcontainer()
                       count1=count1-1
                if(count1==3):
                      conn3= sqlite3.connect("orchestration.db")
                      c3 = conn3.cursor() 
                      c3.execute("update _count set count=(?)",(0,))
                      conn3.commit()    
                      c3.close()
                      conn3.close()
    if(count>=60):
           conn10 = sqlite3.connect("orchestration.db")
           c10 = conn10.cursor()
           c10.execute("select *from  container")
   	   count1=0
           for row in c10.fetchall():  
                           
                   count1=count1+1
           #print(count)
           conn10.commit()    
           c10.close()
           conn10.close() 
           if(count1==4):
              print("done1")
              conn2= sqlite3.connect("orchestration.db")
              c2 = conn2.cursor() 
              c2.execute('UPDATE  _count set count=(?)',(0,)) 
              print("updated")
              conn2.commit()    
              c2.close()
              conn2.close()
              continue
           if(count1<4):
             while(count1!=4):
                if(count1==0): 
                       port=8000                    
                       cmnd="sudo docker run -d -p "+str(port)+":80 acts:latest"
                       os.system(cmnd)
                       conn1= sqlite3.connect("orchestration.db")
                       c1 = conn1.cursor()              
                       c1.execute('INSERT INTO container(containerID,port,rr) VALUES(?,?,?)',(1,port,1))
                       conn1.commit()    
                       c1.close()
                       conn1.close()
                       count1=count1+1 
                else:             
                       conn1= sqlite3.connect("orchestration.db")
                       c1 = conn1.cursor() 
                       c1.execute("select *from container") 
                  
                       port=0
                       containerID=0
                       for row in c1.fetchall():
                          containerID=row[0]
                          port=row[1]  
                       port=port+1
                       containerID=containerID+1
                       cmnd="sudo  docker run -d -p "+str(port)+":80 acts:latest"
                       os.system(cmnd)
                       count1=count1+1
                       c1.execute('INSERT INTO container(containerID,port,rr) VALUES(?,?,?)',(containerID,port,0))
                       conn1.commit()    
                       c1.close()
                       conn1.close()
                       conn2= sqlite3.connect("orchestration.db")
                       c2 = conn2.cursor() 
                       c=0
                       c2.execute('UPDATE  _count set count=(?)',(c,)) 
                       conn2.commit()    
                       c2.close()
                       conn2.close()
           if(count1>4):
                while(count1!=4):
                       stopcontainer()
                       count1=count1-1
                if(count1==4):
                      conn3= sqlite3.connect("orchestration.db")
                      c3 = conn3.cursor() 
                      c3.execute("update _count set count=(?)",(0,))
                      conn3.commit()    
                      c3.close()
                      conn3.close()

"""



def stopcontainer():
           conn10 = sqlite3.connect("orchestration.db")
           c10 = conn10.cursor()
           c10.execute("select *from  container")
   	   count1=0
           i=0
           for row in c10.fetchall():                             
                   count1=count1+1
           for row in c10.fetchall():
                   i=i+1
                   if(i==count1):
                        portno=row[1]
                        print(portno)

           conn10.commit()    
           c10.close()
           conn10.close() 





"""





if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")


