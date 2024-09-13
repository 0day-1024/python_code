'''
if语句
⼀个简单的⽰例
下⾯的⽰例演⽰了如何使⽤ if 语句来正确地处理特殊的情形。
假设你有⼀个汽⻋列表，想将其中每辆汽⻋的名称打印出来。
对于⼤多数汽⻋，应以⾸字⺟⼤写的⽅式打印其名称，但是汽⻋名 'bmw' 应以全⼤写的⽅式打印。
下⾯的代码遍历这个列表，并以⾸字⺟⼤写的⽅式打印其中的汽⻋名，以全⼤写的⽅式打印 'bmw'
'''
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print("\n")

'''
条件测试
每条 if 语句的核⼼都是⼀个值为 True 或 False 的表达式，这种表达式称为条件测试。
Python 根据条件测试的值是 True 还是 False 来决定是否执⾏ if 语句中的代码。
如果条件测试的值为 True，Python 就执⾏紧跟在 if 语句后⾯的代码；如果为 False，Python 就忽略这些代码。
'''
#* 检查是否相等
#* ⼤多数条件测试将⼀个变量的当前值与特定的值进⾏⽐较。
#* 最简单的条件测试检查变量的值是否与特定的值相等：
car = 'bmw'
print(car == 'bmw')

#* 如何在检查是否相等时忽略⼤⼩写
#* 在 Python 中检查是否相等时是区分⼤⼩写的。
#* 例如，两个⼤⼩写不同的值被视为不相等：
car = 'Audi'
print(car == 'audi')

#* 如果⼤⼩写⽆关紧要，你只想检查变量的值，可先将变量的值转换为全⼩写的，再进⾏⽐较：
car = 'Audi'
print(car.lower() == 'audi')