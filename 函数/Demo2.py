# def fn1(name,age):
#     print("姓名为：",name)
#     print("年龄为：",age)
#
# # fn1(age=12,name="张三")
#
# def fn1(name,age=12):
#     print("姓名为：",name)
#     print("年龄为：",age)
#
# fn1("张三",23)


# def fn1(*num):
#     for i in num:
#         print(i)
#
# fn1("张三",23,"男")

def fn2(*num):
    for i in num:
        print(i)
fn2(12,13,14)


# def fn3(a,*num):
#     print(a)
#     print(num)
#     print(type(num))
# fn3(12,12,12,12,12,12,12)


#匿名函数
# sum=lambda a,b:a*b
# print(sum(10,20))

# def lambda(a,b):
#     cf=a*b
#
# sum=lanbda()
# sum(10,20)

#return语句
#用来计算长方形面积
# def mj(width,height):
#     cj=width*height
#     # return cj
#     print(cj)
#
# cj1=mj(10,20)
# print(cj1)



