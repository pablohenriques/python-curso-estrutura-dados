import numpy as np


def bubble_sort(vetor):
    length = len(vetor)

    for i in range(length):
        for j in range(0, length-i-1):
            if vetor[j] > vetor[j+1]:
                temp = vetor[j]
                vetor[j] = vetor[j+1]
                vetor[j+1] = temp
    return vetor


if __name__ == '__main__':
    vetor_nao_ordenado = np.array([15, 34, 8, 3])
    vetor_ordenado = bubble_sort(vetor_nao_ordenado)
    print(f'Vetor não ordenado: {vetor_nao_ordenado}')
    print(f'Vetor ordenado: {vetor_ordenado}')
