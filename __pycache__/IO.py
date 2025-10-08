import math
print(f"pai = {math.pi:.20f}")


table = {'Sjoerdqqqqqqqq': 4127, 'Jack': 4098, 'Dcab': 7678}
for key,value in table.items():
    print(f'{key:20} ==> {value:20}')

for key,value in table.items():
    print(f'{key=:20} ==> {value=:20}')
    
print("{a}是什么{b}".format(a = "狗",b = '动物'))
print("{}大于{i}".format(2,i = 1))

print("Jack:{0[Jack]:d}".format(table))

for i in range(1,11):
    print(repr(i).rjust(2),repr(i*i).rjust(4),end=" ")
    print(repr(i*i*i).rjust(6))
    
    
f = open("test",'r+')
f.write("hello")
print(f.read())
for line in f:
    print(line,end=' ')

with open("test",'r+')as f:
    li = f.readlines()
    print(li)
    
import json
l = [1,'ass',"egg","hello"]
print(json.dumps(l))
f = open("test",'r+')
print(json.dump(l,f))


while True:
    try:
        x =  int(input("请输入一个整数："))
        break
    except ValueError:
        print('输入错误，请重新输入...')