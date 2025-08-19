import socket

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

ver = True
while ver:
    url = input("Informe a URL completa: ")

    retorno = extrairURL(url)
    if retorno[0] == False:
        print("Informe uma URL válida."\
              "\n\nExemplo: \n - https://google.com\n - https://google.com/caminho \n - https://google.com/caminho/index.html\n\n")
    else:
        print (retorno)
        ver = False