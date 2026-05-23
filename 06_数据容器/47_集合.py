#定义集合
my_set={'小舒欢','欢小舒','欢欢欢','小舒欢','欢小舒','欢欢欢'}
print(my_set)
my_set.add('国服舒欢')
print(my_set)
my_set_empty = set()
print(my_set_empty)
my_set.remove('小舒欢')#移除集合中的元素
print(my_set)
# 随机取出一个元素
my_set.pop()
print(my_set)
# 清空集合
my_set.clear()
print(f'清空集合为{my_set}')
# 取出两个集合的差集  在集合1中取出集合二没有的元素
my_set1={'小舒欢','欢小舒','欢欢欢','小舒欢','欢小舒','欢欢欢'}
my_set2={'欢小舒','欢欢欢'}
my_set3=my_set1.difference(my_set2)
print(my_set3)
# 消除两个集合的差集   在集合1中消除集合2 中的元素 集合1修改 集合2不变
my_set1={'小舒欢','欢小舒','欢欢欢','小舒欢','欢小舒','欢欢欢'}
my_set2={'小舒欢','欢小舒'}
my_set1.difference_update(my_set2)
print(my_set1)
print(my_set2)
# 两个集合合并成一个
my_set1={'小舒欢','欢小舒','欢欢欢','小舒欢','欢小舒','欢欢欢'}
my_set2={'kiu','ki7'}
my_set3=my_set1.union(my_set2)
print(my_set3)
# 统计集合元素数量
my_set1={'小舒欢','欢小舒','欢欢欢','小舒欢','欢小舒','欢欢欢'}
num=len(my_set1)
print(num)
# 集合的遍历
# 集合不支持下标索引 不能用while循环
# 可以用for循环
set1={1,2,3,4,5,6,7,8,9,10}
for element in set1:
    print(f'她的元素有：{element}')


set7=set()
my_list=[1,4,3,7,9,5,6,2,3,3,4,5,6,7,8,9,10,10,10,10,3,5,6,7,8,9,3,2,1]
for element in my_list:
    set7.add(element)
print(set7)