import random

import numpy as np


def shell_sort(vetor):
    intervalo = len(vetor) // 2

    while intervalo > 0:
        for indice in range(intervalo, len(vetor)):
            temp = vetor[indice]
            j = indice

            while j >= intervalo and vetor[j - intervalo] > temp:
                vetor[j] = vetor[j - intervalo]
                j -= intervalo
            vetor[j] = temp
        intervalo //= 2

    return vetor


if __name__ == '__main__':
    novo_vetor = np.array([random.randint(1, 100) for _ in range(10)])
    print(f'Vetor: {novo_vetor}')
    vetor_ordenado = shell_sort(novo_vetor)
    print(f'Vetor Ordenado: {vetor_ordenado}')
