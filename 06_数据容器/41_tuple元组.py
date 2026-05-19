#定义元组
# 元组不可以修改
t1=('舒欢','ki7',729,False)
t2=()
t3=tuple()
print(t1)
print(t2)
print(t3)
# 定义单个元素的元组
t4=('舒欢',)
print(f't4的类型是{type(t4)}')
# 元组的嵌套
t5=((1,2,3),(4,5,6))
print(f't5的类型是{type(t5)}，t5的内容是{print(t5)}')
# 下标索引去取出内容
num=t5[1][2]
print(f'从嵌套元组中取出的数据是{num}')
# 元组的操作 ：index查找方法
t6=(23,44,55,66,77,'王俊凯')
index=t6.index('王俊凯')
print(f'王俊凯在t6的下标索引为{index}')
# 元组的操作 count统计方法
t7=(23,'王俊凯','王俊凯','王俊凯',44,55,'王俊凯','王俊凯',66,77,'王俊凯')
count=t7.count('王俊凯')
print(f't7元组中有{count}个王俊凯')
# len函数统计元组元素数量
t7=(23,'王俊凯','王俊凯','王俊凯',44,55,'王俊凯','王俊凯',66,77,'王俊凯')
length=len(t7)
print(f't7元组中有{length}个元素')
# 元组的遍历 while for
def tuple_while_func():
    index=0
    while index<len(t7):
        element=t7[index]
        print(f't7元组分别为{element}')
        index+=1
tuple_while_func()

def tuple_for_func():
    for element in t7:
        print(element)
tuple_for_func()
# 定义一个元组，尝试修改元组内容
t9=(['国服','小'],'舒','欢')
print(t9)
t9[0][0]='世界服'
t9[0][1]='老'
print(t9)