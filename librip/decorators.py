# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно

def print_result(func):
    def wap(*args, **kwargs):
        print(func.__name__)

        cont = func(*args, **kwargs)

        if (type(cont) == list):
            print("\n".join([str(x) for x in cont]))
        elif (type(cont) == dict):
            print("\n".join([str(x) + " = " + str(cont[x]) for x in cont]))
        else:
            print(cont)

        return cont

    return wap
