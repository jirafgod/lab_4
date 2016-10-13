from collections import Counter
# Итератор для удаления дубликатов
class Unique(object):
    ignore_case=False
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        self.ignore_case=False
        if (len(kwargs)>0 and kwargs['ignore_case']!=None) and (type(kwargs['ignore_case'])==bool):
            self.ignore_case=kwargs['ignore_case']
        self.arr = items
        self.buff=[]
    def __next__(self):
        for i in self.arr:
            temp = str(i)
            if (self.ignore_case):
                temp = temp.lower()
            if not temp in self.buff:
                self.buff.append(temp)
                return temp
        raise StopIteration()


    def __iter__(self):
        return self
