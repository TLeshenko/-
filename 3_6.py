N = int(input("Введите целое число N "))
while N % 3 == 0:
   N = N / 3
if N == 1:
    print("Число является степенью числа 3")
else:
    print("Число не является степенью числа 3")
