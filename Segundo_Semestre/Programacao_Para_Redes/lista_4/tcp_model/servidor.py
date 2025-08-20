import socket
from constantes import *

# Criando o socket TCP (AF_INET -> IPv4 / SOCK_STREAM -> TCP)
sockTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ligando o socket à porta
sockTCP.bind(('', HOST_PORT))
sockTCP.listen(1)  # pode aceitar 1 conexão na fila

print('\nServidor TCP aguardando conexão...\n')

# Aceitando conexão de um cliente
conn, addr = sockTCP.accept()
print(f"Conectado a: {addr}")

while True:
    # Recebendo dados do cliente
    byteMensagem = conn.recv(BUFFER_SIZE)
    if not byteMensagem:  # se não veio nada, o cliente fechou
        break

    msg = byteMensagem.decode(CODE_PAGE)
    print(f'{addr}: {msg}')

    # Enviando mensagem de retorno (ECHO)
    strECHO = f'DEVOLVENDO: {msg}'
    conn.send(strECHO.encode(CODE_PAGE))

    # Enviando mensagem de finalização
    if msg.upper() == "SAIR":  
        conn.send("EXIT_BYE".encode(CODE_PAGE))
        break

# Fechando a conexão e o socket
conn.close()
sockTCP.close()

print('\nAVISO: Servidor finalizado...\n')
