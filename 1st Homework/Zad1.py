# 1. Напишете програма, която взима число n от input и генерира редица на фибоначи 
# до този елемент като я принтира на екрана. Пример n = 10 - 1, 1, 2, 3, 5, 8

n = int(input("Enter a number: "))
result = [1, 1]
a = 1
b = 1
print("n = ", n)
while a + b < n:
    c = b
    b = a + b
    a = c
    result.append(b)
print(result)