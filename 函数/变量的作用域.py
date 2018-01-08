# L （Local） 局部作用域
# E （Enclosing） 闭包函数外的函数中
# G （Global） 全局作用域
# B （Built-in） 内建作用域
# a=12                #全局作用域
# a=int(11)           #内建作用域
#
# def outter():
#     # a=13          #闭包函数外的函数中a
#     def inner():
#         # a=14      #局部作用域a
#         print(a)
#     inner()
#     print(a)
# outter()
# print(a)


#王琪     14 13 12

#python函数里面可以嵌套函数   跟js一样   其他语言函数不能嵌套


def fn1():
    print("1")

def fn2():
    print(2)


