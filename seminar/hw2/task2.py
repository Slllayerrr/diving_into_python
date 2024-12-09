# Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и *произведение дробей.
# Для проверки своего кода используйте модуль fractions.
import fractions

frac1 = fractions.Fraction('1/2')
frac2 = fractions.Fraction('1/3')

sum = frac1 + frac2
print(sum)
multiplication = frac1 * frac2
print(multiplication)

