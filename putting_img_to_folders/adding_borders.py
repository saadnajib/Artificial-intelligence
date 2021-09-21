import cv2
import glob


photos = glob.glob('/home/lucky/Desktop/FR images Luckyone Staff/Security-SOC/*')
for p in photos:
    img = cv2.imread(p)
    str1 = p.split('/')[-1]
    str2 = str1.split('.')[-1]
    if str2 == "jpg":
        print(str1)
        color = [0, 0, 0] 
        left, right = [200]*2
        top, bottom = [100]*2
        img_with_border = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
        cv2.imwrite("/home/lucky/Desktop/bordered_images/"+str1+"",img_with_border)
