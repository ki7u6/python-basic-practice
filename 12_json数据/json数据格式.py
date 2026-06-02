import json
# 准备列表，列表内每一个元素都是字典，将其转化为json
data=[{'name':'张三','age':11},{'name':'李四','age':12},{'name':'王五','age':13}]
json_str=json.dumps(data,ensure_ascii=False)
print(json_str)
print(json_str)
# 准备字典 将字典转化为json
d={'name':'kkk','age':11}
json_str=json.dumps(d,ensure_ascii=False)
print(json_str)
# 将json字符串转化为python数据类型
s='[{"name":"张三","age":11},{"name":"李四","age":12},{"name":"王五","age":13}]'
l=json.loads(s)
print(l)
print(type(l))
# 将json字符串转化为python数据类型{k:v，k:v}
k='{"name":"kkk","age":11}'
d=json.loads(k)
print(d)
print(type(d))