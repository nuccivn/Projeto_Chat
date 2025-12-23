import os

def limpar_tela():
    # Verifica o sistema operacional e limpa a tela de acordo
    os.system('cls' if os.name == 'nt' else 'clear')

def rodar_chat():
    mensagens = []
    nome = input("Digite seu nome para entrar no sistema de chat: ")

    while True:
        limpar_tela()

        # Exibe as mensagens existentes
        for m in mensagens:
            print(f"{m['nome']}: {m['texto']}")

        print("-" * 34)

        texto = input("Digite a mensagem (ou 'sair'): ")
        
        if texto.lower() == "sair":
            print("Saindo do chat...")
            break

        # Adiciona a nova mensagem à lista
        mensagens.append({
            'nome': nome,
            'texto': texto
        })

if __name__ == "__main__":
    rodar_chat()