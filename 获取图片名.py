import os

 

file0ss = []

def Test(rootDir):

 

    for file in os.listdir(rootDir):    #os.listdir()是获取当前目录下的文件（当然包括文件夹和各种格式如.html，.xls等文件）

        file_path = os.path.join(rootDir,file)    #加入根目录使得到完整路径

        if os.path.isdir(file_path):      #如果还是文件夹，继续调用Test（）函数，得到当前文件夹下的各个文件

            Test(file_path)

        if '.jpg' in file_path:     #选取.jpg文件

 

            file_name = file_path.split('\\')[-1]

            file0ss.append(file_name)   #加入list

 

    return file0ss

 

file_0 = r'D:\暑假训练营\大作业'

file_1 = r'D:\暑假训练营\大作业\新建文件夹'

filess = Test(file_0,)

 

print(filess)