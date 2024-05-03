# -*- coding = utf-8 -*-
# @Time : 2024/4/17 14:30
# @Author : XX
# @File : file_method_1_write_read.py
# @Software: PyCharm


class FileMethod():

    def __init__(self):
        pass
        # fp.write() ≈≈ writelines()
        # fp.read()  ≈≈ readlines()  readline()

        # 写 读 文件必须关闭      with自动关闭文件，不需要.close()
        # 写文件，内容是中文的话，需要加 encoding='utf-8'  字符就不用

        # open() 打开 write() 写 close() 关


    def write_file(self,file_path,write_content=""):

        print("------  fp.write() ≈≈ writelines()  ------")
        print("------  .write()  str + \\n   file中的回车-需要自己加，print是自动加 ------")
        print("------  a 可追加 保存  append   不存在会新建------")
        # + rw 可读可写   r+  w+  a+    rb wb ab

        pics_url = [
            'https://img.alicdn.com/imgextra/i1/2251059038/O1CN01O2cFeD2GdSXvGvrOG_!!2251059038.jpg',
            'https://img.alicdn.com/imgextra/i1/2251059038/O1CN01Xpp8pR2GdSZl2bf4Y_!!2251059038.jpg',
            'https://img.alicdn.com/bao/uploaded/i2/2251059038/O1CN01G02dzG2GdSaGvuX3R_!!0-item_pic.jpg'
        ]

        # ================= fp.write() a =================
        if write_content == "":
            for pic in pics_url:
                # a 可追加 保存 append   不存在会新建
                with open(file_path, 'a', encoding='utf-8') as f:
                    f.write(pic + '\n')
                    #f.write('\n')
                    #print('下载成功！')


        # ================= fp.write() w =================
        # fp = open(file_path,"w", encoding='utf-8')
        # fp.write(write_content)
        # fp.close()

        # ================= fp.writelines() w =================
        if write_content != "":
            fp = open(file_path, "w", encoding='utf-8')
            fp.writelines(write_content)
            fp.close()


        # 2.  writelines()  参数可以是列表 list-------------------

        # fp = open(file_path, "w", encoding='utf-8')
        # content = ['hello\n', 'world\n', '你好\n', '智游\n', '郑州\n']
        # fp.writelines(content)
        # fp.close()


    def write_html(self):

        print("----- wb -----")
        # with open("baidu.html","wb") as f:
        #     f.write(res.content)


    def write_file_codecs_open(self,file_path,write_content=""):

        # codecs.open 似乎比 open要好
        import codecs

        file_h = codecs.open(file_path, 'a', "utf-8")
        file_h.write(write_content)
        file_h.close()


    def read_file(self,file_path):

        print("------  fp.read() 全读  ≈≈ readlines() ——lines返回一个列表，一个元素是一行内容 ------")
        print("------  fp.readline()  读(第)一行------")
        # 默认是 r   fp = open(file_path, encoding='utf-8')

        # 自动关闭文件！！！
        with open(file_path, "r", encoding='utf-8') as file:
            print(file.read())

        # 1.----------------------------------------------------
        # with open("./cookie.txt", "r", encoding="utf-8") as f:
        #     cookie = f.read()

        # 2.----------------------------------------------------
        # time_list = []
        # # 默认追加  读 r
        # with open(file_path, "r") as f:
        #     for time in f.readlines():
        #         time_list.append(time.strip())

        try:
            f = open(file_path, "r", encoding='utf-8')
            # ============================
            try:
                # ======================
                while True:
                    content = f.readline()
                    if len(content) == 0:
                        break
                    content = content.replace("\n", "")
                    print(content)
                # ======================
            finally:
                f.close()
                print("文件关闭成功------")
            # ============================

        except Exception as result:
            print("文件打开出错------")
            print(result)



def main_write():

    file_name = 'url_write.txt'
    file_path = base_path + file_name
    F.write_file(file_path)

    file_name = '诗歌-致橡树.txt'
    file_path = base_path + file_name

    s1 = "我如果爱你——" + "\n"
    s2 = "绝不像攀援的凌霄花,\n借你的高枝炫耀自己;\n"
    s3 = "我如果爱你——" + "\n"
    s4 = "绝不学痴情的鸟儿,\n为绿荫重复单调的歌曲;\n"
    write_content = s1 + s2 + s3 + s4

    # write_content = '''
    #     1.A
    #     2.B
    #     3.C
    #     4.D
    #     5.E
    #     6.F
    # '''

    F.write_file(file_path, write_content)


if __name__ == "__main__":

    F = FileMethod()
    base_path = ""

    #main_write()

    #F.read_file("诗歌-致橡树.txt")

    file_path = "诗歌-致橡树.txt"















