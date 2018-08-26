import face_recognition
import os
import shutil
def Test(rootDir):
    trainingLib = []
 
    for file in os.listdir(rootDir):    #os.listdir()是获取当前目录下的文件（当然包括文件夹和各种格式如.html，.xls等文件）
        file_path = os.path.join(rootDir,file)    #加入根目录使得到完整路径
        if os.path.isdir(file_path):      #如果还是文件夹，继续调用Test（）函数，得到当前文件夹下的各个文件
            Test(file_path)
        if '.jpg' in file_path:     #选取.jpg文件
 
            file_name = file_path
            trainingLib.append(file_name)   #加入list

    return trainingLib

def Recogition():
    Dir = input()
    trainingLib = Test(Dir)
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
    trainName=Test('train')
    testName=Test('test')
    finalTrainName='hello'
    finalTestName='hi'
    for i in range(len(train)):
        results = face_recognition.compare_faces(test,train[i],0.45)
        finalTrainName=splitName(trainName[i])
        path=os.getcwd()+"\\"+finalTrainName+"\\"
        os.mkdir(path)
        for j in range(len(test)):
            if results[j]:
                finalTestName=splitName(testName[j])
                copyFile(testName[j],finalTestName,finalTrainName)
        
def splitName(name):
    firstSplit=[]
    secondSplit=[]
    firstSplit=name.split(".")
    secondSplit=firstSplit[0].split('\\')
    finalName=secondSplit[1]
    return finalName
def copyFile(fullname,splitname,trainName):
    oldname=fullname
    newname=trainName+"\\"+splitname+'.jpg'
    shutil.copyfile(oldname,newname)

Comparison()
print("分类完成！")


















