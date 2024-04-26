import time
import mining
import hashlib
import random
import json

# Link para o módulo mining: https://github.com/DragonSCPOFICIAL/minera.crpt/blob/main/mining.py
# Link para o módulo de endereços de carteira: https://github.com/DragonSCPOFICIAL/minera.crpt/blob/main/wallet_addresses_for_mined_tokens.json

# Lista de Criptomoedas
cryptocurrencies = [
    "Bitcoin", "Ethereum", "BNB Beacon Chain", "BNB Smart Chain", "Cardano",
    "XRP", "Solana", "Dogecoin", "Polkadot", "Avalanche C-Chain", "Tron",
    "Polygon", "Litecoin", "Cronos Chain", "Crypto.org", "NEAR", "TON",
    "Bitcoin Cash", "Stellar", "Cosmos Hub", "Algorand", "Ethereum Classic",
    "Aptos", "MultiversX", "VeChain", "Filecoin", "Tezos", "KuCoin Community Chain",
    "Zcash", "Mantle", "Theta", "Huobi ECO Chain", "Fantom", "Arbitrum",
    "Gnosis Chain", "Sui", "Native Injective", "THORChain", "Zilliqa",
    "Conflux eSpace", "Waves", "Klaytn", "Dash", "Celo", "Harmony", "Decred",
    "Kava", "KavaEvm", "Hedera", "Nervos Network", "Elrond", "Stacks", "OKX Chain",
    "Hathor Network"
]

# Carregar os endereços das carteiras
with open('wallet_addresses_for_mined_tokens.json') as file:
    wallet_addresses = json.load(file)

# Registro das criptomoedas mineradas
mined_cryptocurrencies = []

# Menu principal
def menu():
    while True:
        print("\nMenu Principal:")
        print("1. Iniciar Mineração")
        print("2. Iniciar Mineração Mil Vezes")
        print("3. Enviar Bitcoins para a Conta do Banco")
        print("4. Mostrar Criptomoedas Encontradas")
        print("5. Sair")
        escolha = input("Digite sua escolha (1-5): ")
        if escolha == '1':
            iniciar_mineracao()
        elif escolha == '2':
            iniciar_mineracao_mil_vezes()
        elif escolha == '3':
            enviar_bitcoins()
        elif escolha == '4':
            mostrar_criptomoedas_encontradas()
        elif escolha == '5':
            print("Encerrando programa.")
            break
        else:
            print("Escolha inválida. Por favor, escolha novamente.")

# Iniciar mineração
def iniciar_mineracao():
    crypto = random.choice(cryptocurrencies)
    print(f"Preparando para minerar {crypto}...")
    time.sleep(1)  # Simulação de tempo de carregamento

    blocks = [{'index': 1, 'previous_hash': '0', 'timestamp': int(time.time()), 'data': f'Dados de exemplo para {crypto}', 'nonce': 0}]
    difficulty = 1000000
    hash_function = hashlib.sha256
    num_processes = 10

    print(f"Mineração de {crypto} em andamento...")
    for block in blocks:
        block_hash, nonce = mining.multiprocess_mine_block(block, difficulty, hash_function, num_processes)
        if block_hash:
            block['nonce'] = nonce
            print(f"Bloco {block['index']} minerado com sucesso para {crypto} com hash: {block_hash} e nonce: {nonce}")
            mined_cryptocurrencies.append(crypto)
        else:
            print(f"Falha ao minerar o bloco para {crypto}.")

# Iniciar mineração mil vezes
def iniciar_mineracao_mil_vezes():
    print("Iniciando mineração mil vezes...")
    for _ in range(1000):
        iniciar_mineracao()

# Simulação de envio de Bitcoins para a conta bancária
def enviar_bitcoins():
    if "Bitcoin" in wallet_addresses:
        print(f"Enviando Bitcoins para a conta bancária do endereço: {wallet_addresses['Bitcoin']}")
    else:
        print("Endereço de Bitcoin não encontrado. Por favor, verifique se há Bitcoins disponíveis para envio.")

# Mostrar as criptomoedas encontradas
def mostrar_criptomoedas_encontradas():
    if mined_cryptocurrencies:
        print("Criptomoedas encontradas:")
        for crypto in set(mined_cryptocurrencies):
            count = mined_cryptocurrencies.count(crypto)
            print(f"{crypto}: {count} vezes")
    else:
        print("Nenhuma criptomoeda foi encontrada até o momento.")

# Executar o menu
if __name__ == "__main__":
    menu()

