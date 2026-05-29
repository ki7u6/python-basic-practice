def user_info(name,age,gender):
    print(name,age,gender)

user_info('小明',19,'男')
user_info('小王',gender='男',age=21)
user_info(name="小龙",gender='女',age=21)

def user_info(name,age,gender='男'):
    print(name,age,gender)

user_info('ki7',25)

# 不定长 位置不定长 *号 参数会作为元组存在，接受不定长数量的参数传入
def user_info(*args):
    print(args)
user_info(1,11,2,'小欢')


# 不定长 关键字不定长 **号 参数会作为字典存在，接受不定长数量的参数传入
def user_info(**kwargs):
    print(kwargs)
user_info(age=17,name='小欢')



