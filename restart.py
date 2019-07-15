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
def adding_container_details(containerID,port):
          conn10 = sqlite3.connect("orchestration.db")
          c10 = conn10.cursor()
          c10.execute("insert into container values(?,?,?)",(containerID,port,"Active"))
	  conn10.commit()
          c10.close()
          conn10.close()


def remove_container_details(containerID):
          conn10 = sqlite3.connect("orchestration.db")
          c10 = conn10.cursor()
          print(containerID)
          print(type(containerID))
          c10.execute("delete from container where containerID=(?)",(containerID))
	  conn10.commit()
          c10.close()
          conn10.close()
"""
def getcontainerID(port):          
          #result1=[]
          result = commands.getoutput("docker ps -a")
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
                      print("inside")
                      containerID=row.split()[0]
                      return containerID
                      
               
                   
def restartcontainer(port):
               #print("1")
               port=str(port)
               containerID=getcontainerID(port)
               containerID=str(containerID)
               #remove_container_details(containerID)
               #print(type(containerID))
               #print("2")
               #print(containerID)
               cmnd= "docker stop "+containerID
               os.system(cmnd)
               cmnd="docker rm "+containerID
               os.system(cmnd)
               cmnd="docker run -d -p "+port+":80 acts:latest"
               os.system(cmnd)

               """
               conn10 = sqlite3.connect("orchestration.db")
               c10 = conn10.cursor()
               c10.execute("select *from container")
               for row in c10.fetchall():
                         containerID=row[0]
               c10.execute("INSERT INTO container(containerID,port,rr) values(?,?,?)",(containerId,port

               """




               #containerID=getcontainerID(port)
               #containerID=str(containerID)
               #adding_container_details(containerID,port)
               #print("success")
               





while(1):
	    time.sleep(1)
	    conn10 = sqlite3.connect("orchestration.db")
	    c10 = conn10.cursor()
	    c10.execute("select * from  container")
	    for row in c10.fetchall():                             
		          portno=row[1]
		          request='http://localhost:'+str(portno)+'/api/v1/_health'
		          resp=requests.get(request)
                          resp=str(resp).split("[") 
                          count=0
                          for i  in resp:
                               count=count+1  
                               if(count==2):  
                                    i=i[0:3]

                          i=int(i)                                                    
                          if(i==500):                                
                              restartcontainer(portno)
                                
                                         
		          		          
	    #print(count)
	    conn10.commit()    
	    c10.close()
	    conn10.close()      
     












if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")















    





