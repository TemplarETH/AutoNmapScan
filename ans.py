import nmap3
import sys



def main():
	print("Automatizador de nmap")
	nmap = nmap3.Nmap()
	so = nmap.nmap_os_detection("192.168.20.32")
	#print (so)
	dic_so = so['192.168.20.32']
	#print(dic_so)
	name_so = dic_so['osmatch']
	if name_so == []:
		print("No se encontro información")
	else:
		print(name_so)	
		#name_so = name_so[0]
		for i in name_so:
			name_so = i['name']
			print(name_so)


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt():
		sys.exit()