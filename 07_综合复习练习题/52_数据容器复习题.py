# ===================== 复习题 =====================
# 第6章  list列表 · tuple元组 · set集合 · 序列切片
# ==================================================

# 题目1：给定 scores = [88, 72, 95, 60, 83, 91]
# (1) 打印第1个和最后1个元素
# (2) 打印前3个（切片）
# (3) 从小到大排序后打印
# (4) 追加 100，删除 60，打印最终列表
# 你的代码：


# 题目2：列表推导式
# (1) 生成 1~10 每个数的平方列表
# (2) 从 nums=[1,2,3,4,5,6,7,8,9,10] 里筛出大于5的数
# 你的代码：


# 题目3：元组
#   t = ('apple', 'banana', 'cherry')
# (1) 打印第2个元素
# (2) 用 for 循环遍历打印每个元素
# (3) 把元组转成列表，加入'mango'，再转回元组打印
# 你的代码：


# 题目4：集合去重
#   my_list = [3,1,4,1,5,9,2,6,5,3,5]
#   用集合去除重复元素，打印去重后的结果（顺序不定）
# 你的代码：


# 题目5：集合运算
#   a = {1, 2, 3, 4, 5}
#   b = {4, 5, 6, 7, 8}
#   打印：差集（a有b没有）、交集、并集
# 你的代码：


# 题目6：综合
#   给定句子 sentence = "python is great python is fun"
#   统计每个单词出现的次数并打印（提示：split + 遍历）
# 你的代码：


# ==================== 参考答案 ====================

# 答案1
# scores = [88, 72, 95, 60, 83, 91]
# print(scores[0], scores[-1])   # 88 91
# print(scores[:3])               # [88, 72, 95]
# scores.sort()
# print(scores)                   # [60, 72, 83, 88, 91, 95]
# scores.append(100)
# scores.remove(60)
# print(scores)                   # [72, 83, 88, 91, 95, 100]

# 答案2
# squares = [i ** 2 for i in range(1, 11)]
# print(squares)

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# big_nums = [n for n in nums if n > 5]
# print(big_nums)  # [6, 7, 8, 9, 10]

# 答案3
# t = ('apple', 'banana', 'cherry')
# print(t[1])            # banana
# for fruit in t:
    # print(fruit)
# lst = list(t)
# lst.append('mango')
# t2 = tuple(lst)
# print(t2)              # ('apple', 'banana', 'cherry', 'mango')

# 答案4
# my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# unique = set(my_list)
# print(unique)

# 答案5
# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}
# print(a.difference(b))   # 差集 {1, 2, 3}
# print(a & b)              # 交集 {4, 5}
# print(a | b)              # 并集 {1,2,3,4,5,6,7,8}

# 答案6
# sentence = "python is great python is fun"
# words = sentence.split()   # 切成列表
# word_count = {}
# for w in words:
    # if w in word_count:
        # word_count[w] += 1
    # else:
        # word_count[w] = 1
# for word, count in word_count.items():
    # print(f'{word}: {count}次')
