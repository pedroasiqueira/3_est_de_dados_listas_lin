# Imagine que você esteja trabalhando em um e-commerce, e foi lhe dado a demanda de analisar um array de números inteiros que representam os produtos dessa empresa. Verifique quantos produtos formam boas combinações, ou seja, quando um produto é igual ao outro e seu índice é maior que o anterior.


def good_pairs(numbers):
    answer = 0
    i = 0
    size = len(numbers)
    for i in range(size):
        for j in range(i + 1, size):
            if numbers[i] == numbers[j]:
                answer += 1
    return answer


produtos = [1, 3, 1, 1, 2, 3]
resultado = 4
# Os índices (0, 2), (0, 3), (1, 5), (2, 3) formam combinações.


produtos = [1, 1, 2, 3]
resultado = 1
# Os índices (0, 1) formam a única combinação.


# def teste(n):
#     a = 0
#     for algo in range(n):
#         a += 1
#     return a

# def teste2(n, m):
#     a = 0
#     for algo in range(n, m):
#         a += 1
#     return a