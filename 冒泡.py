def BubbleSort(s = []):
    l = len(s)
    k = l - 1
    while k > 0:
        k = k-1
        for i in range(0,l - 1):#一趟
            if s[i] > s[i + 1]:
                teamp = s[i]
                s[i] = s[i + 1]
                s[i + 1] = teamp
            else:
                continue
s = [2,31,4,5,3,23,5,3,223]
BubbleSort(s)
print(s)