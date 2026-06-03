# 设计一个类
class Student:
    name=None
    gender=None
    nationality=None
    native_place=None
    age=None
# 创建一个对象（类比生活中打印一张登记表）
stu1=Student()
# 对象属性进行赋值
stu1.name='舒欢'
stu1.gender='girl'
stu1.age=21
stu1.native_place='河南'
stu1.nationality='CHINA'
# 获取对象中记录的信息
print(stu1.name)
print(stu1.native_place)
print(stu1.nationality)
print(stu1.age)
print(stu1.gender)