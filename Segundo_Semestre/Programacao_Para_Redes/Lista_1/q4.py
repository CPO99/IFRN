import os

def faz_xor(arquivo_velho, senha, arquivo_novo):
    try:
        # Verificar se o arquivo de destino já existe
        if os.path.exists(arquivo_novo):
            print(f"O arquivo de destino '{arquivo_novo}' já existe. Operação cancelada.")
            return

        # Abrir o arquivo de origem para leitura em modo binário
        with open(arquivo_velho, 'rb') as velho:
            dados_velhos = velho.read()

        # Preparar a palavra-passe (converter em lista de valores ASCII)
        senha_num = [ord(letra) for letra in senha]

        # Aplicar o XOR em cada byte
        dados_novos = bytearray()
        tamanho_senha = len(senha_num)

        for i in range(len(dados_velhos)):
            byte = dados_velhos[i]
            chave = senha_num[i % tamanho_senha]  # Repete a senha ciclicamente
            novo_byte = byte ^ chave  # Realizar a operação XOR
            dados_novos.append(novo_byte)

        # Salvar os novos dados no arquivo de destino
        with open(arquivo_novo, 'wb') as novo:
            novo.write(dados_novos)

        print(f"Arquivo '{arquivo_novo}' criado com sucesso.")

    except FileNotFoundError:
        print(f"O arquivo de origem '{arquivo_velho}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Programa principal
def principal():
    # Solicitar as informações ao usuário
    arquivo_velho = input("Digite o nome do arquivo de origem: ")
    senha = input("Digite a palavra-passe: ")
    arquivo_novo = input("Digite o nome do arquivo de destino: ")

    # Invocar a função para processar os arquivos
    faz_xor(arquivo_velho, senha, arquivo_novo)

if __name__ == "__main__":
    principal()
