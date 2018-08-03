import math
def my_sum(x,y):
    return(x+y)

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x

def move(x,y,step,angle=0):
    nx = x+step*math.cos(angle)
    ny = y+step*math.sin(angle)
    return nx, ny
        
sum=my_sum(1,2)
print(sum)

abs = my_abs(-100)
print(abs)

x, y =move(100,100,60,math.pi/6)
print(x,y)

badType = my_abs('-10')
print(badType)