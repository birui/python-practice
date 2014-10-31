import multiprocessing
import sys,os,time
import getServerList
cmd = sys.argv[1]
result = []
def runCmd(h,port,user,passwd,command):
    
     cmd = "python single_runCmd.py %s %s %s %s %s" %(h,port,user,passwd,command)
     print cmd
     os.system(cmd)
p = multiprocessing.Pool(processes=25)

#for i in range(1000):
#     result.append(p.apply_async(run,('alex', 'hey')))
server_dic = getServerList.server_dic
#print server_dic
for host,values in server_dic.items():
     ssh_port = values[0]
     username = values[1]
     password = values[2]
     result.append(p.apply_async(runCmd,(host,ssh_port,username,password,cmd)))

#print p.apply_async(run,('hey Jude!',))
#print p.apply_async(run,('hey Alex',)).get()
p.close()
#p.join()

for res in result:
     res.get(timeout=5)