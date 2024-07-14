# 1 - тапшырма
"""
Программага пробел менен ажыратылган сандарды киргизебиз.
Берилген сандардын ичинен терс сандарды он санга айландырып чыгарыныздар
map функциясынын жардамы менен аткарыныздар

Мисалы:
-5 6 8 11 -10 0

Жооп:
5 6 8 11 10 0
"""
numbers = list(map(int, input().split()))
print(list(map(lambda x: x if x > 0 else -x, numbers)))
print(list(map(lambda x: abs(x), numbers)))


# 2 - тапшырма
"""
Программага томонкудой форматта сап(строка) киргизилет:
key_1=value_1 key_2=value_2 .... key_n=value_n

буларды кайра
(('key_1', 'value_1'), ('key_1', 'value_1'), ..., ('key_n', 'value_n'))
деп кортеж тибинде чыгарыныздар.
map функциясынын жардамы менен аткарыныздар
"""

text = list(map(str, input().split()))
print(tuple(map(lambda x: tuple(x.split("=")), text)))


# 3 - тапшырма
"""
Программага боштук менен бөлүнгөн бүтүн сандар киргизилет. 
Бул сандарды окуп, алардын ичинен эки орундуу сандарды гана калтыруу керек. 
Программаны filter функциясын колдонуп ишке ашыруу керек. 
Натыйжаны бир сапка боштук менен бөлүп экранга чыгарыңыз.

Мисалы:
8 11 0 -23 140 1

Жоопко:
11 -23
"""

numbers = list(map(int, input().split()))
print(list(filter(lambda x: 10 <= x < 100, numbers)))
# x >= 10 and x < 100
# 10 <= x < 100