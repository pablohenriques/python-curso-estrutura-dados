# big O(n), 11 passos
import timeit


def soma_simples(n_termos):
    soma = 0
    for i in range(n_termos + 1):
        soma += i
    return soma


# Big O(3), apenas 3 passos
def soma_equacao(n_termos):
    return (n_termos * (n_termos + 1)) / 2


if __name__ == '__main__':
    pass
