#1,2,3,4，四个数组成互不相同且无重复的三位数
for i in range(1,5):
    if i+1<=4:
        for j in range(i+1,5):
            if j+1<=4:
                for k in range(j+1,5):
                    a = i * 100 + j * 10 + k
                    b = i * 100 + k * 10 + j
                    c = j * 100 + i * 10 + k
                    d = j * 100 + k * 10 + i
                    e = k * 100 + j * 10 + i
                    f = k * 100 + i * 10 + j
                    print(a,b,c,d,e,f)

