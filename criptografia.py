import os
from time import sleep
import cryptocode


def print_padrao(mensagem):
    print("*" * 50)
    print(mensagem)
    print("*" * 50)


def input_tratado():    

    input_inicial = input("Digite o número da opção desejada: ")
    try:
        input_inicial = int(input_inicial)
        if input_inicial < 0 or input_inicial > 2:
            input_inicial = -1
            print("*" * 50)
            print("Digite um número válido!")
            print("*" * 50)
    except Exception:
        input_inicial = -1
        print("*" * 50)
        print("Digite um número válido!")
        print("*" * 50)
    return input_inicial


def criptografar(mensagem, chave):
    global contador_mensagens
    print_padrao("Criptografando mensagem...")
    sleep(3)
    mensagem_criptografada = cryptocode.encrypt(mensagem, chave)
    print_padrao("Mensagem criptografada!")

    with open(
        f"mensagens/destinatario/criptografada/{contador_mensagens}.txt",
        "w",
        encoding="UTF-8",
    ) as file:
        file.write(mensagem_criptografada)

    with open(
        f"mensagens/remetente/original/{contador_mensagens}.txt",
        "w",
        encoding="UTF-8",
    ) as file:
        file.write(mensagem)

    contador_mensagens += 1
    sleep(3)


def descriptografar(mensagem, chave):
    mensagem_descriptografada = cryptocode.decrypt(mensagem, chave)
    if mensagem_descriptografada is False:
        print_padrao("Senha incorreta!")
    else:
        print_padrao("Descriptografando...")
        sleep(3)
        print_padrao("Mensagem descriptografada!")
        sleep(1)
        print(f"MENSAGEM: {mensagem_descriptografada}")
        sleep(3)

os.makedirs("mensagens/remetente/original", exist_ok=True)
os.makedirs("mensagens/destinatario/criptografada", exist_ok=True)

contador_mensagens = 0

for i in range(100):
    try:
        with open(f"mensagens/remetente/original/{i}.txt", "r") as file:
            contador_mensagens = i + 1
    except Exception:
        pass


while True:
    print("-" * 50)
    print("0 - SAIR")
    print("1 - Criptografar")
    print("2 - Descriptografar")

    opcao_escolhida = input_tratado()

    if opcao_escolhida == 0:
        break
    if opcao_escolhida == 1:
        mensagem = input("Digite sua mensagem: ")
        chave = input("Digite sua chave (senha) para criptografia: ")
        criptografar(mensagem, chave)
    elif opcao_escolhida == 2:
        mensagem = input("Digite a mensagem criptografada: ")
        chave = input("Digite a chave (senha) para descriptografia: ")
        descriptografar(mensagem, chave)
