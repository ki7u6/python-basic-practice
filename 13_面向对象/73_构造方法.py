class Student:
    name=None
    age=None
    tel=None
    # 构造方法的名称 __init__
    def __init__(self,name,age,tel):
        self.name=name
        self.age=age
        self.tel=tel
        print('Student类创建了一个类对象')
stu=Student('小舒欢','100',18888888888)
print(stu.name)
print(stu.age)
print(stu.tel)
print(stu)
