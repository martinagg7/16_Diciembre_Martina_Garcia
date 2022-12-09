def fibo(n):
    a=0
    b =1
    for i in range(n):
        c = a + b
        a = b
        b = c
    return(c)
print(fibo(200000))

