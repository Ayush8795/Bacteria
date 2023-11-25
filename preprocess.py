import os
import json
import shutil
path= "dataset/AGAR_dataset/dataset"

files= os.listdir(path)
print(len(files))
classes= []
images=[]
for file in files:
    name,ext= file.split('.')
    imgname= name+'.jpg'
    imgpath= os.path.join(path,imgname)
    print(imgpath)
    print("check")
    if ext=='json':
        print(f'dataset/{file}')
        jsonpath= os.path.join(path,file)
        dat= json.load(open(jsonpath))
        try:
            cl= dat['classes'][0]
        except:
            continue
        print(cl)
        try:
            os.mkdir(cl)
            tgt= os.path.join(cl,imgname)
            shutil.copy(imgpath,tgt)
        except:
            tgt= os.path.join(cl,imgname)
            shutil.copy(imgpath,tgt)