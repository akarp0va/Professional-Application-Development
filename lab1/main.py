import random

#функция перестановки
def permutation(arr):
    # индекс элемента
    index_element = 1
    # счетчик и максимальный счетчик; счетчик - это длина последовательности одинаковых элементов
    counter = max_counter = 1
    for i in range(1, len(arr)):
        #если текущий элемент списка равен предыдущему
        if arr[i] == arr[i - 1]:
            #то счетчик увеличивается на 1
            counter += 1
        else:
            #если длина текущей последовательности одинаковых элементов больше максимальной длины
            if counter > max_counter:
                #присваиваем максимальной длине последовательности одинаковых элементов новое значение
                max_counter = counter
                index_element = i
            counter = 1
    #если нашли самую максимальную длину
    if counter > max_counter:
        max_counter = counter
        index_element = i + 1
    return index_element - max_counter, index_element


command = int(input("Если вы хотите ввести элементы с помощью автоматической генерации - 1, с помощью клавиатуры - 2: "))
match command:
    case 1:
     N = int(input("Введите размер массива A: "))
     M = int(input("Введите размер массива B: "))
     A = []
     B = []

     #рандомное заполнение списка
     for i in range(N):
       A.append(random.randint(1, 7))
     print("\nМассив A:", A)

     for i in range(M):
       B.append(random.randint(1, 7))
     print("Массив B:", B)

    case 2:
      #ввод элементов с клавиатуры
      print("Введите массив А: ")
      A = input().split()
      print("Введите массив В: ")
      B = input().split()

      #проверка списка на корректный ввод данных
      res = all(ele.isdigit() for ele in A)
      if res == False:
          print("\nВведите, пожалуйста, целое число, а не иной символ.")
          raise SystemExit(1)

      res = all(ele.isdigit() for ele in B)
      if res == False:
          print("\nВведите, пожалуйста, целое число, а не иной символ.")
          raise SystemExit(1)

      print("Массив A:", A)
      print("Массив B:", B)

#замена цепочек
a_start, a_end = permutation(A)
b_start, b_end = permutation(B)
#срез из списка А с максимальной последовательностью одинаковых элементов
a_slice = A[a_start:a_end].copy()
#срез из списка В с максимальной последовательностью одинаковых элементов
b_slice = B[b_start:b_end].copy()

#соединяем срез из начала списка, максимальную последовательность другого списка и конец текущего списка
A = A[:a_start] + b_slice + A[a_end:]
B = B[:b_start] + a_slice + B[b_end:]

print("\nРезультат перестановки: ")
print(A)
print(B)


