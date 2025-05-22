import random

import numpy as np


def particao(vetor, inicio, final):
    pivo = vetor[final]
    i = inicio - 1

    for j in range(inicio, final):
        if vetor[j] <= pivo:
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]

    vetor[i+1], vetor[final] = vetor[final], vetor[i+1]
    return i + 1


def quick_sort(vetor, inicio, final):
    if inicio < final:
        posicao = particao(vetor, inicio, final)

        # esquerda
        quick_sort(vetor, inicio, posicao - 1)

        # direita
        quick_sort(vetor, posicao + 1, final)
    return vetor


if __name__ == '__main__':
    vetor = np.array([random.randint(0, 100) for _ in range(10)])
    inicio = 0
    final = len(vetor) - 1

    print(f'Vetor não ordenado:\n{vetor}')
    print(f'Vetor ordenado:\n{quick_sort(vetor, inicio, final)}')
