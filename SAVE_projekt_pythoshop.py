from PIL import Image
import os

def save_file(x):   #x - chosen file which user wants to save
    im = Image.open(x)
    print ("Wpisz nazwę nowego pliku")
    new_name = input()  #user has to name new file
    extension = '.jpg'  #extension is needed to allow Python writing a file as a picture file
    new_file = new_name + extension
    save_new_file = im.save(new_file)   #save() is a Pillow module function
    print ("Oto nazwa nowo utworzonego pliku:", new_file)
    return save_new_file

picture = "" #the name of the file user wants to save is needed 
save_file(picutre)
#User can find his new file in the same folder as that specific python file
