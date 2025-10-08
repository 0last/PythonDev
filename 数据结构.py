fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.append("Okk")
print(fruits)

fruits2 = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits2[len(fruits2):] = ["Okk"]#类似fruits.append("Okk")
print(fruits2)

fruits.extend(fruits2)#将整个列表插入另一个列表
print(fruits)

fruits2.insert(0,"100")#指定位置插入
print(fruits2)

fruits2.pop(0)
# print()
print(fruits2)

fruits2.reverse()
print(fruits2)


list = list(map(lambda x:x**2,range(10)))#map将参数二中的所有值都执行参数一的函数
print(list)

print([x for x in range(20)if x<=10])#列表推导式

#翻倍
num = [1,43,4,5,6,2]
print([x*2 for x in num])#使用列表推导式将一个列表中的所有数值翻倍

map = ([1,2,3],["a","b","c"])
print(map)

v = 1,2,3,"abc"
print(v)

a = set("asddffggh")#集合去除重复元素
print(a)

bset = {"asd","a","sdff","a"}
print(bset)


zidian = {1:"a",2:"b"}
print(zidian[1])
for k,v in zidian.items():
    print(k,v)
    
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q,a in zip(questions,answers):
    # print("what your {0}?       it is {1}".format(q,a))
    print(f"what your {q}?       it is {a}")

import 斐波那契数列
fibo = 斐波那契数列.fib

aa = 斐波那契数列.anum
print(fibo(10))

斐波那契数列.anum = 10
print(斐波那契数列.anum)
print(aa)

# from 斐波那契数列 import fib
# print(dir(斐波那契数列))
# import builtins
# print(dir(builtins))

st = 'aaass'
print(str(st))
print(repr(st))