import random

import numpy as np


def merge_sort(vetor):

    if len(vetor) > 1:
        divisao = len(vetor) // 2
        esquerda = vetor[:divisao].copy()
        direita = vetor[divisao:].copy()

        merge_sort(esquerda)
        merge_sort(direita)

        i = 0
        j = 0
        k = 0

        # ordenada esquerda e direita
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                vetor[k] = esquerda[i]
                i += 1
            else:
                vetor[k] = direita[j]
                j += 1
            k += 1

        # ordenacao final
        while i < len(esquerda):
            vetor[k] = esquerda[i]
            i += 1
            k += 1
        while j < len(direita):
            vetor[k] = direita[j]
            j += 1
            k += 1

    return vetor


if __name__ == '__main__':
    vetor = np.array([random.randint(1, 10000) for _ in range(10000)])
    print(f'Vetor não ordenado: {vetor}')
    vetor_ordenado = merge_sort(vetor)
    print(f'Vetor ordenado: {vetor_ordenado}')
