import numpy as np

def inteiros_pra_binario(numeros):
    binarios = [np.binary_repr(numero) for numero in numeros]
    return binarios

numeros = [32, 101, 57, 77]
binarios = inteiros_pra_binario(numeros)
for numero, binario in zip(numeros, binarios):
    print(f'O número {numero} em binário é: {binario}')