"""
функция p(n), вызывающая эту же самую функцию с аргументом, уменьшенным на единицу,
и после чего печатающую значение аргумента
"""
def p(n):
    if n == 0:
        return
    else:
        p(n-1)
        print(n)
p(5)

# 1
# 2
# 3
# 4
# 5