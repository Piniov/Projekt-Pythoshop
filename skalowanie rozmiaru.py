import PIL
import os, sys
from PIL import Image
print("Witaj w Pythoshopie! Program ten umożliwia Ci między innymi przeskalowanie Twojego obrazu!\n")
print()
imageFile=input("Wpisz nazwę pliku, który chcesz przeskalować (np. zabawny_pies.jpg):\n")
obrazek=Image.open(imageFile)
'''obrazek.show() #shows your image'''
print()
print("Oto dane dotyczące wczytanego (pierwotnego) pliku:\n", obrazek.format, obrazek.size, obrazek.mode) #displays format, size and mode of the primaty image
print()

print("Do jakiego formatu chcesz przeskalować swój obrazek: 1 - 4:3, 2 - 16:9, 3 - 1:1, 4 - 9:16, 5 - niestandardowy.\n")
scale_choice=int(input("Wybierz skale: "))
if scale_choice == 1:
    width=640
    height=480  #scale 4:3
    obrazek=obrazek.resize((width,height), Image.ANTIALIAS) #proper scaling of an image
    type=".jpg" #giving a file format
    obrazek.save("nowy" + type) #naming a new picture
    obrazek.show() #displays a new image :)
    print()
    print("Oto rozmiar przeskalowanego pliku (4:3):\n", obrazek.size) #shows a size of an image
    print()
elif scale_choice == 2:
    width=1280
    height=720  #scale 16:9
    obrazek=obrazek.resize((width,height), Image.ANTIALIAS)
    type=".jpg" 
    obrazek.save("nowy" + type) 
    obrazek.show() 
    print()
    print("Oto rozmiar przeskalowanego pliku (16:9):\n", obrazek.size) 
elif scale_choice == 3:
    width=1080
    height=1080  #scale 1:1
    obrazek=obrazek.resize((width,height), Image.ANTIALIAS) 
    type=".jpg" 
    obrazek.save("nowy" + type) 
    obrazek.show() 
    print()
    print("Oto rozmiar przeskalowanego pliku (1:1):\n", obrazek.size) 
elif scale_choice == 4:
    width=720
    height=1280  #scale 9:16
    obrazek=obrazek.resize((width,height), Image.ANTIALIAS) 
    type=".jpg" 
    obrazek.save("nowy" + type) 
    obrazek.show() 
    print()
    print("Oto rozmiar przeskalowanego pliku (9:16):\n", obrazek.size) 
elif scale_choice == 5:
    width=int(input("Podaj szerokość obrazu: "))
    height=int(input("Podaj wysokość obrazu: "))
    obrazek=obrazek.resize((width,height), Image.ANTIALIAS) 
    type=".jpg" 
    obrazek.save("nowy" + type) 
    obrazek.show() 
    print()
    print("Oto rozmiar przeskalowanego pliku (niestandardowy):\n", obrazek.size) 
