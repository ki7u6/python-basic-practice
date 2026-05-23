#有字符串：欢舒张女美小
# 请用学到的任何方式得到小美女张舒欢
my_str = '好的收到,计师欢舒张女美小是哪骏,阿克吾'
# 切片取出，然后倒序字符串
value1=my_str[12:6:-1]
print(value1)
# 先倒叙字符串，然后切片取出
value2  =my_str[::-1][7:13]
print(value2)
value3=my_str.split(',')[1].replace('计师','').replace('是哪骏','')[::-1]
print(value3)



