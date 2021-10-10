import socket

host = "192.168.1.21"
port = 9999

#Crear socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Enlazar
s.bind((host,port))

#acepatar con + nmax
s.listen(10)
print ("Esperando conecciones en el puerto " + str(port))

def aceptar_conexiones():
    conn,addr = s.accept() #[ip,puerto]
    print("cliente " + addr[0])
    comandos(conn)
    conn.close()

def comandos(conn):
    while True:
        cmd = input("Comando> ")

        if str.encode(cmd) == "q" :break

        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            respuesta = str(conn.recv(1024) )
            print(respuesta)

aceptar_conexiones()