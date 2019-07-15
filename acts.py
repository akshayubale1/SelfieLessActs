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

global status
status=1

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}),404)





@app.route('/api/v1/categories',methods=['GET'])
def list_all_category():
    
    global status
    if(status==0):
        return make_response(jsonify({}),500)
    conn10 = sqlite3.connect("acts.db")
    c10 = conn10.cursor()
    c10.execute("select * from  _count")
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

    
    conn = sqlite3.connect("acts.db")
    c = conn.cursor()
    c.execute("SELECT * FROM categories")    
    #data = c.fetchall()
    #print(data)
    #row = c.fetchall()
    catlist=dict()    
    for row in c.fetchall():                         
            catlist[row[1]] = row[2]
    
    #catlist={}
    if(catlist=={}):
         return make_response(jsonify("categories"),204)

    conn.commit()    
    c.close()
    conn.close()    
    return  Response(json.dumps(catlist), mimetype='application/json')
        



@app.route('/api/v1/categories',methods=['POST'])
def add_category():
   global status
   if(status==0):
        return make_response(jsonify({}),500)
   conn10 = sqlite3.connect("acts.db")
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
   conn = sqlite3.connect("acts.db")
   c = conn.cursor()       
   data = request.json
   #print(row1)
   c.execute("SELECT * FROM categories ")
   flag=0
   for row in c.fetchall():       
        if(row[1]==data[0]):
             flag=1
        if(flag==1):
            return make_response(jsonify(),400)
   if(flag==0):          
             c.execute('INSERT INTO categories(categoryName) values(?)',(data[0],))   
             conn.commit()    
             c.close()
             conn.close()
             return jsonify(), 201 






@app.route('/api/v1/categories/<string:catname>',methods=['DELETE'])
def delete_category(catname):
    global status
    if(status==0):
        return make_response(jsonify({}),500)
    conn10 = sqlite3.connect("acts.db")
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
    conn = sqlite3.connect("acts.db")
    c = conn.cursor()       
    c.execute("SELECT * FROM categories ")
    flag=0
    for row in c.fetchall():
         if(row[1]==catname):
              flag=1
         if(flag==1):
            c.execute('DELETE FROM categories WHERE categoryName=(?)',(catname,))
            conn.commit()    
            c.close()
            conn.close()
            return jsonify({}),200
    if(flag==0):
           return make_response(jsonify({'error':'Resource does not exist'}),400)
    

"""


@app.route('/api/v1/categories/<string:catname>/acts',methods=['GET'])
def list_particular_category_acts(catname):
    conn10 = sqlite3.connect("acts.db")
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
    conn = sqlite3.connect("acts.db")
    conn1 = sqlite3.connect("acts.db")
    c = conn.cursor()
    d = conn1.cursor()
    c.execute("SELECT * FROM categories")
    
    ##row=c.fetchall()
    ##print(row)
    ##print(catname)
    actlist=dict()
    tasks=list()
    flag1=0
    flag=0
    for row in c.fetchall():        
         if(row[1]==catname):
              flag1=1
              if(row[2]<100):
                    d.execute('SELECT * FROM acts where catid=(?)',(row[0],))        
                    for row1 in d.fetchall():
                      task={
                             "id":row1[0],
                             "catid":row1[1],
                             "timestamp":row1[2],
                             "upvotes":row1[3],
                             "caption":row1[4],
                             "username":row1[5],
                           }
                      tasks.append(task)
                      ##jsonify({'task':task})
                      
                                  
                    conn.commit()    
                    c.close()
                    conn.close()
                    conn1.commit()    
                    d.close()
                    conn1.close()
                    return  Response(json.dumps(tasks), mimetype='application/json')
    if(flag1==0):
         return make_response(jsonify({}),400)
    if(flag==0):
         return make_response(jsonify({}),204)         
              
         
"""




@app.route('/api/v1/categories/<string:catname>/acts/size',methods=['GET'])
def no_of_acts(catname):
    global status
    if(status==0):
        return make_response(jsonify({}),500)
    
    conn10 = sqlite3.connect("acts.db")
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
    
    conn = sqlite3.connect("acts.db")
    c = conn.cursor()
    print("akshay")
    c.execute("SELECT * FROM categories ")
    #print(c.fetchall())
    actsize=list()
    flag=0
    try:        
        if(c.fetchall()):
          print("gh")          
    except:
        return make_response(jsonify({}),204)
    #print(catname)
    c.execute("SELECT * FROM categories ")
    for row in c.fetchall():
        print(row[1])
        if(row[1]==catname):
              flag=1
        if(flag==1):
              actsize.append(row[2])            
              conn.commit()    
              c.close()
              conn.close()
              return  Response(json.dumps(actsize), mimetype='application/json')
    #print(flag)
    if(flag==0):
          return make_response(jsonify({}),400)
         
         
##no of acts and no of acts with arguements both are included

@app.route('/api/v1/categories/<string:cat1name>/acts',methods=['GET'])
def no_of_acts_in_a_range(cat1name):
  
  if(request.args.get('start')==None):
       global status
       if(status==0):
          return make_response(jsonify({}),500)
       conn10 = sqlite3.connect("acts.db")
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

      
       conn = sqlite3.connect("acts.db")
       conn1 = sqlite3.connect("acts.db")
       c = conn.cursor()
       d = conn1.cursor()
       c.execute("SELECT * FROM categories")
    
       ##row=c.fetchall()
       ##print(row)
       ##print(catname)
       actlist=dict()
       tasks=list()
       flag1=0
       flag=0
       for row3 in c.fetchall():
         #print(row3[1]);
         if(row3[1]==cat1name):
             if(row3[2]!=0):
               flag1=1
              
       if(flag1==0):          
            return Response("{}" ,status=204,mimetype='applications/json')

       flag2=0
       flag=0
       c.execute("SELECT * FROM categories")
       for row in c.fetchall():        
         if(row[1]==cat1name):
              flag2=1
              if(row[2]<100):
                    flag=1
                    d.execute('SELECT * FROM acts where catid=(?)',(row[0],))        
                    for row4 in d.fetchall():
                      print(row4)
                      task={
                             "actId":row4[0],
                             "catid":row4[1],
                             "timestamp":row4[2],
                             "upvotes":row4[3],
                             "caption":row4[4],
                             "username":row4[5],
                             "imgB64":row4[6]
                           }
                      tasks.append(task)
                      ##jsonify({'task':task})
                      
                                  
                    conn.commit()    
                    c.close()
                    conn.close()
                    conn1.commit()    
                    d.close()
                    conn1.close()
                    #print("as");
                    return  Response(json.dumps(tasks), mimetype='application/json')
       if(flag2==0):
           return make_response(jsonify({}),400)
       if(flag==0):
           return make_response(jsonify({}),413)

       
  else:
    global status
    if(status==0):
        return make_response(jsonify({}),500)
    conn10 = sqlite3.connect("acts.db")
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


    
    conn = sqlite3.connect("acts.db")
    conn1 = sqlite3.connect("acts.db")
    c = conn.cursor()
    d = conn1.cursor()
    startrange=int(request.args.get('start'))
    endrange=int(request.args.get('end'))
    #endrange=int(endrange)
    #startrange=int(startrange)
    c.execute("SELECT * FROM categories")
    tasks=list()
    rangeof=endrange-startrange+1
    flag=0
    for row in c.fetchall():
         #print(row)
         if(row[1]==cat1name):
              flag=1
              x=row[0]
              break
    print(row[1])
    if(flag==0):
         return make_response(jsonify("category"),204) 
    if(startrange<=0):
         return make_response(jsonify("<0"),400)
    if(startrange>endrange):
         return make_response(jsonify("s>e"),400)
    
    if(endrange>row[2]):
         return make_response(jsonify("e>row"),400)
    if(rangeof>100):
         return make_response(jsonify(),413)
    
                 
    
    else:
               if(startrange>=1 & endrange<=row[2]):
                          d.execute('SELECT * FROM acts where catid=(?)',(x,))
                          #print("akshay")
                          row1=d.fetchall()
                          print(row1)                         
                          row1.sort(key=lambda x:x[2][12])
                          row1.sort(key=lambda x:x[2][11])
                          row1.sort(key=lambda x:x[2][15])
                          row1.sort(key=lambda x:x[2][14])
                          row1.sort(key=lambda x:x[2][18])
                          row1.sort(key=lambda x:x[2][17])
                          row1.sort(key=lambda x:x[2][0])
                          row1.sort(key=lambda x:x[2][1])
                          row1.sort(key=lambda x:x[2][3])
                          row1.sort(key=lambda x:x[2][4])
                          row1.sort(key=lambda x:x[2][3])
                          row1.sort(key=lambda x:x[2][9])
                          row1.sort(key=lambda x:x[2][8])
                          row1.sort(key=lambda x:x[2][7])
                          row1.sort(key=lambda x:x[2][6])
                          row1.reverse()
                          print(len(row1))
                          print(row1)
                                                  
                          for i in range(startrange-1,endrange):                              
                              task1={
                                     "id":row1[i][0],
                                     "catid":row1[i][1],
                                     "timestamp":row1[i][2],
                                     "upvotes":row1[i][3],
                                     "caption":row1[i][4],
                                     "username":row1[i][5],
                                     "imgB64":row1[i][6]
                                    }
                              tasks.append(task1)
                          conn.commit()    
                          c.close()
                          conn.close()
                          conn1.commit()    
                          d.close()
                          conn1.close()
                          return  Response(json.dumps(tasks), mimetype='application/json')
               
    
          

@app.route('/api/v1/acts/upvote',methods=['POST'])
def upvote_an_act():
      global status
      if(status==0):
        return make_response(jsonify({}),500)
      conn10 = sqlite3.connect("acts.db")
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
      conn = sqlite3.connect("acts.db")
      c = conn.cursor()
      data = request.json     
      #print(row1)      
      c.execute("SELECT * FROM acts");
      actIdlist=list()
      flag=0
      for row in c.fetchall():
           #print(y)
           #print(row[0])
           if(row[0]==data[0]):                
                flag=1
                x=int(row[3])
                x=x+1
                print(x)
                c.execute('UPDATE acts set upvotes=(?) where actId=(?)',(x,data[0]))
                conn.commit()    
                c.close()
                conn.close()    
                return make_response(jsonify({}),200)
      if(flag==0):
           return make_response(jsonify(),400)
                
      
      


@app.route('/api/v1/acts/<int:actId>',methods=['DELETE'])
def remove_an_act(actId):
      global status
      if(status==0):
        return make_response(jsonify({}),500)
      conn10 = sqlite3.connect("acts.db")
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
      
      conn = sqlite3.connect("acts.db")
      c = conn.cursor()   
      c.execute("SELECT *  FROM acts")
      flag=0
      for row in c.fetchall():
           if(row[0]==actId):
                flag=1                
                c.execute('Select *From acts where actId=(?)',(actId,))
                #print(c.fetchall())
                flag1=0
                for row2 in c.fetchall():
                     #print(row2)
                     flag1=row2[1]
                c.execute('Select *From categories')
                #print(flag1)
                for row10 in c.fetchall():
                     print(row10)
                     if(row10[0]==flag1):
                        l=row10[2]
                        l=l-1
                        c.execute('UPDATE categories set number_of_acts=(?) where categoryName=(?)',(l,row10[1]))
                c.execute('Delete  FROM acts where actId=(?)',(actId,))
                conn.commit()    
                c.close()
                conn.close()                
                return make_response(jsonify(), 200)
      if(flag==0):
               return make_response(jsonify(),400)
      

@app.route('/api/v1/acts',methods=['POST'])
def upload_an_act():
      global status
      if(status==0):
        return make_response(jsonify({}),500)
      conn10 = sqlite3.connect("acts.db")
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
      conn = sqlite3.connect("acts.db")
      conn1 = sqlite3.connect("acts.db")
      conn2 = sqlite3.connect("acts.db")
      conn3 = sqlite3.connect("acts.db")
      c = conn.cursor()
      d = conn1.cursor()
      e=conn2.cursor()
      f=conn3.cursor()
      data=dict()
      #data["categoryName"]=None
      data=request.json
      flag1=0
      try:
           if(data["upvotes"]):
                flag1=1
      except:
           pass

      if(flag1==1):
           return make_response(jsonify("upvotes"),400)      
      flag=0
      try:
           if(data["username"]):
                flag=1
      except:
           pass
      if(flag==0):
           return make_response(jsonify("username"),400)

      """
      try:
           resp=requests.get('http://100.24.79.8:8080/api/v1/users')
      except:
           return make_response(jsonify("wrong"),400)
      if resp.status_code==204:
           return make_response(jsonify("wrong1"),400)
      users=resp.json()
      if username in users:
           pass
      else:
           return make_response(jsonify("username"),400)
      
      """

      
      """
      base64=data["imgB64"]
      #print(type(base64))
      pattern = re.compile('^@(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$')
      match = re.match(pattern,base64)
      l=0
      try:
          if(match.group(0)==base64):
            l=1
                   
      except:
          pass
      if(l==0):
           return make_response(jsonify(" base64 required"),400)
      
      """
      


      base64= isBase64(data["imgB64"])    
      if(base64):
           print("")
      else:
           return make_response(jsonify(" base64 "),400)

      
      row=(data["actId"],data["username"],data["timestamp"],data["caption"],data["imgB64"])
      
      e.execute("SELECT *from acts")
      #print(e.fetchall())
      
      for row1 in e.fetchall():          
          if(int(data["actId"])==row1[0]):
                return make_response(jsonify("actId"),400)
      
      try:         
          if(data["categoryName"]):
               print(" ")                        
      except :         
          return make_response(jsonify("categoryName2"),400)
      f.execute("SELECT *FROM categories")
      #print("ino")
      flag5=0
      #print(data["categoryName"])
      #print(f.fetchall())
      for row4 in f.fetchall():
          #print("ubale")
          if(data["categoryName"]==row4[1]):      
                row2=(data["categoryName"])
                flag5=1
                      
      
      if(flag5==0):
           return make_response(jsonify("categoryName1"),400)
     
           
      try:
           datetime.datetime.strptime(data["timestamp"],'%d-%m-%Y:%S-%M-%H')
      except ValueError:
           return make_response(jsonify("timestamp"),400)

      
      #print(row1)
      c.execute('SELECT * FROM categories where categoryName=(?)',(row2,))
      x=0
      row=list(row)
      for row2 in c.fetchall():
          row.append(row2[0])
          row.append(x)
      
      #print(row2[0])
           
      #print(row)
      #d.execute('INSERT INTO acts(catid,upvotes) VALUES(?,?)',(row1,x))
      d.execute('INSERT INTO acts(actId,username,timestamp,caption,imgB64,catid,upvotes) VALUES(?,?,?,?,?,?,?)',(row[0],row[1],row[2],row[3],row[4],row[5],row[6],))
      c.execute('SELECT * FROM categories')
      for row10 in c.fetchall():
          if(row10[1]==data["categoryName"]):
              l=row10[2]
              l+=1
              d.execute('UPDATE categories set number_of_acts=(?) where categoryName=(?)',(l,row10[1]))
      conn.commit()    
      c.close()
      conn.close()
      conn1.commit()    
      d.close()
      conn1.close()
      conn2.commit()    
      e.close()
      conn2.close()
      conn3.commit()    
      f.close()
      conn3.close()
      return jsonify({}), 201 









def isBase64(sb):
        try:
                if type(sb) == str:
                        # If there's any unicode here, an exception will be thrown and the function will return false
                        sb_bytes = bytes(sb, 'ascii')
                elif type(sb) == bytes:
                        sb_bytes = sb
                else:
                        raise ValueError("Argument must be string or bytes")
                return base64.b64encode(base64.b64decode(sb_bytes)) == sb_bytes
        except Exception:
                return False




@app.route('/api/v1/acts',methods=['GET'])
def count_acts():
      global status
      if(status==0):
        return make_response(jsonify({}),500)
      conn10 = sqlite3.connect("acts.db")
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
      conn = sqlite3.connect("acts.db")
      c = conn.cursor()
      c.execute("select * from acts")
      count=0;
      for row in c.fetchall():
            count=count+1
      count1=list()
      count1.append(count)
      return  Response(json.dumps(count1), mimetype='application/json')                       

 




@app.route('/api/v1/_count',methods=['GET'])
def count_requests():
    global status
    if(status==0):
        return make_response(jsonify({}),500)
    conn10 = sqlite3.connect("acts.db")
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
    global status
    if(status==0):
        return make_response(jsonify({}),500)
    conn10 = sqlite3.connect("acts.db")
    c10 = conn10.cursor()
    count=0
    c10.execute('UPDATE _count set count=(?) ',(count,))
    conn10.commit()    
    c10.close()
    conn10.close()
    l1=dict()
    return  Response(json.dumps(l1), mimetype='application/json')


@app.route('/api/v1/_health',methods=['get'])
def check_health():
    global status
    if(status==0):
         return make_response(jsonify({}),500)
    else:
         return make_response(jsonify({}),200)






@app.route('/api/v1/_crash',methods=['post'])
def crashserver():
   global status
   status=0
   return make_response(jsonify({}),200)




if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=80)






'''
{
"actId": 123,
"username": "ubale",
"timestamp": " 77834",
"caption": "caption56text",
"categoryName": "school",
"imgB64":"TWFuIGlzIGR3Rpbmd1aXNoZWQsIG5vdCBvb"
}

'''



   
    
"""                  
@app.route('/api/v1/parcategory',methods=['GET'])
def list_all_particular_category():
    conn = sqlite3.connect("acts.db")
    c = conn.cursor()       
    data = request.json
    print("akshay")
    row = (data['id'])
    c.execute("SELECT * FROM categories where id=(?)",(row,))
    catlist=list()
    for row in c.fetchall():
          catlist.append(row)
    conn.commit()    
    c.close()
    conn.close()
    return str(catlist) 
"""   






