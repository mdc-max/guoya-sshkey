# 求1-100的所有数的和
#!/usr/bin/env python
#-*- coding:utf-8 -*-
# sum = 0
# start = 1
# while True:
#     sum = sum + start
#     if start == 100:
#         break
#     start += 1
# print(sum)


# for 循环练习
#
# (1).用户登录需求：
#     1.输入用户名和密码；
#     2.判断用户名和密码是否正确（name='root',passwd='westos'）
#     3.登录仅有三次机会，超过3次会报错
# for i in range(3):
#     name = input('用户名:')
#     passwd = input('密码:')
#     if name == 'root' and passwd == 'westos':
#         print('登录成功')
#         break
#     else:
#         print('登录失败')
#     print('您还剩余%d次机会' %(2 - i))
# else:
#     print('登录次数超过三次，请稍后登录')


















#九九九九九九i九九i就i九九乘乘乘乘乘乘乘乘乘乘法法法法法法法法法法法法法表笔哦表笔哦表表
# for i in range(10):
#     #print(i)
#     for j in range(1,i+1):
#         print(j,'x',i,'=',i*j,end="\t")
#     print()

# i=0
# while i < 5:
#     print(i)
#     i += 1


#
# def sum(10,20):
#     print(10+20)
# def div():
# 	a = 10
# 	b = 2
# 	if b == 0:
# 		print("被除数不能为0")
# 		return
# 	return a / b
#
# print(div())


# 输入4位数num，每位都加5,再%10后倒序输出
a = input("请输入4位")
c=""
for i in a :
    b=str((int(i)+5)%10)
    c=c+b
print(c[::-1])
print(c)

# def sum(a,b):
#     print(a+b)
# sum(30,50)
# class TheFirstDemo:
#     '''这是一个学习Python定义的第一个类'''
#     #构造方法
#     def __init__(self):
#         print("调用构造方法")
#     # 下面定义了一个类属性
#     add = 'https://www.stu.guoyasoft.com/'
#     # 下面定义了一个say方法
#     def say(self, content):
#         print(content)
#     def __del__(self):
#         print("对象已经被删除")
# zhangsan = TheFirstDemo()