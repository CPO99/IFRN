import socket, sys, os
from constantes import *
from funcoes import *

ver = True
while ver:
    # Solicita a URL completa
    url = input("Informe a URL completa: ")

    # Extrai partes da URL
    boolSucesso, strProtocolo, strHost, strCaminho, strArquivoNome = extrairURL(url)

    dir_host = criarDiretorioHost(strHost)
    
    if boolSucesso:
        try:
            # Cria socket HTTP
            sockTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sockTCP.connect((strHost, PORT_HTTP))

            # Envia requisição HEAD para obter cabeçalho
            sockTCP.sendall(REQ_HEAD_TEMPLATE.format(strHost).encode(CODE_PAGE))
            full_response = obterFullResponse(sockTCP)
            sockTCP.close()

            # Separa header e body (aqui body é vazio, só interesse nos headers)
            header_bytes, _, _ = full_response.partition(b'\r\n\r\n')
            strRespHeader = header_bytes.decode(CODE_PAGE, errors='replace')

            # Obtém código de status e possíveis redirecionamentos
            intStatusCode = obterStatusCode(strRespHeader)
            strNewHost, _ = extrairHeaders(strRespHeader)

            ###############################
            # Redirecionamento 3xx (ex: HTTP -> HTTPS)
            if 300 <= intStatusCode < 400 and strNewHost:
                new_host = strNewHost.split('//')[-1].split('/')[0]

                # Cria socket SSL para HTTPS
                sockTCP = criarSocketSSL(new_host)
                sockTCP.connect((new_host, PORT_HTTPS))

                # Envia requisição GET
                sockTCP.sendall(REQ_GET_TEMPLATE.format(strCaminho, new_host).encode(CODE_PAGE))
                full_response = obterFullResponse(sockTCP)

                # Separando header e corpo
                header_bytes, _, body_bytes = full_response.partition(b'\r\n\r\n')

                print(f'\nRedirecionado para: {new_host}')
                print(f'Tamanho do conteúdo: {len(body_bytes)} bytes')

                # Salvar arquivo
                if strArquivoNome.endswith((".html", ".txt")) or strArquivoNome == "":
                    nome_arquivo = strArquivoNome if strArquivoNome else "arquivo.html"
                    with open(os.path.join(strHost, nome_arquivo), 'w', encoding=CODE_PAGE) as f:
                        f.write(body_bytes.decode(CODE_PAGE, errors='replace'))
                else:
                    with open(os.path.join(strHost, strArquivoNome), 'wb') as f:
                        f.write(body_bytes)

            else:
                # Sem redirecionamento: HTTP GET normal
                sockTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sockTCP.connect((strHost, PORT_HTTP))
                sockTCP.sendall(REQ_GET_TEMPLATE.format(strCaminho, strHost).encode(CODE_PAGE))
                full_response = obterFullResponse(sockTCP)

                header_bytes, _, body_bytes = full_response.partition(b'\r\n\r\n')

                print(f'\nSocket conectado na porta {PORT_HTTP}')
                print(f'Tamanho do conteúdo: {len(body_bytes)} bytes')

                # Salvar arquivo
                if strArquivoNome.endswith((".html", ".txt")) or strArquivoNome == "":
                    nome_arquivo = strArquivoNome if strArquivoNome else "arquivo.html"
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
