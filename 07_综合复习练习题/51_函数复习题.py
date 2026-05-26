# ===================== 复习题 =====================
# 第5章  函数 · 传参 · 返回值 · 全局变量 · 嵌套调用
# ==================================================

# 题目1：定义函数 say_hello(name)，打印"你好，XXX！欢迎回来"
# 调用两次，传不同的名字
# 你的代码：
def say_hello(name):
    print("Hello " + name)
say_hello('舒欢')

# 题目2：定义函数 calc(a, b, op='+')，根据 op 做加减乘除并返回结果
#   calc(10, 3, '+')  → 13
#   calc(10, 3, '*')  → 30
#   calc(10, 3)       → 13  （默认加法）
# 你的代码：
def cale(a,b,op="+"):
    if op == '+':
        return a + b
    elif op == '*':
        return a * b
cale(10,3,"+")
print(cale(10,3,"+"))
print(cale(10,3,"*"))


# 题目3：全局变量练习
#   定义全局变量 count = 0
#   定义函数 add_count()，每次调用让 count +1
#   调用3次后打印 count（应该是3）
#   提示：函数内要用 global count
# 你的代码：



# 题目4：嵌套调用
#   定义 square(n) → 返回 n 的平方
#   定义 sum_of_squares(a, b) → 调用 square 后返回两数平方和
#   打印 sum_of_squares(3, 4) → 应该是 25
# 你的代码：


# 题目5：综合练习 — 简易计算器
#   定义 calculator(a, b, op)
#   op 是 '+''-''*''/' 之一
#   除以0时打印"不能除以0"并返回 None
#   其他情况返回计算结果
# 你的代码：


# ==================== 参考答案 ====================

# 答案1
# def say_hello(name):
    # print(f'你好，{name}！欢迎回来')

# say_hello('ki7')
# say_hello('小舒欢')

# 答案2
# def calc(a, b, op='+'):
    # if op == '+':
        # return a + b
    # elif op == '-':
        # return a - b
    # elif op == '*':
        # return a * b
    # elif op == '/':
        # return a / b

# print(calc(10, 3, '+'))  # 13
# print(calc(10, 3, '*'))  # 30
# print(calc(10, 3))       # 13

# 答案3
# count = 0

# def add_count():
    # global count
    # count += 1

# add_count()
# add_count()
# add_count()
# print(count)  # 3

# 答案4
# def square(n):
    # return n * n

# def sum_of_squares(a, b):
    # return square(a) + square(b)

# print(sum_of_squares(3, 4))  # 25

# 答案5
# def calculator(a, b, op):
    # if op == '+':
        # return a + b
    # elif op == '-':
        # return a - b
    # elif op == '*':
        # return a * b
    # elif op == '/':
        # if b == 0:
            # print('不能除以0')
            # return None
        # return a / b

# print(calculator(10, 2, '/'))  # 5.0
# print(calculator(5, 0, '/'))   # 不能除以0
