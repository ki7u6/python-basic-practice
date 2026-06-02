def print_file_info(file_name):
    '''
    将给定路径的文件内容输出到控制台
    :param file_name:即将被读取的文件路径
    :return:None
    '''
    f=None
    try:
        f=open(file_name,'r',encoding='utf-8')
        content=f.read()
        print('文件的全部内容如下：')
        print(content)
    except Exception as e:
        print(f'程序出现异常了，原因是{e}')
    finally:
        if f:  #如果变量是None，表示Flase，如果有任何内容，就是True
            f.close()

def append_file_info(file_name,data):
    '''
    将指定的数据追加到指定的文件中
    :param file_name:指定文件的路径
    :param data:指定文件的数据
    :return:None
    '''
    with open(file_name,'a',encoding='utf-8') as f:
        f.write(data)
        f.write('\n')


if __name__ == '__main__':

    # print_file_info('D:/AI开发实习冲刺计划.txtxxx')

