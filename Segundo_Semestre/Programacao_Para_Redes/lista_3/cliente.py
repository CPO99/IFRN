import socket, sys, os
from constantes import *
from funcoes import *

while True:
    url = input("Informe a URL completa: ")

    sucesso, protocolo, host, caminho, arquivoNome = extrairURL(url)
    
    if sucesso == False:
        print("Informe uma URL válida."\
            "\n\nExemplo: \n - https://google.com\n - https://google.com/caminho \n - https://google.com/caminho/index.html\n\n")
    else:
        conectar(host, porta(protocolo))

        break