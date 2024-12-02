# from PIL import Image
#
# img = Image.open(r"C:\Users\Антон\Desktop\тестирование\a1cccbb91e8b64c356b21d399538f079.jpeg")
#
# #img_resized = img.resize((1000,1000))
# #img_resized.save(r"C:\Users\Антон\Desktop\тестирование\1111.jpeg","jpeg")
# img_grey= img.convert("L")
# img_grey.show()
# img_grey.save(r"C:\Users\Антон\Desktop\тестирование\1113.jpeg","jpeg")
# ################## библиотека OpenCV
# import cv2
#
# img=cv2.imread('D:\\py_files\\1113.jpeg')
# img_resize = cv2.resize(img,(500,1000))
# cv2.imshow('resize',img_resize)
# cv2.waitKey(0)
#img_cropped = img[top:10bottom,left:right] #обрезка изображения
# img_bw =cv2.cvtColor(img,cv2.COLOR_YCrCb2RGB) # изменение цвета
# img_rotate = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
#
# cv2.imwrite("D:\\py_files\\1113_modified.jpeg",img_rotate) # сохранение
################# сравнение изображение cv2
# import  cv2
# img_ref =cv2.imread('D:\\py_files\\1113.jpeg')
# img_test =cv2.imread('D:\\py_files\\1114.jpg')
# diff_img = cv2.absdiff(img_ref,img_test)
# cv2.imwrite('D:\\py_files\\diff.jpg',diff_img)
##################Подсвечивется контур отличий картинок
# import  cv2
# img_ref =cv2.imread('D:\\py_files\\1113.jpeg')
# img_test =cv2.imread('D:\\py_files\\1114.jpg')
# # преобразование в градации серого и вычисление различий
# gray1= cv2.cvtColor(img_ref,cv2.COLOR_BGR2GRAY)
# gray2 = cv2.cvtColor(img_test,cv2.COLOR_BGR2GRAY)
# diff = cv2.absdiff(gray1,gray2)
# # поиск контуров различий
# contours,_ =cv2.findContours(diff,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# # отрисовка прямоугольника вокруг контуров различий
# for contour in contours:
#     x,y,w,h =cv2.boundingRect(contour)
#     cv2.rectangle(img_test,(x,y),(x+w,y+h),(0,255,0),2)
# cv2.imwrite('D:\\py_files\\result.jpg',img_test)
############################## скриншоты Pillow
# from PIL import ImageGrab
# #сделать скриншот всего экрана
# image = ImageGrab.grab()
# #сохранить скриншот в файл
# image.save('D:\\py_files\\screenshot1.jpg')
# #Сделать скриншот конкретной области
# box=(10,10,500,500)
# image = ImageGrab.grab(bbox=box)
# #сохраняем в файл
# image.save('D:\\py_files\\cropped_screenshot.jpg')
################################ склеивание вкриншотов
from PIL import Image
img1 =Image.open('D:\\py_files\\1113.jpeg')
img2 =Image.open('D:\\py_files\\1114.jpg')
# Получение размера первого изображения
width1,height1 =img1.size
#получение размера 2 изображения
width2,height2 = img2.size
#Добавление второго изображения внизу первого
result= Image.new('RGB',(width1,height1+height2))
result.paste(im=img1,box=(0,0))
result.paste(im=img2,box=(0,height1))
result.save('D:\\py_files\\result.jpg')