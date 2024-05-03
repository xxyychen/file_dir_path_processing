# -*- coding = utf-8 -*-
# @Time : 2024/4/17 14:23
# @Author : XX
# @File : path_method.py
# @Software: PyCharm


def get_dirs_list():
    print("--------  os.listdir  --------")

    import os
    path_dir = "D:\python"
    # 获得 当前路径下的 文件
    files = os.listdir(path_dir)
    print(files)



class PathMethod():

    def __init__(self):
        pass

    def p1(self):
        print('------  os.path.join/abspath  ------')
        print('------  os.getcwd()           ------')

        import os

        # 1. 路径+文件夹 ————拼接路径 ===============
        base_path = "D:\图片\百度图片"
        keyword = "张天爱"

        path = os.path.join(base_path,keyword)
        print(path)

        # 2. 路径+桌面 =============================
        # 获取桌面路径
        # os.path.expanduser("~") == C:\Users\85317    'Desktop'
        path_desktop = os.path.join(os.path.expanduser("~"), 'Desktop')
        print(path_desktop)

        # 输出的pdf路径 os.path.join('文件夹1', '文件夹2', '文件.txt')
        # 文件夹1\文件夹2\文件.txt

        # 3. 路径+文件名 ===========================
        base_path = path_desktop
        file_name = "图片损坏信息.txt"
        path = os.path.join(base_path, file_name)
        # path = path_desktop + "/" + file_name

        print(path)


        # 4. 绝对路径 path.abspath  ============================

        # abspath 获取绝对(abs)路径
        print(os.path.abspath('.'))  # 当前的绝对路径 D:\python\study

        # __file__代表当前文件名
        # res = os.path.abspath(__file__)
        # print(res) # 当前的绝对路径 D:\python\study\9_1.py


        file_abspath = os.path.abspath('x.py') + '\\'
        # 当前的绝对路径 + 文件名(只是简单拼接，不看文件存不存在) ———— xxx\ x.py \
        print(file_abspath) # 当前路径 + 文件名

        # 5. 当前路径 getcwd ============================
        # “./” 当前路径
        path_current = os.getcwd()  # 获取当前路径的文件夹
        print(path_current)

        keyword = "张天爱"
        path = os.getcwd() + "\\" + keyword
        print(path)

        # 6. str/path .replace('\\', '/')   ======
        # D:\D_C++
        # #path = path.replace('\\', '/')  # 路径里面需要用 / 而不是 \


    def p1_2(self):

        import os

        res = f"D:\python\study\practice.py"
        # 得到文件所在目录  带文件名-去点
        re_ = os.path.dirname(res)
        print(re_) # D:\python\study

        # 得到上层目录  无文件名-返回上级目录
        #    re_ = D:\python\study
        rex = os.path.dirname(re_)
        print(rex) # D:\python




    def p2(self):
        print("-----os.path.split()  将 文件名和路径 分割开-----")

        import os
        pic_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0q8ecIRRfWQVbMKvwwux0_LY-Z9SCOg4nkQ&usqp=CAU'
        # os.path.split(pic_url)     ('https://...', 'imag...qp=CAU')

        # ('https://xxx.com', 'images?q=xxxx=CAU') [-1]
        name = os.path.split(pic_url)[-1]


    def p3_path_exist_flag(self,path):

        import os
        if not os.path.exists(path):

            print("新建文件，再写入")
            cookie = "buvid3=7-916"


if __name__ == "__main__":

    P = PathMethod()
    #P.p1()

    #P.p1_2()

    get_dirs_list()
