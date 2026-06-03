"""
演示面向对象中的成员方法定义和使用

"""
# 定义一个带有成员方法的类
class Student:
    name=None

    def sey_hello(self):
        print(f'大家好呀，我是偶像练习生{self.name}')


    def sey_hello2(self,msg):
        print(f'大家好呀，我是偶像练习生{self.name},{msg}')

stu=Student()
stu.name='蔡徐坤'
stu.sey_hello2('小伙子可以的')

stu2=Student()
stu2.name='小舒欢'
stu2.sey_hello2('小伙子可以的')