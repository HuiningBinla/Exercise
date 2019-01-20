#-*- coding:utf-8 -*-
# 计算0-100之间整数和
# 思路：
# 1.准备数字
# 2.计算

print("计算0-100之间整数和")
print("方法一")
sum = 0
n = 0
while n <= 100:
    sum += n
    n += 1

print('整数和是：%d ' % sum)

print("方法二")
sum = 0
for x in range(101):
    sum += x
    
print('整数和是：%d ' % sum)


print("计算0-100之间的所有奇数之和")
print("方法一")
sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
# print(n)   
print("100之内奇数和是： %s " % sum)

print("方法二")
sum = 0
n = 0
while n <= 100:
    # 判断变量n的值是否是奇数
    if n % 2 != 0:
        sum += n
    n += 1
    
print("100之内奇数和是： %s " % sum)


print("计算0-100之间的所有偶数之和")
print("方法一")
sum = 0
n = 100
while n >= 0:
    sum += n
    n -= 2

# print(n)    
print("100之内偶数和是：%d " % sum)

print("方法二")
sum = 0
n = 0
while n <= 100:
    if n % 2 == 0:
        sum += n
    n += 1
    
print("100之内偶数和是：%d " % sum)
    
    
    
    
