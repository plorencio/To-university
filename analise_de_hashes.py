import hashlib
import os

aarquivo = input("Caminho do arquivo: ")

def calculohash(arquivo):
    ohash = hashlib.sha256()
    with open(arquivo, 'rb') as x:
        dados = x.read()
        ohash.update(dados)
    return ohash.hexdigest()

resultado = calculohash(aarquivo)

hash_original = input("Hash original: ")

if resultado == hash_original:
    print("-"*33)
    msg = "O arquivo está intacto."
    print("{:^33}".format(msg))
    print("-" * 33)
else:
    print("-" * 33)
    msg2 = "O arquivo foi corrompído!"
    print("{:^33}".format(msg2))
    print("-" * 33)