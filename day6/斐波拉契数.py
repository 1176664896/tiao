
def dg(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        return dg(n-1)+dg(n-2)
while 1:
    s=int(input("请输入一个数："))
    n=dg(s)
    print(n)