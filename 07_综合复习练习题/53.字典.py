#定义字典
my_dict1={'舒欢':28,'ki7':88}
print(my_dict1)
my_dict2={}
print(my_dict2)
my_dict3=dict()#空字典
print(my_dict3)
# 定义重复的字典
my_dict4={'舒欢':28,'ki7':88,'舒欢':29}
print(my_dict4)#如果有重复的字典,后面的value值会把前面的value值覆盖
# 从字典中基于key获取value
my_dict5={'舒欢':28,'ki7':88,'洛基':97}
score=my_dict5['舒欢']
print(f'舒欢的成绩是{score}')
score1=my_dict5['ki7']
print(f'ki7的成绩是{score1}')
score2=my_dict5['洛基']
print(f'洛基的成绩是{score2}')
SCore1={'语文':99,'数学':98,'英语':97}
SCore2={'语文':88,'数学':56,'英语':100}
SCore3={'语文':99,'数学':100,'英语':38}
check_score={'舒欢':SCore1,'明宇':SCore2,'佳欣':SCore3}
print(f'{check_score['舒欢']}')
print(f'{check_score['明宇']}')
print(f'{check_score['佳欣']}')
# 定义嵌套字典
Check_score_dict={
    "舒欢":{'语文': 99,
            '数学': 98,
            '英语': 97
    },"明宇":{'语文': 88,
            '数学': 56,
            '英语': 100
    },"佳欣":{'语文': 99,
             '数学': 100,
             '英语': 38
    }
}
print(f'舒欢的成绩为{Check_score_dict['舒欢']}')
print(f'明宇的成绩为{Check_score_dict['明宇']}')
print(f'佳欣的成绩为{Check_score_dict["佳欣"]}')
print(f'佳欣的成绩为{Check_score_dict["佳欣"]['数学']}')
