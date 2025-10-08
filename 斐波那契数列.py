a,b = 0,1
while a<20:
    print(a)
    print("\t")
    a,b = b,a+b


def fib(n):
    """打印斐波那契数列"""
    a,b = 0,1
    while a < n:
        print(a,end = "  ")
        a,b = b,a + b 
        
# fib(20)

anum = 100000 
print(anum)