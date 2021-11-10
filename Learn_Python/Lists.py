# -*- coding: utf8 -*-
# Cписки
# Для просмотра последнего элемента списка необходимо запросить элемент с индексом -1
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1]) # Этот же принцип можно применять и для предпоследнего и тд.

# Присоединение элементов в конец списка

#  метод -  .append , .insert

motorcycles = ['honda', ' suzuki', 'yamaha' , 'stels', 'nordway']
motorcycles.append('xren')
motorcycles.insert(2, ' kon')
del motorcycles[0]
popped_motorcycle = motorcycles.pop() # Метод рор удаляет последний элемент из списка, но позволяет далее работать с ним.
motorcycles.remove('nordway') # Удалает элемент по значению
motorcycles.sort() # Сортировка списка в алфавитном порядке
motorcycles.sort(reverse=True) # Сртировка в обратном порядке
print(motorcycles)
# Временная сортировка списка sorted, после вызова функции список продолжает хранится в первоначальном порядке
motorcycles.sorted()
motorcycles.sorted(reverse=True)
motorcycles.reverse() # Не сортирует а представляет список в обратном порядке.





