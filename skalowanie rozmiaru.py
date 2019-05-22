import PIL
import os, sys
from PIL import Image
print("Witaj w Pythoshopie! Program ten umożliwia Ci między innymi przeskalowanie Twojego obrazu!\n")
print()
imageFile=input("Wpisz nazwę pliku, który chcesz przeskalować (np. zabawny_pies.jpg):\n")
obrazek=Image.open(imageFile)
'''obrazek.show() #otwiera pierwotny obrazek'''
print()
print("Oto dane dotyczące wczytanego (pierwotnego) pliku:\n", obrazek.format, obrazek.size, obrazek.mode) #pokazuje format, rozmiar i typ obrazu
print()

print("Do jakiego formatu chcesz przeskalować swój obrazek: 1 - 4:3, 2 - 16:9, 3 - 1:1, 4 - 9:16, 5 - niestandardowy.\n")
scale_choice=int(input("Wybierz skale: "))
if scale_choice == 1:
    width=640
    height=480  #skalowanie 4:3
    obrazek=obrazek.resize((width,height), Image.ANTIALIAS) #właściwe przeskalowanie obrazka
    type=".jpg" #nadanie formatu pliku
    obrazek.save("nowy" + type) #nadanie nazwy nowemu (przeskalowanemu) obrazkowi
    obrazek.show() #pokazuje już nowy, przeskalowany obrazek :)
    print()
    print("Oto rozmiar przeskalowanego pliku (4:3):\n", obrazek.size) #pokazuje rozmiar obrazu
    print()
elif scale_choice == 2:
    width=1280
    height=720  #skalowanie 16:9
    obrazek=obrazek.resize((width,height), Image.ANTIALIAS) #właściwe przeskalowanie obrazka
    type=".jpg" #nadanie formatu pliku
    obrazek.save("nowy" + type) #nadanie nazwy nowemu (przeskalowanemu) obrazkowi
    obrazek.show() #pokazuje już nowy, przeskalowany obrazek :)
    print()
    print("Oto rozmiar przeskalowanego pliku (16:9):\n", obrazek.size) #pokazuje rozmiar obrazu
elif scale_choice == 3:
    width=1080
    height=1080  #skalowanie 16:9
    obrazek=obrazek.resize((width,height), Image.ANTIALIAS) #właściwe przeskalowanie obrazka
    type=".jpg" #nadanie formatu pliku
    obrazek.save("nowy" + type) #nadanie nazwy nowemu (przeskalowanemu) obrazkowi
    obrazek.show() #pokazuje już nowy, przeskalowany obrazek :)
    print()
    print("Oto rozmiar przeskalowanego pliku (1:1):\n", obrazek.size) #pokazuje rozmiar obrazu
elif scale_choice == 4:
    width=720
    height=1280  #skalowanie 16:9
    obrazek=obrazek.resize((width,height), Image.ANTIALIAS) #właściwe przeskalowanie obrazka
    type=".jpg" #nadanie formatu pliku
    obrazek.save("nowy" + type) #nadanie nazwy nowemu (przeskalowanemu) obrazkowi
    obrazek.show() #pokazuje już nowy, przeskalowany obrazek :)
    print()
    print("Oto rozmiar przeskalowanego pliku (9:16):\n", obrazek.size) #pokazuje rozmiar obrazu
elif scale_choice == 5:
    width=int(input("Podaj szerokość obrazu: "))
    height=int(input("Podaj wysokość obrazu: "))
    obrazek=obrazek.resize((width,height), Image.ANTIALIAS) #właściwe przeskalowanie obrazka
    type=".jpg" #nadanie formatu pliku
    obrazek.save("nowy" + type) #nadanie nazwy nowemu (przeskalowanemu) obrazkowi
    obrazek.show() #pokazuje już nowy, przeskalowany obrazek :)
    print()
    print("Oto rozmiar przeskalowanego pliku (niestandardowy):\n", obrazek.size) #pokazuje rozmiar obrazu
