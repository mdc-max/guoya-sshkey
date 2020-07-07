


class Parent():

    money=1000000
    house=100
    def skill(self):
        print('点石成金')
    def __init__(self):
        pass

class Child (Parent):
    ai_hao='花钱'

    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
c = Child()

print(c.ai_hao)
print(c.house)
print(c.money)
c.skill()

# print(os.path.exist)

# from test1 import 练习导入
# print(a)

# name()
# # print()
# from test1 import 练习导入
# if __name__=='__main__':
#     name()
#     print()
# a=123456
# class Parent():
#     money = 10000000000
#     house = 100
#     __clothes = "裤子"
#
#     def __init__(self,a):
#         self.a = a
#
#     def shou_yi(self):
#         print("点石成金")
#
# class Child(Parent):
#     def shou_yi(self):
#         super().shou_yi()  #多态：一定是发生在子类和父类之间，必须重写父类的方法
#         print("影分身")
#     ai_hao = "花钱"
#     pass
#
# c = Child(123)
# print(c.ai_hao)
# print(c.house)
# print(c.money)
# c.shou_yi()
