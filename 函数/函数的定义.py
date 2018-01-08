#1.无参无返回值类型
def fn1():
    print("函数的申明")
fn1()

#2.无参有返回值类型
def fn2():
    return "有返回值"
#定义一个变量来接受
s1=fn2()
print(s1)

#3.有参数没有返回值类型
def fn3(a,b):
    sum=a+b
    print("a和b的和为：",sum)
fn3(12,23)

#4.有参数有返回值类型
def fn4(a1,b1):
    return a1*b1
q=23
w=34
cj=fn4(q,w)
print(cj)
#a1和b1是形式参数
#q,w是实际参数


# def fn5(n):
#
#     print(n)
# fn5("张三")