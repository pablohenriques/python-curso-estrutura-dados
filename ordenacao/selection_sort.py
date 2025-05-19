import random


def selection_sort(vetor):
    length = len(vetor)

    for indice in range(length):
        indice_minimo = indice

        for j in range(indice+1, length):
            if vetor[indice_minimo] > vetor[j]:
                indice_minimo = j

        temp = vetor[indice]
        vetor[indice] = vetor[indice_minimo]
        vetor[indice_minimo] = temp

    return vetor


if __name__ == '__main__':
    vetor_nao_ordenado = [random.randint(1, 100) for x in range(10)]
    print(f'Vetor não ordenado: {vetor_nao_ordenado}')

    vetor_ordenado = selection_sort(vetor_nao_ordenado)
    print(f'Vetor ordenado: {vetor_ordenado}')
