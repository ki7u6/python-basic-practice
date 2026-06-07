#定义一个类 内部有私有成员变量和私有成员方法
class phone:
    __current_voltage = 1  #当前手机运行电压

    def __keep_single_core(self):
        print('让CPU以单核模式运行')
    def call_by_5g(self):
        if self.__current_voltage>=1:
            print('5g通话已开启')
        else:
            self.__keep_single_core()
            print('电量不足,无法使用5g通话，并已设置为单核模式进行省电')
phone=phone()
phone.call_by_5g()
