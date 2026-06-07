class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
#         __str__魔术方法
    def __str__(self):
        return f'Student类对象name:{self.name},age: {self.age}'
    # __lt__ 小于大于比较
    def __lt__(self,other):
        return self.age<other.age
#     __le__ 小于等于和大于等于比较
    def __le__(self,other):
        return self.age<=other.age
#     __eq__相等判断

stu=Student('舒欢',18)
stu1=Student('s舒欢',19)
print(stu)
print(str(stu))
print(stu<stu1)
print(stu>stu1)