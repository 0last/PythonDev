a = 0
if a > 0:
    print("a > 0")
elif a == 0:
    print("a == 0")
else:
    print("a < 0")
    
Words = ["min","world","win"]
for w in Words:
    print(w,len(w))
    
for i in range(5,10):
    print(i)

print(sum(range(5,10)))


# while True:
#     Ellipsis#==...
#     # ...#效果和pass类似
#     # pass#无限等待键盘中断

print("aaa")

s = 10

match s:
    case 100:
        print("不匹配")
    case _:#任意情况
        print("匹配成功")
        
        
s = "aa"
print(f"这是{s}")#Cpp中使用<<占位,UE中使用TEXT（%s）占位

class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
def where_is(point):
    match point:
        case point(x=0,y=0):
            print("原点")
        case point(x=0,y = y):
            print(f"y = {y}")
        case point(x = x,y=0):
            print(f"x = {x}")
        case point(x = x,y = y):
            print(f"x = {x},y = {y}")
        case _:
            print("未知")
# where_is(point(10,0))

from enum import Enum

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
color = Color(input("选择你的颜色（red,green,blue）:"))#在输入时就实例化对象

match color:
    case Color.RED:
        print("红色")
    case Color.GREEN:
        print("绿色")
    case Color.BLUE:
        print("蓝色")
    case _:
        print("未知")
    

    