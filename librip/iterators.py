# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False

        self.ignore_case = kwargs.get('ignore_case', False)
        self.arr = iter(items)
        self.buff = set()

    def __next__(self):
        while True:
            value = next(self.arr)
            temp = value
            if self.ignore_case:
                temp = temp.lower()
            if not temp in self.buff:
                self.buff.add(temp)
                return value

    def __iter__(self):
        return self
