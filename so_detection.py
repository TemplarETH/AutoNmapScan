import nmap3

def so():
	nmap = nmap3.Nmap()
	so = nmap.nmap_os_detection("192.168.20.30")
	#print (so)
	dic_so = so['192.168.20.30']
	#print(dic_so)
	name_so = dic_so['osmatch']
	for i in name_so:
		name_so = i['name']
		print(name_so)