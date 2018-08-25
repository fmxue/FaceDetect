import face_recognition
import os

def AbsPath(catalog):
    trainingLib = []
 
    for file in os.listdir(catalog):    #os.listdir()是获取当前目录下的文件（当然包括文件夹和各种格式如.html，.xls等文件）
        file_path = os.path.join(catalog,file)    #加入根目录使得到完整路径
        if os.path.isdir(file_path):      #如果还是文件夹，继续调用Test（）函数，得到当前文件夹下的各个文件
            AbsPath(file_path)
        if '.jpg' in file_path:     #选取.jpg文件
 
            file_name = file_path
            trainingLib.append(file_name)   #加入list

    return trainingLib

def Recogition():
    Dir = input()
    trainingLib = AbsPath(Dir)
    image = []
    FaceEncoding = []
    for i in range(len(trainingLib)):
        image.append(face_recognition.load_image_file(trainingLib[i]))
        try:
            FaceEncoding.append(face_recognition.face_encodings(image[i])[0])
        except IndexError:
            print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
            quit()
    return FaceEncoding

def Comparison():
    print("请输入训练目录：")    
    train = Recogition()
    print("请输入测试目录：")
    test = Recogition()
    trainName=AbsPath('test')
    finalName=''
    for i in range(len(train)):
        results = face_recognition.compare_faces(test,train[i])
        #path=os.getcwd()[:-4] + test[i]+'\\'
        #path=os.path.join(os.getcwd(),test[i]+'\\')
        finalName=splitName(trainName[i])
        #print(finalName)
        #print(type(trainName[i]))
        path=os.getcwd()+"\\"+finalName+"\\"
        os.mkdir(path)
        print(results)
        
def splitName(name):
    firstSplit=[]
    secondSplit=[]
    firstSplit=name.split(".")
    secondSplit=firstSplit[0].split('\\')
    finalName=secondSplit[1]
    return finalName
        
Comparison()
print("分类完成！")


















