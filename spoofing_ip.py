from scapy.all import *
class spoofing:
	def __init__(self, ip_origen, ip_destino):
		self.ip_origen = ip_origen
		self.ip_destino = ip_destino

def crear(origin, destiny,protocolo):
	if protocolo == 1:
		res = IP(src=origin, dst= destiny)/TCP()
		
		print("packete TCP creado ")
	elif protocolo == 2:
		res = IP(src=origin, dst= destiny)/ICMP()
		print("packete ICMP creado ")
	elif protocolo == 3:
		res = IP(src=origin, dst= destiny)/UDP()
		print("packete UDP creado ")
	else : print("opcion invalida")
	
	return res
	#packete = spoofing(ip_or, ip_des)
   # packete = IP(src=ip_or, dst=ip_des)/TCP()
def mostrar(aux):
	print("IP de origen: ", aux.src)
	print("IP destino: ", aux.dst)

def enviar(packete):
	#el loop es el bucle, inter es la frecuencia de encvio en segundos
	#send(packet, loop =1 , inter= 0.1)
	payload = "CONNECT"
	aux = packete/payload
	send(aux)
	print("Paquete enviado")
	

def nada():
	print("Opcion invalida")

def showProtocol():
	print("""1.- TCP
			2.- ICMP
			3.- UDP""")

def prot(opcion):
	if opcion == 1:
		return "TCP"
	elif opcion == 2:
		return "ICMP"
	elif opcion == 3:
		return "UDP"

menu = """
    1.-Crear paquete IP
    2.-Ver datos del paquete creado
    3.-Enviar paquete"""
flag = True
while flag == True:
	print(menu)
	opcion = int(input("Ingrese la opcion >> "))
	if opcion == 1:
		ip_or = input("Ingrese IP origen >> ")
		ip_des = input("Ingrese IP destino >>")
		showProtocol()
		protocolo = int(input("Seleccione el protocolo: "))
		#pro = prot(protocolo)
		aux = crear(ip_or, ip_des, protocolo)
		#print(aux.src)
		
	elif opcion == 2:
		mostrar(aux)
	elif opcion == 3:
		enviar(aux)
	else : nada()






#ip_or = input("Ingrese IP origen")
#ip_des = input("Ingrese IP destino")
#packet = spoofing(ip_or,ip_des)
#print(packet.ip_origen)
#print(packet.ip_destino)