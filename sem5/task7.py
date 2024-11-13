# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел, начиная с числа 2.
# ✔ Для проверки числа на простоту используйте правило:
# «число является простым, если делится нацело только на единицу и на себя».

# 1

def isprime(count_num):
    prime_num = 2
    cnt = 1
    yield prime_num
    prime_num += 1
    while cnt < count_num:
        for i in range(3, prime_num, 2):
            if prime_num % i == 0:
                break
        else:
            cnt += 1
            yield prime_num
        prime_num += 2


print(*isprime(10))


# 2

def isprime2(count_num):
    prime_num = 2
    yield prime_num
    prime_num = 3
    cnt = 2
    yield prime_num
    while cnt < count_num:
        prime_num += 2

        for i in range(3, int(prime_num), 2):
            if prime_num % i == 0:
                break
        else:
            cnt += 1
            yield prime_num


print(*isprime2(2))
# print дугой вариант:
for num in isprime2(20):
    print(num)
