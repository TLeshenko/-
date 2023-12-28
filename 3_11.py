def simple():
    number = int(input("Введите число "))
    p = 0
    for i in range(1, number + 1):
        if number % i == 0:
            p+=1   
    if p <=2:
        print("Это простое число")
    if p > 2:
        print("Это не простое число")


if __name__ == "__main__":
    simple() 