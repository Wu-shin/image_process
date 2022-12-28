# import
import cv2
from matplotlib import pyplot as plt
import os

#定義resize function
def resize_func(img,scale,interpolation):
    nr,nc = img.shape[:2]
    nr2 = int(nr*scale)
    nc2 = int(nc*scale)
    retImg = cv2.resize(img,(nc2,nr2),interpolation= interpolation)
    return retImg

#選擇的照片進行儲存
def image_choice(img,choice):
    print(f"\n\n\n\n\nYou Choice is {choice}, It shape is {img.shape}")
    #新增一個新的名稱給新的影像
    img_path = str(newImage_path)+'_newImg'+'.png'
    #將影像儲存
    cv2.imwrite(img_path, cv2.cvtColor(img, cv2.COLOR_BGR2RGB), [cv2.IMWRITE_JPEG_QUALITY, 90])
    print("Save Image succeed")

#輸入影像的相對路徑，並且取得影像圖檔的名稱
image_path = str(input("輸入影像路徑:"))
newImage_path = image_path[:len(image_path)-4]
img = cv2.imread(image_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()


# 判斷是否需要進行resize
need_resize = eval(input("\n\n\n\n\n如果要resize請選擇1 否則選2\nchoice:"))
#如果有需要輸入scale大小，並且呼叫resize_fun
if need_resize == 1:
    scale = eval(input("\n\n\n\n\n請輸入resize scale: "))
    img1 = resize_func(img, scale, cv2.INTER_CUBIC)
    print("Before image resize",img.shape)
    print("After image resize",img1.shape)
    img = img1
elif need_resize == 2:
    pass
#防呆處理
else:
    print("輸入有誤程式中止")
    os._exit(0)


#先用高斯模糊進行處理
guassian = cv2.GaussianBlur(img,(1,1),0)

#再用雙邊濾波器進行美肌
newImg1 = cv2.bilateralFilter(guassian, 3, 50, 50)
newImg2 = cv2.bilateralFilter(guassian, 5, 50, 50)
newImg3 = cv2.bilateralFilter(guassian, 8, 50, 50)

# show出原圖以及進行過雙邊濾波器處理的影像
images = [img, newImg1, newImg2, newImg3]
titles = ['Original', 'Choice 1', 'Choice2', 'Choice3']
labels = ['','3x3','5x5','8x8']
plt.figure(figsize=(20, 5))
for i in range(4):
    plt.subplot(1, 4, i+1),plt.imshow(images[i],cmap='gray')
    plt.title(titles[i], fontsize=15, color='r')
    plt.xlabel(labels[i],fontsize=15, color='b')
plt.tight_layout()
plt.show()


#選擇喜歡的影像，呼叫image_choice來進行儲存
img_choice = eval(input("\n\n\n\n\n選擇你喜歡的:"))
if img_choice == 1:
    image_choice(newImg1,img_choice)
elif img_choice == 2:
    image_choice(newImg2,img_choice)
elif img_choice == 3:
    image_choice(newImg3,img_choice)
else:
    print("選擇不存在")