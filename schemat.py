from __future__ import print_function
import PIL
import os, sys
from PIL import Image

def menu():
    while True:
        print("Wybierz - co chcesz zrobić:")
        print("1 - zmiana kolorystyki; 2 - przeskalowanie rozmiarów; 3 - obrót obrazu; 4 - zapis pliku; 5 - zakończ działanie programu\n")
        opcja=int(input("Odpowiedź:"))
        if opcja==1:
            x=imageFile
            color(x)
        elif opcja==2:
            choice()
            scale(obrazek)
        elif opcja==3:
            x=imageFile
            rotate(x)
        elif opcja==4:
            picture=imageFile
            save_file(picture)
        elif opcja==5:
            print("Dziękujemy za skorzystanie z naszego programu :)")
            break

def color(x):
    while True:
        print("Chcesz czarno białe zdjęcie?(y/n)") #asks user if he wants b&w or colored picture
        m = input()
        if m=="y":
            im = Image.open(x).convert("L") #changes colors to black and white
        else:
            im = Image.open(x) #changes colors to RGB
        im.show()
        if input("Chcesz zakończyć działanie programu - 'Q', czy dokonać wyboru innej opcji -'R'? ")=='Q':
            print("Dzięki za skorzystanie z naszego programu!")
            break
        else:
            print()
            menu()

def choice():
    print("Do jakiego formatu chcesz przeskalować swój obrazek: 1 - 4:3, 2 - 16:9, 3 - 1:1, 4 - 9:16, 5 - niestandardowy.\n")

def scale(obrazek):
    scale_choice=int(input("Wybierz skale: "))
    while True:
        if scale_choice == 1:
            width=640
            height=480 #scale 4:3
            obrazek=obrazek.resize((width,height), Image.ANTIALIAS) #proper scaling of an image
            type=".jpg" #a file format
            obrazek.save("nowy" + type) #naming a new picture
            obrazek.show() #displays a new image
            print()
            print("Oto rozmiar przeskalowanego pliku (4:3): ", obrazek.size)
            if input("Chcesz zakończyć działanie programu - 'Q', czy dokonać wyboru innej opcji -'R'? ")=='Q':
                print("Dzięki za skorzystanie z naszego programu!")
                break
            else:
                print()
                menu()
        elif scale_choice == 2:
            width=1280
            height=720 #scale 16:9
            obrazek=obrazek.resize((width,height), Image.ANTIALIAS)
            type=".jpg"
            obrazek.save("nowy" + type)
            obrazek.show()
            print()
            print("Oto rozmiar przeskalowanego pliku (16:9): ", obrazek.size)
            if input("Chcesz zakończyć działanie programu - 'Q', czy dokonać wyboru innej opcji -'R'? ")=='Q':
                print("Dzięki za skorzystanie z naszego programu!")
                break
            else:
                print()
                menu()
        elif scale_choice == 3:
            width=1080
            height=1080 #scale 1:1
            obrazek=obrazek.resize((width,height), Image.ANTIALIAS)
            type=".jpg"
            obrazek.save("nowy" + type)
            obrazek.show()
            print()
            print("Oto rozmiar przeskalowanego pliku (1:1): ", obrazek.size)
            if input("Chcesz zakończyć działanie programu - 'Q', czy dokonać wyboru innej opcji -'R'? ")=='Q':
                print("Dzięki za skorzystanie z naszego programu!")
                break
            else:
                print()
                menu()
        elif scale_choice == 4:
            width=720
            height=1280 #scale 9:16
            obrazek=obrazek.resize((width,height), Image.ANTIALIAS)
            type=".jpg"
            obrazek.save("nowy" + type)
            obrazek.show()
            print()
            print("Oto rozmiar przeskalowanego pliku (9:16): ", obrazek.size)
            if input("Chcesz zakończyć działanie programu - 'Q', czy dokonać wyboru innej opcji -'R'? ")=='Q':
                print("Dzięki za skorzystanie z naszego programu!")
                break
            else:
                print()
                menu()
        elif scale_choice == 5:
            width=int(input("Podaj szerokość obrazu: "))
            height=int(input("Podaj wysokość obrazu: "))
            obrazek=obrazek.resize((width,height), Image.ANTIALIAS)
            type=".jpg"
            obrazek.save("nowy" + type)
            obrazek.show()
            print()
            print("Oto rozmiar przeskalowanego pliku (niestandardowy): ", obrazek.size)
            if input("Chcesz zakończyć działanie programu - 'Q', czy dokonać wyboru innej opcji -'R'? ")=='Q':
                print("Dzięki za skorzystanie z naszego programu!")
                break
            else:
                print()
                menu()

def rotate(x):
    while True:
        print("O ile stopni chcesz obrócić obraz?(90,180,270)")
        m=input()
        if m=="90":
            im = Image.open(x).rotate(90) #rotates image by 90 degrees
        elif m=="180":
            im = Image.open(x).rotate(180) #rotates image by 180 degrees
        elif m=="270":
            im = Image.open(x).rotate(270) #rotates image by 270 degrees
        else:
            print("Podano błędną wartość ") #text that will be displayed if user input was invalid
        im.show() #displays rotated image
        if input("Chcesz zakończyć działanie programu - 'Q', czy dokonać wyboru innej opcji -'R'? ")=='Q':
            print("Dzięki za skorzystanie z naszego programu!")
            break
        else:
            print()
            menu()

def save_file(x):   #x - chosen file which user wants to save
    while True:
        im = Image.open(x)
        print ("Wpisz nazwę nowego pliku")
        new_name = input()  #user has to name new file
        extension = '.jpg'  #extension is needed to allow Python to write a file as a picture file
        new_file = new_name + extension
        save_new_file = im.save(new_file)   #save() is a Pillow module function
        print ("Oto nazwa nowo utworzonego pliku:", new_file)
        return save_new_file
        print()
        if input("Chcesz zakończyć działanie programu - 'Q', czy dokonać wyboru innej opcji -'R'? ")=='Q':
            print("Dzięki za skorzystanie z naszego programu!")
            break
        else:
            print()
            menu()

print("Witaj w Pythoshopie! Program ten umożliwia Ci zmianę kolorystyki, przeskalowanie lub obrót obrazu!\n")
imageFile=input("Wpisz nazwę pliku (np. zabawny_pies.jpg):\n")
obrazek=Image.open(imageFile)
print("Oto dane dotyczące wczytanego (pierwotnego) pliku: ", obrazek.format, obrazek.size, obrazek.mode)
print()
menu()
