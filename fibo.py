# date:2019/11/27
# author:pomelo


def fibo(n):
    if n <= 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


i = int(input("input a number:"))

if i <= 0:
    print("请输入正数")
else:
    print("斐波那契数列：")
    for x in range(i):
        print(fibo(x))
