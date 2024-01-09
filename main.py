#юніт-тести
#будемо перевіряти просту функцію
#функція додавання аргументів
def adder(*args, **kwargs):
    result = 0
    for _ in args:
        result += _
    for _ in kwargs.values():
        result += _
