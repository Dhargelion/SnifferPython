from scapy.all import *
class spoofing:
	def __init__(self, ip_origen, ip_destino):
		self.ip_origen = ip_origen
		self.ip_destino = ip_destino

def crear(origin, destiny,pro):
	res = IP(src=origin, dst= destiny)/pro()
	return res
	#packete = spoofing(ip_or, ip_des)
   # packete = IP(src=ip_or, dst=ip_des)/TCP()
def mostrar(aux):
	print("IP de origen: ", aux.src)
	print("IP destino: ", aux.dst)

def enviar():
	print("funciona2")

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
		protocolo = input("Seleccione el protocolo: ")
		pro = prot(protocolo)
		aux = crear(ip_or, ip_des, pro)
		#print(aux.src)
		
	elif opcion == 2:
		mostrar(aux)
		#print(aux.src)
		#print(aux.dst)
		flag = False
	elif opcion == 3:
		enviar()
		flag =False
	else : nada()






#ip_or = input("Ingrese IP origen")
#ip_des = input("Ingrese IP destino")
#packet = spoofing(ip_or,ip_des)
#print(packet.ip_origen)
#print(packet.ip_destino)