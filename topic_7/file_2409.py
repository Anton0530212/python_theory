# n = int(input())
#
# prod = 1
# summa = 0
# while n > 0:
#     last_digit = n % 10
#
#     if last_digit != 0:
#         prod *= last_digit
#         summa += last_digit
#
#     n //= 10
#
# print('Произведение:', prod)
# print('Сумма:', summa)

# ----------------


# Задание 7
# num = int(input('Введите число: '))
#
# small_prime_num = 2  # наименьшее простое число
# while small_prime_num <= num:
#     if ...:
#         ...
#
#     else:
#         ...


# https://academy.yandex.ru/handbook/python/article/cikly

# while True:
#     n = int(input())
#
#     if n == 0:
#         break
#
    # print(n)


# while (n := int(input())) != 0:
#     print(n)

# while 0:
#     pass

# while n := int(input()):
#     print(n)


# ---------------------

# double = float(input())
i = 0.0
while i <= 1:
    print(round(i, 1))
    i += 0.1
