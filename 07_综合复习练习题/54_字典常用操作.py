my_dict1={'舒欢':28,'明宇':88,'佳欣':99}
# 更新增加
my_dict1['小明']=84
my_dict1['明宇']=56
print(my_dict1)
# 删除
score=my_dict1.pop('小明')
print(f'字典中被去除了一个元素结果：{my_dict1},小明的考试成绩为{score}')
# 清空
my_dict1.clear()
print(my_dict1)
# 获取全部的key
my_dict1={'舒欢':28,'明宇':88,'佳欣':99}
keys=my_dict1.keys()
print(keys)
for key in keys:
    print(f'字典的key是{key}')
    print(f'{key}的成绩是{my_dict1[key]}')

for key in my_dict1:
    print(f'{key}的成绩是{my_dict1[key]}')
    # 统计字典内的元素数量
num=len(my_dict1)
print(f'字典中的元素数量是{num}')