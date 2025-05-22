import random

import numpy as np


def insertion_sort(vetor):
    n = len(vetor)

    for indice in range(1, n):
        marcado = vetor[indice]

        j = indice - 1
        while j>= 0 and marcado < vetor[j]:
            vetor[j+1] = vetor[j]
            j -= 1
        vetor[j+1] = marcado

    return vetor


if __name__ == '__main__':
    new_vetor = np.array([random.randint(1, 100) for _ in range(10)])
    print(f'Novo vetor: {new_vetor}')
    resultado = insertion_sort(new_vetor)
    print(f'Vetor ordenado: {resultado}')
