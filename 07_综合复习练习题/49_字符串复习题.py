# ===================== 复习题 =====================
# 第2章  字符串 · 格式化 · 拼接 · 常用操作
# ==================================================

# 题目1：定义 msg = "  Hello, Python!  "
# (1) 去掉两端空格后打印
# (2) 转成全小写打印
# (3) 把 "Python" 替换成 "World" 打印
# 你的代码：
msg = "  Hello, Python!  "
k=msg.strip()
print(k)
w=msg.strip().lower()
print(w)
f=msg.strip().replace(" Python","world")
print(f)

# 题目2：用三种方式把 name="ki7" 和 score=99 拼成：
#   "ki7的分数是99分"
#   方式一：用 + 拼接
#   方式二：用 % 格式化
#   方式三：用 f-string
# 你的代码：
name="ki7"
score=99
print(name+'的分数是'+str(score)+'分')
print('%s的分数是%d分'%(name,score))



# 题目3：s = "abcdefgh"
# (1) 打印第3个字符（索引2）
# (2) 打印最后一个字符
# (3) 打印 "cde"（切片）
# (4) 倒序打印整个字符串
# 你的代码：
s = "abcdefgh"
print(s[2])
print(s[-1])
print(s[2:5])
print(s[::-1])



# 题目4：统计 sentence = "how many a are in this sentence a a"
# 里面字母 "a" 出现了几次，打印结果
# 你的代码：
sentence = "how many a are in this sentence a a"
count=sentence.count("a")
print(count)

# ==================== 参考答案 ====================

# 答案1
# msg = "  Hello, Python!  "
# print(msg.strip())                 # "Hello, Python!"
# print(msg.strip().lower())         # "hello, python!"
# print(msg.strip().replace("Python", "World"))  # "Hello, World!"

# 答案2
# name = 'ki7'
# score = 99
# print(name + '的分数是' + str(score) + '分')   # 方式一
# print('%s的分数是%d分' % (name, score))          # 方式二
# print(f'{name}的分数是{score}分')               # 方式三

# 答案3
# s = 'abcdefgh'
# print(s[2])      # c
# print(s[-1])     # h
# print(s[2:5])    # cde
# print(s[::-1])   # hgfedcba

# 答案4
# sentence = "how many a are in this sentence a a"
# print(sentence.count('a'))  # 4
