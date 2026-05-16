#演示嵌套调用函数
def fun_B():
    print('-----舒------')
def fun_A():
    print('-----小------')
    fun_B()
    print('-----欢------')
fun_A()
