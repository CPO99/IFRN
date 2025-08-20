#centralizador de funcoes, seguindo a lógica do professor para uma melhor organização
import socket, ssl, sys, os
from constantes import *

#tratamento da URL
def extrairURL(url:str):
    protocolo = ""
    host = ""
    caminho = ""
    arquivoNome = ""

    try:
        #extraindo host
        if url.find("://") != -1:
            inicioHost = url.find("://") + 3
        else:
            sucesso=False
            return (sucesso, protocolo, host, caminho, arquivoNome)

        fimHost = url.find("/",inicioHost)
        if fimHost == -1:
            fimHost = len(url)
        host = url[inicioHost:fimHost]

        if host.find(".") == -1:
            sucesso=False
            return (sucesso, protocolo, host, caminho, arquivoNome)

        #extraindo caminho
        
        if url.find("/",fimHost) != -1:
            caminho = url[url.find("/",fimHost):]

            if caminho == "/":
                caminho = ""
        else:
            caminho = ""

        #extraindo nome do arquivo
        arquivoNome = url.split('/')[-1]
        if arquivoNome.find(".") == -1 or caminho == "":
            arquivoNome = ""

        #verificando protocolo
        if url.find("https") != -1:
            protocolo = "https"
            sucesso=True
            return (sucesso, protocolo, host, caminho, arquivoNome)
        elif url.find("http") != -1:
            protocolo = "http"
            sucesso=True
            return (sucesso, protocolo, host, caminho, arquivoNome)
        else:
            sucesso=False
            return (sucesso, protocolo, host, caminho, arquivoNome)
    except:
        sucesso=False
        return (sucesso, protocolo, host, caminho, arquivoNome)

def porta(protocolo:str):
    if protocolo == "http":
        return 80
    else:
        return 443
    


    import socket

    try:

        #socket TCP, http padrão
        socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #porta 443 utiliza socket ssl
        if porta == 443:
            context = ssl.create_default_context()
            socket = context.wrap_socket(socket, server_hostname=host)

        socket.connect((host, porta))

        return "Conexão realizada com sucesso!!!"

    except Exception as e:
        sys.exit(f'\nERRO.... {type(e).__name__}\n{str(e)}')
    finally:
        if 'socket' in locals(): 
            socket.close()

def criarDiretorioHost(host: str) -> str:
    dir_host = os.path.join(DIR_APP, host)
    if not os.path.exists(dir_host):
        os.makedirs(dir_host)

    return dir_host

#retorna a resposta recebida em bytes                    
def obterFullResponse(sock: socket):
    data = b''
    while True:
        part = sock.recv(BUFFER_SIZE)
        if not part:
            break
        data += part
    return data

def criarSocketSSL(host: str) -> socket:
    context = ssl.create_default_context()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_sock = context.wrap_socket(sock, server_hostname=host)
    return ssl_sock

def obterStatusCode(headerResposta: str) -> int:
    strStatusLine = headerResposta.split('\r\n')[0]
    intStatusCode = int(strStatusLine.split(' ')[1]) if 'HTTP/' in strStatusLine else 0
    return intStatusCode

def extrairHeaders(headerResposta: str) -> tuple:
    strNovoHost = next((line[9:].strip() for line in headerResposta.split('\r\n') 
                      if line.lower().startswith('location:')), None)
    
    intTamanhoConteudo = int(next((line[15:].strip() for line in headerResposta.split('\r\n') 
                                 if line.lower().startswith('content-length:')), 0))
    
    return (strNovoHost, intTamanhoConteudo)