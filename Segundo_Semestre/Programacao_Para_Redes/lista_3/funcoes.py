#centralizador de funcoes, seguindo a lógica do professor para uma melhor organização
import socket, ssl, sys

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
    
def conectar(host:str, porta:int):
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