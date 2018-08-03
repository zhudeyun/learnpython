print("测试中文正常")
age=14
#age=int(input('please input age '))
if age>=18:
    print('your age is ',age)
    print('adult')
elif age>=6 and age<18:
    print('your age is',age)
    print('teenager')
else:
    print('kid')
    
names=['Michael','Bob','Tracy']
for name in names:
    print(name)
    
sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum+=x
print(sum)

print('生成整数序列：')
ls = range(101)
for l in ls:
    print(l)
sum = 0
for x in ls:
    sum+=x
print("sum:",sum)