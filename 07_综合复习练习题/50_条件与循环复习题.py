# ===================== 复习题 =====================
# 第3-4章  if判断 · while循环 · for循环 · range
# ==================================================

# 题目1：score = 88，用 if/elif/else 打印等级
#   ≥90 优秀 | ≥75 良好 | ≥60 及格 | 其余 不及格
# 你的代码：
score=88
if score>=90:
    print("优秀")
elif score>=75:
    print('良好')
elif score>=60:
    print('及格')
else:
    print('不及格')

# 题目2：用 while 循环计算 1+2+3...+100 的总和并打印
# 你的代码：
i=1
sum=0
while i<=100:
    sum+=i
    i=i+1
print(sum)

# 题目3：用 for + range 打印 1~20 里的奇数（用 continue 跳过偶数）
# 你的代码：
for x in range(0,20):
    if x%2!=0:
        print(x)
    else:
        continue

# 题目4：用 for 遍历列表 words = ['python','java','go','rust']
# 打印每个单词和它的长度，格式：  python → 6个字母
# 你的代码：
words = ['python','java','go','rust']
for word in words:
    print(f'{word}有{len(word)}个字母')


# 题目5：猜数字（不用input，直接模拟）
#   secret = 66
#   猜测列表 = [20, 80, 66, 50]
#   太小打印"小了"，太大打印"大了"，猜对打印"猜对了！"并 break
# 你的代码：
secret = 66
list = [20, 80, 66, 50]
for l in list:
    if l==secret:
        print('猜对了')
        break
    elif l>secret:
        print('猜大了')
    else:
        print('猜小了')




# 题目6：用嵌套循环打印 3×3 的星号矩形（每行3个*）
#   * * *
#   * * *
#   * * *
# 你的代码：
for x in range(3):
    for y in range(3):
        print('*',end='')
    print()


# ==================== 参考答案 ====================

# 答案1
# score = 88
# if score >= 90:
    # print('优秀')
# elif score >= 75:
    # print('良好')
# elif score >= 60:
    # print('及格')
# else:
    # print('不及格')

# 答案2
# total = 0
# i = 1
# while i <= 100:
    # total += i
    # i += 1
# print(f'1到100的总和是{total}')  # 5050

# 答案3
# for i in range(1, 21):
    # if i % 2 == 0:
        # continue
    # print(i, end=' ')
# print()

# 答案4
# words = ['python', 'java', 'go', 'rust']
# for w in words:
    # print(f'{w} → {len(w)}个字母')

# 答案5
# secret = 66
# guesses = [20, 80, 66, 50]
# for g in guesses:
    # if g < secret:
        # print(f'{g} 小了')
    # elif g > secret:
        # print(f'{g} 大了')
    # else:
        # print(f'{g} 猜对了！')
        # break

# 答案6
# for row in range(3):
    # for col in range(3):
        # print('*', end=' ')
    # print()
