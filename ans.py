import nmap3
import sys
import so_detection
from os import path, remove

def ping_scan(target):	
   nmap = nmap3.NmapHostDiscovery()
   host_info = nmap.nmap_no_portscan(target)
   host_up = host_info.keys()


   if path.exists("Subred '{}'.txt".format(target)):
   		remove("Subred '{}'.txt".format(target))
   else:
   		pass

   if path.exists("IPs_up_'{}'.txt".format(target)):
   		remove("IPs_up_{}.txt".format(target))
   else:
   		pass


   print("MOSTRANDO HOST ACTIVOS\n")
   #Recorriendo llaves del diccionario generado - las llaves con las IP que se encuentran activas
   for i in host_up:
   		#Excluimos la llaves "stats" y "runtime" pues no son ip
   		if i == "stats" or i == "runtime":
   			pass
   		else:

   			salida = open("Subred '{}'.txt".format(target),'a')
   			#Archivo en el que almcenaremos unicamente las ip - para un uso posterior
   			list_ip = open("IPs_up_{}.txt".format(target),'a')
   			print("---"*10)
   			#imprimimos la ip
   			print("Host: {}".format(i))
   			list_ip.write(i+"\n")
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
   			list_ip.close()




def main():
	print("Automatizador de nmap")
	#target = input("Ingrese Rango de ip: ejemplo 192.168.1.*\n")
	#so_detection.so()
	#ping_scan(target)

	ip_list = input("Ingrese nombre de archivo con lista de IPs")
	so_detection.os_list(ip_list)


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt():
		sys.exit()