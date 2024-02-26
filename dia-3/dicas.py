import threading, queue

# fila = queue.Queue()

# for tarefa in range(1, 6):
#   fila.put(tarefa)

# print(f'Agora, nossa fila tem tamanho: {fila.qsize()}')
# print(f'A fila está vazia? {fila.empty()}')

# print(f'função fila.get ----        {fila.get()}')
# fila.task_done()

# print(f'Agora, nossa fila tem tamanho: {fila.qsize()}')

# for i in range(fila.qsize()):
#   print(fila.get())


fila_2 = queue.Queue()

def worker():
  while True:
    elemento = fila_2.get()
    print(f'Trabalhando na tarefa {elemento}')
    print(f'Finalizando a tarefa {elemento}')
    fila_2.task_done()

threading.Thread(target=worker, daemon=True).start()

for elemento in range(30):
  fila_2.put(elemento)
print('Todas as requisições foram enviadas!\n', end='')

fila_2.join()
print('Todo o trabalho foi concluído!')