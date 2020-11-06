import os
import shutil

"""
total_list = []
def recur_f(the_dir):
    lsd = os.listdir(the_dir)
    for d in lsd:
        if the_dir  == "/":
            new_path = the_dir+d
        else:
            new_path = the_dir +"/"+d
        #print(d)
        if os.path.isdir(new_path):
            try:
                recur_f(new_path)
            except PermissionError:
                print("permission error")
        else:
            print(new_path)
            total_list.append(new_path)
            continue




recur_f("/home/master/professor/web dev with Angela")
print(len(total_list))
"""




base_dir = "/home/master/Downloads/"


l = os.listdir(base_dir)
images = []
videos = []
audios = []
others = []




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
        # print(i[-4:])
        extension = i[-4:]
        if extension == ".jpg":
            images.append(i)
            move_to_images(i)
        elif extension == ".mp3":
            audios.append(i)
            move_to_audios(i)
        elif extension == ".mp4":
            videos.append(i)
            move_to_videos(i)
        else:
            others.append(i)
            move_to_others(i)





print("Images .. \n")
for i in images:
    print(i)
print("___________________")

print("Audios .. \n")
for a in audios:
    print(a)
print("___________________")

print("Videos .. \n")
for v in videos:
    print(v)
print("___________________")

print("Others .. \n")
for o in others:
    print(o)
print("___________________")




# with open(base_dir+"tsfile.txt",'w') as file:
#     file.writelines(["this is what\n","address bar long"])
"""
try:
    print("trying")
    os.mkdir(base_dir+"tss")
        
except FileExistsError:
    pass
    
try:
    print("trying22")
    shutil.move(base_dir+"tsfol",base_dir+"tss/")
except shutil.Error:
        print("shutiler")

"""





print("Successfully Updated!")