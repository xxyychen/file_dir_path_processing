# -*- coding = utf-8 -*-
# @Time : 2024/4/21 19:53
# @Author : XX
# @File : dir_method.py
# @Software: PyCharm




import os


# 遍历 目录/文件夹
def traverse_directory():

    print("--------  os.listdir(path) 获取路径下所有 文件、文件夹名称 --------")

    print("--------  import os  import os.path  --------")
    # os  os.path

    # li = os.listdir(r"D:\0000研\222")
    # sub_folder = os.listdir(url)

    import os
    real_url = r"C:\Users\85317\Desktop\test\snow" # 文件夹

    # 根目录，目录下的文件夹，目录下的文件
    for file_num in os.walk(real_url):
        # file_num = ('C:\\Users\\85317\\Desktop\\1\\2', [], ['QQ截.png', 'Qx.png', 'Qy.png'])
        print(file_num[2])  # 文件列表  ['QQ截.png', 'Qx.png', 'Qy.png']

        # for files in file_num[2]:
        # files='QQ截图20231219192605 - 副本 (2).png'



# 多层目录创建
def new_dirs_create(save_path):
    print("--------  os.make-dirs  多级目录  --------")
    print("--------  os.mk   dir    一级目录  --------")

    if not os.path.exists(save_path): # 如果不存在,就创建文件夹
        os.makedirs(save_path)  # 建多级目录 

        #os.mkdir(save_path) # 建一级目录


def keyword_dirs_create(file_path,keyword):

    tail = "/"
    if file_path[-1] != tail:  # 有时候在输入路径的时候，末尾会少一个 / ，
        # 这时候会保存到上一级目录里面，怪尴尬的
        file_path = file_path + tail

    dir_name = keyword  # 新建的文件夹名字

    if os.path.exists(file_path + dir_name):  # 查看路径是否存在
        print('该文件已存在，请重新输入')
        dir_name = input('请建立一个存储图片的文件夹，输入文件夹名称即可:')

        os.makedirs(file_path + dir_name)
    else:
        os.makedirs(file_path + dir_name)



def main():
    # 新建多层文件夹
    save_path = r'D:\图片\yy\x\y\z'
    new_dirs_create(save_path)

    keyword = "张天爱"
    # keyword = input('请输入你想下载的内容：')
    path = 'D:/图片/'  # 保存路径
    keyword_dirs_create(path, keyword)


if __name__ == "__main__":

    # main()



    li = ["1.mp4", "2.jpg", "3.mp4"]
    file = "1.jpg"
    path = r"D:\图片"
    a = [os.path.join(path, f) for f in li if f.endswith('.mp4')]
    print(a)

    # real_url = path.join(path, file)  # 字符串拼接
    # real_url = url + "\\" + fold

