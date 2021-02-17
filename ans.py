import nmap3
import sys
import so_detection
from os import path, remove

def ping_scan():	
   nmap = nmap3.NmapHostDiscovery()
   host_info = nmap.nmap_no_portscan("192.168.20.*")
   host_up = host_info.keys()
   if path.exists("Subred '{}'.txt".format("192.168.20.*")):
   		remove("Subred '{}'.txt".format("192.168.20.*"))
   else:
   		pass
   		
   print("MOSTRANDO HOST ACTIVOS\n")
   #Recorriendo llaves del diccionario generado - las llaves con las IP que se encuentran activas
   for i in host_up:
   		#Excluimos la llaves "stats" y "runtime" pues no son ip
   		if i == "stats" or i == "runtime":
   			pass
   		else:

   			salida = open("Subred '{}'.txt".format("192.168.20.*"),'a')
   			print("---"*10)
   			#imprimimos la ip
   			print("Host: {}".format(i))
   			salida.write("IP: "+i+"\n")
   			#Asignamod el diccionario que contiene la llave IP
   			datos_host = host_info[i]
   			#Dentro del diccionario buscamos la llave "macaddress" que contiene otro diccionario
   			macaddress = datos_host["macaddress"]
   			#Puede que en el escaneo no se obtenga datos de "macaddress", por lo que validamos que sea un diccionario para porder recorrerlo
   			if type(macaddress) == dict:
   				#Recorremos las llaves del diccionario "macaddress"
   				for a in macaddress.keys():
   					if "addr" == a:
   						#Validamos la llave y asignamos su valor
   						direccion = macaddress["addr"]
   						print("MAC: {}".format(direccion))
   						salida.write("MAC: "+direccion+"\n")
   					else:
   						pass

   					if "vendor" == a:
   						#Validamos la llave y asignamos su valor
   						tarjeta = macaddress["vendor"]
   						print("Tarjeta: {}\n".format(tarjeta))
   						salida.write("Tarjeta: "+tarjeta+"\n")
   					else:
   						pass
   			else:
   				print("NO SE ENCONTRARON DATOS\n")
   				salida.write("NO SE ENCONTRARON DATOS\n")
   			salida.close()


def main():
	print("Automatizador de nmap")
	#so_detection.so()
	ping_scan()


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt():
		sys.exit()