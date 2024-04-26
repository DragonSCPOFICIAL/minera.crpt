import hashlib
import concurrent.futures

# Função para calcular o hash de um bloco
def calculate_hash(block, hash_function):
    block_string = str(block['index']) + str(block['previous_hash']) + str(block['timestamp']) + str(block['data']) + str(block['nonce'])
    return hash_function(block_string.encode('utf-8')).hexdigest()

# Função para minerar um bloco
def mine_block(block, difficulty, hash_function):
    block['nonce'] = 0
    while True:
        block_hash = calculate_hash(block, hash_function)
        if int(block_hash, 16) < difficulty:
            return block_hash
        block['nonce'] += 1

# Função para minerar um intervalo de nonces
def mine_block_range(block, difficulty, hash_function, start_nonce, end_nonce):
    for nonce in range(start_nonce, end_nonce):
        block['nonce'] = nonce
        block_hash = calculate_hash(block, hash_function)
        if int(block_hash, 16) < difficulty:
            return block_hash, nonce
    return None, None

# Função para minerar utilizando múltiplos processos
def multiprocess_mine_block(block, difficulty, hash_function, num_processes):
    block_hashes = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as executor:
        future_to_block = {executor.submit(mine_block_range, block.copy(), difficulty, hash_function, i * 10000, (i + 1) * 10000): i for i in range(num_processes)}
        for future in concurrent.futures.as_completed(future_to_block):
            result = future.result()
            block_hashes.append(result)

    for block_hash, nonce in block_hashes:
        if block_hash:
            return block_hash, nonce
    return None, None

