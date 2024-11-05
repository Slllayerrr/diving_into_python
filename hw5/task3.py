# # Создайте функцию генератор чисел Фибоначчи

# 1 вариант
n = 10
cnt = 0
num1 = 0
num2 = 1
res = [num1, num2]
while cnt < n - 2:
    item = num1 + num2
    num1 = num2
    num2 = item
    cnt += 1
    res.append(item)
print(res)


# 2 вариант
def fibon(n):
    cnt = 0
    num1 = 0
    yield num1
    num2 = 1
    yield num2
    while cnt < n - 2:
        item = num1 + num2
        num1 = num2
        num2 = item
        cnt += 1
        yield item


print(*fibon(n))
