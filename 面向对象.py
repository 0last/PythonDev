def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam#在上一级绑定
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    
    spam = "test spam"
    do_local()
    print(spam)
    do_nonlocal()
    print(spam)
    do_global()
    print(spam)
scope_test()
print(spam)#global spam

if True:
    class MyClass:
        print("hello class!")
        
        
class Dog:
    kind = 'canine'
    def __init__(self,name):
        self.name = name
        
d = Dog('Budi')
e = Dog('Fido')        
print(f"{d.kind} name is: {d.name}")
print(f"{e.kind} name is: {e.name}")


ls = "sssjjj"
it = iter(ls)
print(it)
print(next(it))
print(next(it))
        
import os
print(os.getcwd())
print(help(os))