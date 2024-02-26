def contains_duplicate(nums):
  nums.sort()
  for index in range(len(nums)-1):
    if nums[index] == nums[index + 1]:
      return True
  return False

test1 = [1, 2, 3, 1]
test2 = []
test3 = [1, 2, 3, 4]
test4 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

# Dado um array de doces candies e um valor inteiro extra_candies, onde candies representa o número de doces das crianças.
# Verifique se há uma maneira de distribuir doces extras entre as crianças de forma que ela possa ter o maior número de doces entre elas.
# Várias criaças podem ter o maior número de doces entre elas

candies = [2, 3, 5, 1, 3]
extra_candies = 3
# Resposta correta: [True, True, True, False, True]

def kid_with_candies(candies, extra_candies):
  max_candies = max(candies)
  return [candy + extra_candies >= max_candies for candy in candies]

# print(kid_with_candies(candies, extra_candies))


# Dado um array de números inteiros que representam uma avaliação a respeito de um ponto turístico. E seus índices representam a distância entre os pontos turísticos.
# Calcule a máxima pontuação obtida a partir de um par de pontos turísicos.
# Para calcular a pontuação some as avaliações dos dois pontos e em seguida subtraia a distância entre eles.

spots1= [8, 1, 5, 2, 6] #R: 11
spots2= [4, 1, 5, 2, 6] #R: 9

def max_score(array):
  answer = -1
  previous = -1

  for j in range(1, len(array)):
    i = j - 1
    previous = max(previous, array[i] + i)
    answer = max(answer, previous + array[j] - j)
  return answer