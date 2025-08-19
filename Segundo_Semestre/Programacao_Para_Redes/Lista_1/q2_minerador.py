import hashlib
import time

def bytes_to_bits(byte_data):
    """Converte bytes para string de bits"""
    return ''.join(f'{byte:08b}' for byte in byte_data)

def findNonce(dataToHash, bitsToBeZero):
    """Procura o nonce que gera hash começando com N bits zero"""
    nonce = 0
    start_time = time.time()

    while True:
        # Concatena o nonce em 4 bytes + os dados
        nonce_bytes = nonce.to_bytes(4, byteorder='big')
        combined = nonce_bytes + dataToHash

        # Calcula o SHA256
        hash_result = hashlib.sha256(combined).digest()

        # Converte o hash para bits
        hash_bits = bytes_to_bits(hash_result)

        # Verifica se os primeiros bits são zeros
        if hash_bits.startswith('0' * bitsToBeZero):
            break

        nonce += 1

    end_time = time.time()
    elapsed_time = end_time - start_time
    return nonce, elapsed_time
