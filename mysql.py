# import os
# os.system('python -V')

import MySQLdb
try:
        conn=MySQLdb.connect(host='localhost',user='root',passwd='',port=3306) 
        cur=conn.cursor()  
        cur.execute('create database if not exists python2')
        conn.select_db('python2') 
        cur.execute('create table test(id int,info varchar(20))')

        value=[1,'hirollen']
        cur.execute('insert into test values(%s,%s)',value) 

        values=[]
        for i in range(20):
                values.append((i,'hi rollen'+str(i)))
        cur.executemany('insert into test values(%s,%s)',values) 

        cur.execute('update test set info="i am rollen"where id=3')

        conn.commit()  
        cur.close()      
        conn.close()  

except MySQLdb.Error,e:
        print "Mysql Error %d:%s"%(e.args[0],e.args[1])