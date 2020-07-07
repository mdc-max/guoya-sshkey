# def div(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError as e:
#         print(e)
#
# div(10,0)
#
#
class CustomException(Exception):
#
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return self.value

a = 'sssssss'
try:
    if a == 0:
        print('a = {} 触发异常'.format(a) )
        raise CustomException('值不能为0')
    print ('a = {} 未触发异常'.format(a))
except CustomException as e :
    print(e)