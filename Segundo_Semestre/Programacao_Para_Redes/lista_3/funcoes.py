#centralizador de funcoes, seguindo a lógica do professor para uma melhor organização
import socket, ssl, sys, os
from constantes import *

#tratamento da URL
def extrairURL(url: str):
    protocolo = ""
    host = ""
    caminho = "/"
    arquivoNome = ""

    try:
        # Verifica protocolo
        if url.startswith("https://"):
            protocolo = "https"
            inicioHost = 8
        elif url.startswith("http://"):
            protocolo = "http"
            inicioHost = 7
        else:
            return False, protocolo, host, caminho, arquivoNome

        # Extrai host
        fimHost = url.find("/", inicioHost)
        if fimHost == -1:
            fimHost = len(url)
        host = url[inicioHost:fimHost]

        if "." not in host:
            return False, protocolo, host, caminho, arquivoNome

        # Extrai caminho
        if fimHost < len(url):
            caminho = url[fimHost:]
        else:
            caminho = "/"

        # Extrai nome do arquivo (última parte do caminho)
        arquivoNome = caminho.split('/')[-1]
        if not "." in arquivoNome:
            arquivoNome = ""

        return True, protocolo, host, caminho, arquivoNome

    except Exception:
        return False, protocolo, host, caminho, arquivoNome


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

def ler_header(sock: socket) -> bytes:
    header = b''
    while b'\r\n\r\n' not in header:
        part = sock.recv(1)
        if not part:
            break
        header += part
    return header

def ler_corpo_http(sock: socket, headers: bytes) -> bytes:
    body = b''
    headers_str = headers.decode(CODE_PAGE, errors='replace').lower()

    # Content-Length
    content_length = 0
    for line in headers_str.split("\r\n"):
        if line.startswith("content-length:"):
            content_length = int(line.split(":")[1].strip())
            break

    # Chunked
    is_chunked = "transfer-encoding: chunked" in headers_str

    if content_length > 0:
        bytes_lidos = 0
        while bytes_lidos < content_length:
            chunk = sock.recv(min(BUFFER_SIZE, content_length - bytes_lidos))
            if not chunk:
                break
            body += chunk
            bytes_lidos += len(chunk)

    elif is_chunked:
        while True:
            # Lê linha do tamanho do chunk
            chunk_size_line = b''
            while not chunk_size_line.endswith(b'\r\n'):
                c = sock.recv(1)
                if not c:
                    break
                chunk_size_line += c

            chunk_size = int(chunk_size_line.strip(), 16)
            if chunk_size == 0:
                break

            # Lê o chunk
            chunk_data = b''
            while len(chunk_data) < chunk_size:
                chunk_data += sock.recv(chunk_size - len(chunk_data))
            body += chunk_data

            # Lê o \r\n após o chunk
            sock.recv(2)
    else:
        # Sem Content-Length nem chunked: lê até fechar
        while True:
            chunk = sock.recv(BUFFER_SIZE)
            if not chunk:
                break
            body += chunk

    return body
