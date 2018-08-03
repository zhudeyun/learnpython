import math
def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

def enroll(name, gender, age=6, city='Beijing'):
    print('name: ',name)
    print('gender: ',gender)
    print('age: ',age)
    print('city: ',city)
    print()
    
#n =power(5,3)
#print(n)

#m=power(4)
#print(m)

#s = enroll('Xiaowang','男',city='Nanjing')
#print(s)

def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum

nums = [1,2,3,4]
sum = calc(*nums)
print(sum)

def person(name, age, **kw):
    if 'city' in kw:
    #有city参数
        pass
    if 'job' in kw:
    #有job参数
        pass
    print('name:',name,'age:',age,'other:',kw)

print(person('Bob',18,city='Beijing',job='Enginer'))
extra = {'city':'Beijing','job':'Engineer'}  #dict
print(person('Bob',20,**extra))

print(person('Bob',24,city = 'Beijing',addr='changyang',zipcode=111))