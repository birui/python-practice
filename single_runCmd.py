#!/usr/bin/env python
#encoding:utf8
import paramiko
import sys,os

host = sys.argv[1]
port = sys.argv[2]
user = sys.argv[3]
password = sys.argv[4]

msg = "-----------Result:%s----------" % host

cmd = sys.argv[5]

s = paramiko.SSHClient()     #绑定实例
s.load_system_host_keys()     #加载本机HOST主机文件
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())


try:
     s.connect(host,port,user,password,timeout=5)  #连接远程主机
     stdin,stdout,stderr = s.exec_command(cmd)          #执行命令

     cmd_result = stdout.read(),stderr.read()          #读取命令结果
     print msg

     for line in cmd_result:
             print line,

     s.close()
except paramiko.AuthenticationException:
     print msg
     print 'AuthenticationException Failed'
except paramiko.BadHostKeyException:
     print msg
     print "Bad host key"     