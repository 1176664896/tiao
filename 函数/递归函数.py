#从控制台传入一个参数n，输出n的阶乘
s=int(input("请输入一个整数"))
# sum=1
# for i in range(1,n+1):
#     sum=sum*i
#
# print(sum)

def dg(n):
    if n==1:
        return 1
    else:
        return n*dg(n-1)

jc=dg(s)
print(jc)
