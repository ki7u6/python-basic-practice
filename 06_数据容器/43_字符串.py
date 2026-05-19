my_str='      sndsjd sidn ionug       '
# 通过下标索引取值
value=my_str[2]
print(value)
value2=my_str[-6]
print(value2)
# 找起始下标
value3=my_str.index('sidn')
print(value3)
# replace方法
kiu7=my_str.replace('sndsjd','舒欢')
print(kiu7)
# split方法
ki7=my_str.split(' ')
print(ki7)
# strip方法 不传入参数 就是取出收尾空格
ki5=my_str.strip()
print(ki5)
my_str='72a ds daad27'
ki4=my_str.strip('27')
print(ki4)
# 统计字符串中某个字符出现的次数
my_str='72a ds daad27'
count=my_str.count('2')
print(count)
# 统计字符串的长度
my_str=' sndsjd '
length=len(my_str)
print(length)