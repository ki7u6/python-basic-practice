#定义一个元组，内容是['周杰伦',11,['football','music'],记录的是一个学生的信息(姓名，年龄，爱好)
ki7=('周杰伦',11,['football','music'])
# 查询年龄所在的下标位置
index=ki7.index(11)
print(f'年龄所在的下标位置为{index}')
# 查询学生的姓名
print(f'学生姓名为{ki7[0]}')
# 删除学生爱好中的football
del ki7[2][0]
print(ki7)
# 添加爱好coding到爱好list里
ki7[2].append('coding')
print(ki7)