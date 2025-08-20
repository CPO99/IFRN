import socket, sys, os
from constantes import *
from funcoes import *

ver = True
while ver:
    #solicitando a URL completa para requisição
    url = input("Informe a URL completa: ")

    #URL tratada
    boolSucesso, strProtocolo, strHost, strCaminho, strArquivoNome = extrairURL(url)

    dir_host = criarDiretorioHost(strHost)
    
    if boolSucesso == True:
        try:
            #criando conexão http/TCP
            sockTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)            
            sockTCP.connect((strHost, PORT_HTTP))

            #obtendo o header
            sockTCP.sendall(REQ_HEAD_TEMPLATE.format(strHost).encode(CODE_PAGE))
            strRespHeader = obterFullResponse(sockTCP)
            print(strRespHeader)
            sockTCP.close()

            # Obtém informações do cabeçalho
            intStatusCode = obterStatusCode(strRespHeader)
            strNewHost, _ = extrairHeaders(strRespHeader)
            
            ###############################
            if 300 <= intStatusCode < 400 and strNewHost:
                new_host = strNewHost.split('//')[-1].split('/')[0]
            
                # Cria novo socket SSL
                sockTCP = criarSocketSSL(new_host)
                sockTCP.connect((new_host, PORT_HTTPS))
            
                # Envia requisição GET para obter conteúdo completo
                sockTCP.sendall(REQ_GET_TEMPLATE.format(new_host).encode(CODE_PAGE))
                full_response = obterFullResponse(sockTCP)
            
                # Separa headers do conteúdo
                if '\r\n\r\n' in full_response:
                    strRespHeaders, strContent = full_response.split('\r\n\r\n', 1)
                else:
                    strRespHeaders, strContent = full_response, ''
            
                # Exibe informações
                print(f'\nRedirecionado para............: {new_host}')
                print(f'Socket conectado..............: Porta {PORT_HTTPS}')
                print(f'Tamanho do conteúdo...........: {len(strContent)} bytes')
            
                # Salva o conteúdo
                with open(os.path.join(dir_host, f'conteudo_porta_{PORT_HTTPS}.txt'), 'w', encoding=CODE_PAGE) as f:
                    f.write(strContent)
            else:
                # Se não houve redirecionamento, faz GET na porta 80
                sockTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sockTCP.connect((strHost, PORT_HTTP))
                sockTCP.sendall(REQ_GET_TEMPLATE.format(strHost).encode(CODE_PAGE))
                full_response = obterFullResponse(sockTCP)
            
                if '\r\n\r\n' in full_response:
                    strRespHeaders, strContent = full_response.split('\r\n\r\n', 1)
                else:
                    strRespHeaders, strContent = full_response, ''

                print(f'\nSocket conectado..............: Porta {PORT_HTTP}')
                print(f'Tamanho do conteúdo..........: {len(strContent)} bytes')

                print(strContent)
                print(dir_host)
                print(PORT_HTTP)
                print(CODE_PAGE)

                with open(os.path.join(dir_host, f'conteudo_porta_{PORT_HTTP}.txt'), 'w', encoding=CODE_PAGE) as f:
                    f.write(strContent)
                    except Exception as e:
            sys.exit(f'\nERRO.... {type(e).__name__}\n{str(e)}')
        finally:
            if 'sockTCP' in locals(): 
                sockTCP.close()
    else:
        print("Informe uma URL válida."\
            "\n\nExemplo: \n - https://google.com\n - https://google.com/caminho \n - https://google.com/caminho/index.html\n\n")
    