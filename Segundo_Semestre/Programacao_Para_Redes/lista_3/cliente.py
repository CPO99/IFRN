import socket, sys, os
from constantes import *
from funcoes import *

ver = True
while ver:
    url = input("Informe a URL completa: ")

    boolSucesso, strProtocolo, strHost, strCaminho, strArquivoNome = extrairURL(url)
    dir_host = criarDiretorioHost(strHost)

    print(f"Host:{strHost}")
    print(f"Caminho do arquivo:{strCaminho}")
    print(f"Nome do arquivo:{strArquivoNome}")
    
    if boolSucesso:
        try:
            # Cria socket HTTP
            sockTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sockTCP.connect((strHost, PORT_HTTP))

            # Envia requisição HEAD
            sockTCP.sendall(REQ_HEAD_TEMPLATE.format(strHost).encode(CODE_PAGE))

            # Lê header (não fecha o socket ainda)
            header_bytes = ler_header(sockTCP)
            strRespHeader = header_bytes.decode(CODE_PAGE, errors='replace')

            # Obtém status e possíveis redirecionamentos
            intStatusCode = obterStatusCode(strRespHeader)
            strNewHost, _ = extrairHeaders(strRespHeader)

            ###############################
            # Redirecionamento 3xx (HTTP -> HTTPS)
            if 300 <= intStatusCode < 400 and strNewHost:
                new_host = strNewHost.split('//')[-1].split('/')[0]

                sockTCP = criarSocketSSL(new_host)
                sockTCP.connect((new_host, PORT_HTTPS))

                sockTCP.sendall(REQ_GET_TEMPLATE.format(strCaminho, new_host).encode(CODE_PAGE))

                # Lê header e corpo corretamente
                header_bytes = ler_header(sockTCP)
                body_bytes = ler_corpo_http(sockTCP, header_bytes)
                sockTCP.close()

                print(f'\nRedirecionado para: {new_host}')
                print(f'Tamanho do conteúdo: {len(body_bytes)} bytes')

                # Salvar arquivo
                if strArquivoNome.endswith((".html", ".txt")) or strArquivoNome == "":
                    nome_arquivo = strArquivoNome if strArquivoNome else "index.html"
                    with open(os.path.join(strHost, nome_arquivo), 'w', encoding=CODE_PAGE) as f:
                        f.write(body_bytes.decode(CODE_PAGE, errors='replace'))
                else:
                    with open(os.path.join(strHost, strArquivoNome), 'wb') as f:
                        f.write(body_bytes)

            else:
                # HTTP GET normal sem redirecionamento
                sockTCP.sendall(REQ_GET_TEMPLATE.format(strCaminho, strHost).encode(CODE_PAGE))

                header_bytes = ler_header(sockTCP)
                body_bytes = ler_corpo_http(sockTCP, header_bytes)
                sockTCP.close()

                print(f'\nSocket conectado na porta {PORT_HTTP}')
                print(f'Tamanho do conteúdo: {len(body_bytes)} bytes')

                if strArquivoNome.endswith((".html", ".txt")) or strArquivoNome == "":
                    nome_arquivo = strArquivoNome if strArquivoNome else "index.html"
                    with open(os.path.join(strHost, nome_arquivo), 'w', encoding=CODE_PAGE) as f:
                        f.write(body_bytes.decode(CODE_PAGE, errors='replace'))
                else:
                    with open(os.path.join(strHost, strArquivoNome), 'wb') as f:
                        f.write(body_bytes)

        except Exception as e:
            sys.exit(f'\nERRO.... {type(e).__name__}\n{str(e)}')
        finally:
            if 'sockTCP' in locals(): 
                sockTCP.close()
    else:
        print("\n\nInforme uma URL válida."\
              "\n\nExemplo:\n - https://google.com\n - https://google.com/caminho\n - https://google.com/caminho/index.html\n")