import nmap3
import sys
from os import path

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

def os_list(ip_list):
	nmap = nmap3.Nmap()
	if path.exists(ip_list):
		ips = open(ip_list,'r')
		ips_r = ips.read().split('\n')
		for ip in ips_r:
			print("---"*10)
			print("Sistema operativo para la ip: {}".format(ip))
			try:
				os = nmap.nmap_os_detection(ip)
				dic_os = os[ip]
				name_os = dic_os['osmatch']

				for i in name_os:
					name_os = i['name']
					print(name_os)
			except (TypeError, KeyError):
				print("IP: {} NO ENCONTRADA".format(ip))
				pass
		ips.close()
	else:
		print("Seleccione un archivo con el listado de IPs")