import os
import shutil



base_dir = "/home/master/Downloads/"


l = os.listdir(base_dir)



def move_to_images(filename):
    if not os.path.exists(base_dir+"images"):
        os.mkdir(base_dir+"images")
    shutil.move(base_dir+filename, base_dir+"images/")
    

def move_to_audios(filename):
    if not os.path.exists(base_dir+"audios"):
        os.mkdir(base_dir+"audios")
    shutil.move(base_dir+filename, base_dir+"audios/")

def move_to_videos(filename):
    if not os.path.exists(base_dir+"videos"):
        os.mkdir(base_dir+"videos")
    shutil.move(base_dir+filename, base_dir+"videos/")

def move_to_others(filename):
    if not os.path.exists(base_dir+"others"):
        os.mkdir(base_dir+"others")
    shutil.move(base_dir+filename, base_dir+"others/")


for i in l:
    if not os.path.isdir(base_dir+i):
        extension = i[-4:]
        if extension == ".jpg":
            move_to_images(i)
        elif extension == ".mp3":
            move_to_audios(i)
        elif extension == ".mp4":
            move_to_videos(i)
        else:
            move_to_others(i)





print("Successfully Updated!")