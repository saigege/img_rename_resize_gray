# -*- coding: utf-8 -*-
"""

win10
anaconda
python3.6
scikit-image

@author: SAI
"""

from skimage import io, transform #, color
import os 

original_path = 'D:\京\plate' #原始图片路径
destination_path = 'D:/plate/plateresize/津' #修改后图片存放路径
number = 1 #序号
def resiz(f): #定义resize函数
    img=io.imread(f)    #依次读取rgb图片
    #gray=color.rgb2gray(rgb)   #将rgb图片转换成灰度图
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    form=transform.resize(img,(40,160))  #将灰度图片大小转换为40*160
    return form  
    
for root, dirs, files in os.walk(original_path):  #读取文件信息，files为文件名
    for filename in files:
        str_or = original_path + '/' + filename #合成原始图片路径
        #print(str_or)
        coll = io.ImageCollection(str_or,load_func=resiz) #读取，resize
        for i in range(len(coll)): #renumber，保存
            plat_name = filename[0:7] #取前六位为车牌号
            #filename_temp = filename[8:14] #取8~13位为序号
            n = number
            number += 1
            io.imsave(destination_path + '/'+ str(n) + '_'+ plat_name +'.jpg',coll[i]) #保存图片
