import socket
from constantes import *

# Criando o socket TCP (AF_INET -> IPV4 / SOCK_STREAM -> TCP)
sockTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectando ao servidor
sockTCP.connect((HOST_IP_SERVER, HOST_PORT))

print('\n\nPara sair digite EXIT...\n\n')

while True:
    try:
        # Informando a mensagem a ser enviada para o servidor
        strMensagem = input('Digite a mensagem: ')

        # Saindo do Cliente quando digitar EXIT
        if strMensagem.lower().strip() == 'exit':
            break

        # Enviando a mensagem ao servidor
        sockTCP.send(strMensagem.encode(CODE_PAGE))

        # Recebendo ECHO do servidor
        byteRetorno = sockTCP.recv(BUFFER_SIZE)
        if not byteRetorno:  # servidor fechou a conexão
            print("Servidor encerrou a conexão.")
            break

        print(f'ECHO RECEBIDO: {byteRetorno.decode(CODE_PAGE)}')

        # Verificando se o servidor pediu encerramento
        if byteRetorno.decode(CODE_PAGE) == "EXIT_BYE":
            print("Encerrando aplicação por ordem do servidor...")
            break

    except Exception as e:
        print("\nOcorreu um erro inesperado:", e)
        break

# Fechando o socket
sockTCP.close()
