server_list_file = 'server_list.txt'

def get_server_dic():
     server_dic = {}
     f = file(server_list_file)
     for line in f.readlines():
          if len(line.strip()) ==0:break
          server_dic[line.split()[0]] = line.split()[1:]
     f.close()
     return server_dic
server_dic =  get_server_dic()
print server_dic