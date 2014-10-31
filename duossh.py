#!/usr/bin/env python
import multiprocessing 
import sys,os,time
import getServerList
cmd = sys.argv[1]
result = []

def runCmd(h,port,user,passwd,command):
	cmd = "python single_runCmd.py %s %s %s %s %s" %(h,port,user,passwd,command)
	print cmd
	os.system(cmd)
p = multiprocessing.Pool(processes=250)
	

server_dic = getServerList.server_dic

for  host,values in server_dic.items():
	ssh_port = values[0]
	username = values[1]
	password = values[2]
	result.append(p.apply_async(runCmd,(host,ssh_port,username,password.cmd)))
p.close()
	
for res in result:
	res.get(timeout=5)
	
