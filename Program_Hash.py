import hashlib
import os

msg = "Bem-vindo ao programa de criptografia!"
print('-'*100)
print('{:^100}'.format(msg))
print('-'*100)
print(" "*30)
print("Aqui, você pode criptografar qualquer mensagem que desejar e transformá-la em Hash! Vamos começar?")

def gerar_hash_arquivo(caminho_arquivo, algoritmo):
    try:
        hash_obj = hashlib.new(algoritmo)
        with open(caminho_arquivo, 'rb') as arquivo:
            while True:
                bloco = arquivo.read(8192)
                if not bloco:
                    break
                hash_obj.update(bloco)
    except FileNotFoundError:
        print("Arquivo não encontrado!")
        return None
    except Exception as e:
        print(f"Erro: {e}")
        return None
    return hash_obj.hexdigest()


def main():
    caminho_arquivo = input("Digite o caminho do arquivo .txt: ")

    if not os.path.isfile(caminho_arquivo):
        print("Arquivo não encontrado. Verifique o caminho.")
        return

    algoritmos = hashlib.algorithms_available
    print("Algoritmos de hash disponíveis:")
    for algo in algoritmos:
        print(f"- {algo}")

    tentativas = 3
    while tentativas > 0:
        algoritmo = input(f"Digite o algoritmo de hash desejado: ").lower()

        if algoritmo in algoritmos:
            hash_hex = gerar_hash_arquivo(caminho_arquivo, algoritmo)
            if hash_hex:
                print("Seu código está logo abaixo.")
                print('-'*100)
                print('{:^100}'.format(hash_hex))
                print('-'*100)
                print("Obrigado por usar o programa!")
            return
        else:
            tentativas -= 1
            print(f"Algoritmo '{algoritmo}' não é válido. Tente novamente.")

    print("Número máximo de tentativas atingido. Programa encerrado.")


if __name__ == "__main__":
    main()
