import sys
"""Perceba que temos uma coleção de valores
e operações que atuam sobre estes valores,
de acordo com o que foi definido pelo TAD."""


class ListaArray:
    def __init__(self):
        self.data = []

    def __len__(self):
        # quando pedido o tamanho do array
        # retorne o tamanho de data
        return len(self.data)

    def __str__(self):
        # converte para string e exibe os valores de data
        return str(self.data)

    def get(self, index):
        # recupera o elemento no índice informado
        return self.data[index]

    def set(self, index, value):
        # insere um elemento no índice informado
        self.data.insert(index, value)

    def remove(self, index):
        # removeremos o item, retornando-o
        return self.data.pop(index)
    
    def update(self, index, value):
        self.data[index] = value
        
# Eu fiz desse jeito:
    # def update(self, index, value):
    #     self.data.pop(index)
    #     self.data.insert(index, value)


# vamos inicializar e preencher uma estrutura de dados array
array = ListaArray()
# sys.getsizeof retorna o tamanho da lista em bytes
array_memory_size = sys.getsizeof(array.data)
print(f'Tamanho em bytes sem nada: {array_memory_size}') #  56


array.set(0, "Marcos")
array.set(1, "Patrícia")
# quando começamos as inserções o valor muda
array_memory_size = sys.getsizeof(array.data)
print(f'Tamanho em bytes com 2 elem: {array_memory_size}')


array.set(2, "Matheus")
array.set(3, "Giovana")
# como um espaço adicional é reservado o valor não é modificado
array_memory_size = sys.getsizeof(array.data)
print(f'Tamanho em bytes com 4 elem: {array_memory_size}')


array.set(4, "Alberto")
array.set(5, "Marta")
array.set(6, "Túlio")
array.set(7, "Michelle")
array_memory_size = sys.getsizeof(array.data)
print(f'Tamanho em bytes com 8 elem: {array_memory_size}')

print(array)

array.set(0, "Valeria")
array.set(1, "Miguel")
print(array)

array.remove(0)
print(array)

array.update(1, 'pedro')
print(array)