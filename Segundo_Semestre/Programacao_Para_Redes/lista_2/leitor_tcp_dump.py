import struct
from collections import defaultdict
from datetime import datetime

# abre o arquivo .dump (formato pcap)
arquivo = open("cap1.dump", "rb")

# lê os 24 primeiros bytes (cabeçalho geral)
cabecalho = arquivo.read(24)

# lê pacotes um por um
hora_inicio = None
hora_fim = None
maior_tcp = 0
qtd_incompletos = 0
udp_tamanhos = []
trafego = defaultdict(int)
ip_base = None
ips_conectados = set()

while True:
    # cada pacote tem um cabeçalho de 16 bytes
    dados_cabecalho = arquivo.read(16)
    if not dados_cabecalho or len(dados_cabecalho) < 16:
        break

    ts_sec, ts_usec, tamanho_salvo, tamanho_real = struct.unpack("IIII", dados_cabecalho)
    tempo = ts_sec + ts_usec / 1000000

    if hora_inicio is None:
        hora_inicio = tempo
    hora_fim = tempo

    # lê os dados do pacote
    dados_pacote = arquivo.read(tamanho_salvo)
    if len(dados_pacote) < 34:  # mínimo para ethernet + IP
        continue

    # pula o cabeçalho ethernet (14 bytes)
    inicio_ip = 14
    versao_ihl = dados_pacote[inicio_ip]
    versao = versao_ihl >> 4
    ihl = versao_ihl & 0xF
    tamanho_cabecalho_ip = ihl * 4

    if len(dados_pacote) < inicio_ip + tamanho_cabecalho_ip:
        continue

    ip_info = struct.unpack("!BBHHHBBH4s4s", dados_pacote[inicio_ip:inicio_ip+20])
    tos = ip_info[1]
    total_length = ip_info[2]
    protocolo = ip_info[6]
    src_ip = ".".join(map(str, ip_info[8]))
    dst_ip = ".".join(map(str, ip_info[9]))

    print("\n--- Novo Pacote IP ---")
    print(f"Versão: {versao}")
    print(f"Tamanho do cabeçalho IP: {tamanho_cabecalho_ip} bytes")
    print(f"Tamanho total: {total_length}")
    print(f"Protocolo: {protocolo}")
    print(f"De: {src_ip}")
    print(f"Para: {dst_ip}")

    if protocolo == 6:  # TCP
        if total_length > maior_tcp:
            maior_tcp = total_length

    if protocolo == 17:  # UDP
        udp_tamanhos.append(total_length)

    if tamanho_salvo < tamanho_real:
        qtd_incompletos += 1

    par = tuple(sorted([src_ip, dst_ip]))
    trafego[par] += total_length

    if not ip_base:
        ip_base = src_ip

    if src_ip == ip_base:
        ips_conectados.add(dst_ip)
    elif dst_ip == ip_base:
        ips_conectados.add(src_ip)

# fim da leitura
arquivo.close()

# mostrando os resultados finais
print("\n========== RESULTADOS ==========")
print(f"Início da captura: {datetime.fromtimestamp(hora_inicio)}")
print(f"Fim da captura: {datetime.fromtimestamp(hora_fim)}")
print(f"Maior pacote TCP: {maior_tcp} bytes")
print(f"Pacotes cortados (incompletos): {qtd_incompletos}")

if udp_tamanhos:
    media = sum(udp_tamanhos) / len(udp_tamanhos)
    print(f"Média dos tamanhos UDP: {media:.2f} bytes")
else:
    print("Nenhum pacote UDP encontrado.")

if trafego:
    mais_trafego = max(trafego.items(), key=lambda x: x[1])
    print(f"Par de IP com mais tráfego: {mais_trafego[0]} com {mais_trafego[1]} bytes")
else:
    print("Não foi possível calcular o tráfego.")

print(f"O IP da interface ({ip_base}) falou com {len(ips_conectados)} IPs diferentes.")
