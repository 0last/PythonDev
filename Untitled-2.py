print("hello world!")

print(4/2)#4/2返回的也是浮点数
print(4//2)#整数除法

print(3**2)
hight=4**2#无需初始化
print(hight)
print('j'=='J')
# Print("hello")

s = "hello world"
print("""
      这
      是
      多
      行
      的
      写
      法
      """)
# print(""
#       这
#       是
#       多
#       行
#       的
#       写
#       法
#       "")#少一重会报错

print("8"*10)
print("a""b")#相邻直接合并

st = "abcd"
print(st[2])#下标访问字符串的字符
print(st[-1])

print(st[:20])#自动处理索引越界
print(len(st))
st = "lll"
print(st)

list  = [1,1,2,3,4,3]
list.append(10)
print(list)