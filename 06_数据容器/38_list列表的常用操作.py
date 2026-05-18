mylist=['张','舒','欢']
# 查找某元素在列表内的下标索引
index=mylist.index('欢')
print(f'"欢"在列表中的下标索引值为{index}')
mylist[0]='小'
print(mylist)

# 插入元素 insert方法
mylist.insert(1,'一头')
print(mylist)

# 追加元素 append方法 在列表的尾部追加一个函数
mylist.append('爱撒欢')#填要插入的元素即可
print(mylist)

# 追加元素方法2 在列表的尾部追加一批元素 extend方法
mylist2=['ki7',666,729]
mylist.extend(mylist2)
print(mylist)

# 删除指定下标索引的元素
mylist=['张','舒','欢']
# 方式1 del删除列表[下标]
del mylist[0]
print(f'列表删除元素后的结果是{mylist}')
# 方式2 列表.pop(下标)
mylist=['张','舒','欢']
element=mylist.pop(0)
print(f'列表通过pop方法取出元素后列表内容：{mylist},取出的元素{element}')
# 删除某元素在列表的第一个匹配项
mylist=['张','舒','舒','舒','欢','欢','欢']
mylist.remove('舒')
print(mylist)
# 清空列表元素方法 列表.clear()
mylist=['张','舒','欢']
mylist.clear()
print(mylist)