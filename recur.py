import math

#计算n的阶乘
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

n=fact(1000)
print(n)


def fact_inte(num, product):
    if num==1:
        return product
    return fact_inte(num-1,num*product)
    