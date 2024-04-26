import time
import mining
import hashlib

# Link para o módulo mining: https://github.com/DragonSCPOFICIAL/minera.crpt/blob/main/mining.py

# Menu principal
def menu():
    while True:
        print("\nMenu Principal:")
        print("1. Iniciar Mineração")
        print("2. Iniciar Mineração Mil Vezes")
        print("3. Sair")
        escolha = input("Digite sua escolha (1-3): ")
        if escolha == '1':
            iniciar_mineracao()
        elif escolha == '2':
            iniciar_mineracao_mil_vezes()
        elif escolha == '3':
            print("Encerrando programa.")
            break
        else:
            print("Escolha inválida. Por favor, escolha novamente.")

# Iniciar mineração
def iniciar_mineracao():
    print("Preparando para minerar...")
    time.sleep(1)  # Tempo de carregamento simulado de 1 segundo

    blocks = [{'index': 1, 'previous_hash': '0', 'timestamp': int(time.time()), 'data': 'Dados de exemplo', 'nonce': 0}]
    difficulty = 1000000
    hash_function = hashlib.sha256
    num_processes = 10

    print("Mineração em andamento...")
    for block in blocks:
        block_hash, nonce = mining.multiprocess_mine_block(block, difficulty, hash_function, num_processes)
        if block_hash:
            block['nonce'] = nonce
            print(f"Bloco {block['index']} minerado com hash: {block_hash} e nonce: {nonce}")
        else:
            print("Falha ao minerar o bloco.")

# Iniciar mineração mil vezes
def iniciar_mineracao_mil_vezes():
    print("Iniciando mineração mil vezes...")
    time.sleep(1)  # Tempo de carregamento simulado de 1 segundo
    for _ in range(1000):
        iniciar_mineracao()

# Executar o menu
if __name__ == "__main__":
    menu()

