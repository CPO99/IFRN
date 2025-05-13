import json

def checa_ip(ip):
    partes = ip.split('.')
    if len(partes) != 4:
        return False
    for parte in partes:
        if not 0 <= int(parte) <= 255:
            return False
    return True

def checa_mascara(mascara):
    try:
        mascara = int(mascara)
        return 0 <= mascara <= 32
    except ValueError:
        return False

def ip_pra_bin(ip):
    return ''.join([bin(int(x))[2:].zfill(8) for x in ip.split('.')])

def bin_pra_ip(binario):
    return '.'.join([str(int(binario[i:i+8], 2)) for i in range(0, 32, 8)])

def rede(ip_bin, mascara_bin):
    return ''.join(['1' if ip_bin[i] == mascara_bin[i] else '0' for i in range(32)])

def broadcast(ip_bin, mascara_bin):
    return ''.join([ip_bin[i] if mascara_bin[i] == '1' else '1' for i in range(32)])

def primeiro_host(rede_bin):
    rede_int = int(rede_bin, 2)
    primeiro = rede_int + 1
    return bin_pra_ip(bin(primeiro)[2:].zfill(32))

def ultimo_host(broadcast_bin):
    broadcast_int = int(broadcast_bin, 2)
    ultimo = broadcast_int - 1
    return bin_pra_ip(bin(ultimo)[2:].zfill(32))

def quantos_hosts(mascara):
    return (2 ** (32 - mascara)) - 2

def mascara_pra_dec(mascara_bin):
    return bin_pra_ip(mascara_bin)

def formata_bin(binario):
    return '.'.join([binario[i:i+8] for i in range(0, len(binario), 8)])

def calcula_subrede():
    ip = input("Digite o endereço IP (formato: x.x.x.x): ")
    while not checa_ip(ip):
        print("Endereço IP inválido. Tente novamente.")
        ip = input("Digite o endereço IP (formato: x.x.x.x): ")

    masc_inicial = input("Digite a máscara de rede inicial (0 a 32): ")
    while not checa_mascara(masc_inicial):
        print("Máscara de rede inválida. Tente novamente.")
        masc_inicial = input("Digite a máscara de rede inicial (0 a 32): ")

    masc_final = input("Digite a máscara de rede final (0 a 32): ")
    while not checa_mascara(masc_final) or int(masc_final) < int(masc_inicial):
        print("Máscara de rede inválida ou inferior à máscara inicial. Tente novamente.")
        masc_final = input("Digite a máscara de rede final (0 a 32): ")

    ip_bin = ip_pra_bin(ip)
    resultados = {}

    for masc in range(int(masc_inicial), int(masc_final) + 1):
        masc_bin_completa = '1' * masc + '0' * (32 - masc)
        masc_bin_formatada = formata_bin(masc_bin_completa)
        rede_bin = rede(ip_bin, masc_bin_completa)
        broadcast_bin = broadcast(ip_bin, masc_bin_completa)
        masc_dec = mascara_pra_dec(masc_bin_completa)
        primeiro = primeiro_host(rede_bin)
        ultimo = ultimo_host(broadcast_bin)
        total_hosts = quantos_hosts(masc)

        resultados[masc] = {
            "Rede": bin_pra_ip(rede_bin),
            "Primeiro Host": primeiro,
            "Último Host": ultimo,
            "Broadcast": bin_pra_ip(broadcast_bin),
            "Máscara Decimal": masc_dec,
            "Máscara Binária": masc_bin_formatada,
            "Número de Hosts": total_hosts
        }

    print("\nResultados:")
    for masc, dados in resultados.items():
        print(f"\nMáscara /{masc}")
        for chave, valor in dados.items():
            print(f"{chave}: {valor}")

    try:
        with open('subrede_results.json', 'r') as arquivo:
            dados_existentes = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        dados_existentes = {}

    dados_existentes.update(resultados)

    with open('subrede_results.json', 'w') as arquivo:
        json.dump(dados_existentes, arquivo, indent=4)

    print("\nResultados salvos em 'subrede_results.json'.")

if __name__ == "__main__":
    calcula_subrede()