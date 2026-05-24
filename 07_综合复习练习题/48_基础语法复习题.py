# ===================== 复习题 =====================
# 第1章  基础语法 · 变量 · 数据类型 · 运算符
# 先自己写，不会的往下翻参考答案
# ==================================================

# 题目1：定义 name="ki7", age=18, height=1.75
# 用 f-string 打印：  我叫ki7，今年18岁，身高1.75m
# 你的代码：
name='ki7'
age=18
height=1.75
print(f'我叫{name},今年{age}岁,身高{height}米')


# 题目2：把字符串 "100" 转成整数，再加上 50，打印结果
# 你的代码：
s='100'
count=int(s)+50
print(count)


# 题目3：不用第三个变量，交换 a=10 和 b=20 的值，打印 a 和 b
# 你的代码：
a,b=10,20
a,b=b,a
print(f'a={a},b={b}') 

# 题目4：计算下面三个表达式，用 print 验证自己的判断
#   (1) 10 % 3       → 应该是？
#   (2) 2 ** 8       → 应该是？
#   (3) 7 // 2       → 应该是？
# 你的代码：
a=10%3
print(f'10%3的值为{a}')
b=2**8
print(f'10%3的值为{b}')
c=7//2
print(f'10%3的值为{c}')


# 题目5：用 type() 打印 True、None、3.14 各自的数据类型
# 你的代码：
print(type(None))
print(type(True))
print(type(3.14))


# ==================== 参考答案 ====================

# 答案1
# name = 'ki7'
# age = 18
# height = 1.75
# print(f'我叫{name}，今年{age}岁，身高{height}m')

# 答案2
# s = '100'
# result = int(s) + 50
# print(result)  # 150

# 答案3
# a, b = 10, 20
# a, b = b, a
# print(f'a={a}, b={b}')  # a=20, b=10

# 答案4
# print(10 % 3)   # 1  (取余)
# print(2 ** 8)   # 256 (幂运算)
# print(7 // 2)   # 3  (整除)

# 答案5
# print(type(True))   # <class 'bool'>
# print(type(None))   # <class 'NoneType'>
# print(type(3.14))   # <class 'float'>
