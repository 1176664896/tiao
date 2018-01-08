a=12
def outter():
    # global a
    a=13
    def inner():
        nonlocal a
        a=14
        print(a)
    inner()
    print(a)

outter()
print(a)

#结论1：全局变量被改变了    global可以改变全局变量
#结论2：闭包函数外的函数中的变量被改变了   nonlocal可以改变闭包函数外的函数中