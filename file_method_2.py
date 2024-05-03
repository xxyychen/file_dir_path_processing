# -*- coding = utf-8 -*-
# @Time : 2024/4/21 16:58
# @Author : XX
# @File : file_method_2.py
# @Software: PyCharm


import os


def file_type_flag_0():

    # file = D:\other\5.mp4  或  5.mp4  都可
    file = r"D:\other\5.mp4"
    f = file.endswith('.mp4') # 检查 字符串file 是否以.mp4结尾的条件语句

    print(f)


# 判断 pic文件后缀
def file_type_flag(suffix='.jpg'):

    suffix = '.jpg'

    pic_url = 'https://www.cdharman.com/template/zanpian/statics/img/default.png'

    # os.path.split(path) 将一个完整的路径 拆分为两部分：目录和文件名
    # 返回一个元组 ('C://template//statics/img', '1.png')
    file_name = os.path.split(pic_url)[-1]

    print(file_name)

    if '.' not in file_name:
        file_name = file_name + suffix

    print(file_name)





# 分离 文件名和文件后缀
def name_split_suffix(file_name="8_张天爱.jpg"):

    #
    res = os.path.splitext(file_name) # ('8_张天爱', '.jpg')
    print(res)

    f_name = os.path.splitext(file_name)[0] # 文件名
    f_suffix = os.path.splitext(file_name)[1] # 后缀
    print(f_name)
    print(f_suffix)



if __name__ == "__main__":

    #file_type_flag(suffix='.jpg')

    #name_split_suffix()

    file_type_flag_0()