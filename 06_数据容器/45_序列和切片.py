#对list进行切片，从1开始，4结束
my_list=[0,1,2,3,4,5,6,7]
result=my_list[1:4]#默认步长是1，可以省略不写
print(result)
# 对tuple切片，从头开始，到最后结束，步长1
tuple=(1,2,3,4,5,6,7)
result1=tuple[:]#冒号前后不写表示从头到尾
print(result1)
# 对str进行切片，从头开始，到最后结束，步长2
str='1234567'
result2=str[::2]
print(result2)
# 对str进行切片，从头开始，到最后结束，步长-1
str='0123456789'
value=str[::-1]
print(value)
# 对列表进行切片，从3开始，到1结束，步长-1
my_list=[0,1,2,3,4,5,6,7]
value=my_list[3:1:-1]
print(value)
# 对元组进行切片，从头开始，到尾结束，步长-2
tuple = (0,1,2,3,4,5,6,7)
value = tuple[::-2]
print(value)

