
import PIL
import os
import os.path
from PIL import Image


# def iter_folder_make_scale_picture(directory,prefix):
#
#     for filename in os.listdir(directory):
#         name,extension = os.path.splitext(filename)
#         if extension.lower() in [".jpeg",".jpg",".png"]:
#             img = Image.open (os.path.join(directory, filename))
#             current_with, current_hight = img.size
#             scale_factor=0.1
#             new_with =int(current_with*scale_factor)
#             new_hight =int(current_hight*scale_factor)
#             img_resized = img.resize((new_with, new_hight))
#             new_filename=f'{name}_{prefix}{extension}'
#             img_resized.save(os.path.join(r"D:\py_files\modified_images",new_filename))
#
#
#
# iter_folder_make_scale_picture(r"D:\py_files\images","_resized")
#
# def iter_folder_make_black_white_picture(directory,prefix):
#     for filename in os.listdir(directory):
#         name, extension = os.path.splitext(filename)
#         if extension.lower() in [".jpeg", ".jpg", ".png"]:
#             img = Image.open(os.path.join(directory, filename))
#             img_grey=img.convert("L")
#             new_filename = f'{name}_{prefix}{extension}'
#             img_grey.save(os.path.join(r"D:\py_files\modified_images",new_filename))
# iter_folder_make_black_white_picture(r"D:\py_files\images","_bw")
#
#
# def iter_folder_make_cropp_picture(directory,prefix):
#     for filename in os.listdir(directory):
#         name, extension = os.path.splitext(filename)
#         if extension.lower() in [".jpeg", ".jpg", ".png"]:
#             img = Image.open(os.path.join(directory, filename))
#             width,height = img.size
#             if width < 100 and height < 100:
#                print(f"{filename} размер меньше 100на100, обрезка не применена")
#                continue
#             else:
#              img_crop=img.crop((0, 0,100,100))
#              new_filename = f'{name}_{prefix}{extension}'
#              img_crop.save(os.path.join(r"D:\py_files\modified_images",new_filename))
# iter_folder_make_cropp_picture(r"D:\py_files\images","_cropped")
######################### Вложенность по папкам. Цикл в цикле
def iter_folder_make_scale_picture(directory,prefix):

    for  root, dirs, files in os.walk(directory):
        for filename in files:

            name,extension = os.path.splitext(filename)
            if extension.lower() in [".jpeg",".jpg",".png"]:
             img_path = os.path.join(root,filename)
             img = Image.open (img_path)
             current_with, current_hight = img.size
             scale_factor=0.1
             new_with =int(current_with*scale_factor)
             new_hight =int(current_hight*scale_factor)
             img_resized = img.resize((new_with, new_hight))
             new_filename=f'{name}_{prefix}{extension}'
             output_path =os.path.join(r"D:\py_files\modified_images",new_filename)
             img_resized.save(output_path)

iter_folder_make_scale_picture(r"D:\py_files\images","_resized")