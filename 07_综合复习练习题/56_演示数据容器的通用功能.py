mylist=[1,2,3,4,5]
mytuple=(1,2,3,4,5)
mystr='1,2,3,4,5'
myset={1,2,3,4,5}
mydict={'key1':1,'key2':2,'key3':3,'key4':4,'key5':5,}
# len()元素个数
print(len(mylist))
print(len(mytuple))
print(len(myset))
print(len(mydict))
print(len(mystr))
# max最大元素
print(max(mylist))
print(max(mytuple))
print(max(myset))
print(max(mydict))
print(max(mystr))
# min最小元素
print(min(mylist))
print(min(mytuple))
print(min(myset))
print(min(mydict))
print(min(mystr))
# 转换类型 容器转了列表
print(f'列表转列表的结果是{list(mylist)}')
print(f'元组转列表的结果是{list(mytuple)}')
print(f'字符串转列表的结果是{list(mystr)}')
print(f'集合转列表的结果是{list(myset)}')
print(f'字典转列表的结果是{list(mydict)}')
# 转换类型 容器转了元组
print(f'列表转元组的结果是{tuple(mylist)}')
print(f'元组转元组的结果是{tuple(mytuple)}')
print(f'字符串转元组的结果是{tuple(mystr)}')
print(f'集合转元组的结果是{tuple(myset)}')
print(f'字典转元组的结果是{tuple(mydict)}')
# 转换类型 容器转了集合
print(f'列表转集合的结果是{set(mylist)}')
print(f'元组转集合的结果是{set(mytuple)}')
print(f'字符串转集合的结果是{set(mystr)}')
print(f'集合转集合的结果是{set(myset)}')
print(f'字典转集合的结果是{set(mydict)}')
# 进行容器的排序sorted()对元素进行排序 进入列表之中
print(sorted(mylist))
print(sorted(mytuple))
print(sorted(myset))
print(sorted(mydict))
print(sorted(mystr))
# 反向排序 reverse反转的意思
print(sorted(mylist,reverse=True))
print(sorted(mytuple,reverse=True))
print(sorted(myset,reverse=True))
print(sorted(mydict,reverse=True))
print(sorted(mystr,reverse=True))
