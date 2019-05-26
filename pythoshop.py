from __future__ import print_function
import PIL
import os, sys
from PIL import Image
from colorama import init
from termcolor import colored
from pyfiglet import Figlet
init()

def logo(tekst):
    nazwa=Figlet(font="basic").renderText(tekst)
    print(nazwa)

logo("Pythoshop")


def menu():
    while True:
        print(colored("MENU GŁÓWNE","green"))
        print("Wyświetl opcje edytowania - naciśnij 'q'\nWyłącz program - naciśnij 'r'\n")
        wybor1 = input()
        if wybor1== 'q':
            while True:
                print("Wybierz - co chcesz zrobić:")
                print (colored("1 - zmiana kolorystyki;","magenta"), colored("2 - przeskalowanie rozmiarów;","cyan"),colored("3 - obrót obrazu;","yellow"),
                colored("4 - zapis pliku;","blue"), colored("5 - wyjdź do menu głównego\n","red"))
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
                    print(colored("\nWyjście do menu głównego\n","red"))
                    break
        elif wybor1=='r':
            print(colored("\nDziękujemy za skorzystanie z naszego programu. \nDobrego dnia! :)","green"))
            break

def color(x):
    while True:
        print("Chcesz czarno białe zdjęcie?")
        print(colored("TAK: Wciśnij: 'y'","cyan"))
        print(colored("NIE: Wciśnij 'n'","red")) #asks user if he wants b&w or colored picture
        m = input()
        if m=="y":
            im = Image.open(x).convert("L") #changes colors to black and white
        elif m=="n":
            im = Image.open(x) #changes colors to RGB
        else:
            print("Niewłaściwy klawisz! Spróbuj ponownie.\n")
            print(colored("Powrót do opcji edytowania\n","red"))
            break
        im.show()
        im.save(imageFile)
        print(colored("\nPowrót do opcji edytowania\n","red"))
        break

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
            obrazek.save(imageFile) #naming a new picture
            obrazek.show() #displays a new image
            print()
            print("Oto rozmiar przeskalowanego pliku (4:3): ", obrazek.size)
            print(colored("\nPowrót do opcji edytowania\n","red"))
            break

        elif scale_choice == 2:
            width=1280
            height=720 #scale 16:9
            obrazek=obrazek.resize((width,height), Image.ANTIALIAS)
            type=".jpg"
            obrazek.save(imageFile)
            obrazek.show()
            print()
            print("Oto rozmiar przeskalowanego pliku (16:9): ", obrazek.size)
            print(colored("\nPowrót do opcji edytowania\n","red"))
            break

        elif scale_choice == 3:
            width=1080
            height=1080 #scale 1:1
            obrazek=obrazek.resize((width,height), Image.ANTIALIAS)
            type=".jpg"
            obrazek.save(imageFile)
            obrazek.show()
            print()
            print("Oto rozmiar przeskalowanego pliku (1:1): ", obrazek.size)
            print(colored("\nPowrót do opcji edytowania\n","red"))
            break

        elif scale_choice == 4:
            width=720
            height=1280 #scale 9:16
            obrazek=obrazek.resize((width,height), Image.ANTIALIAS)
            type=".jpg"
            obrazek.save(imageFile)
            obrazek.show()
            print()
            print("Oto rozmiar przeskalowanego pliku (9:16): ", obrazek.size)
            print(colored("\nPowrót do opcji edytowania\n","red"))
            break

        elif scale_choice == 5:
            width=int(input("Podaj szerokość obrazu: "))
            height=int(input("Podaj wysokość obrazu: "))
            obrazek=obrazek.resize((width,height), Image.ANTIALIAS)
            type=".jpg"
            obrazek.save(imageFile)
            obrazek.show()
            print()
            print("Oto rozmiar przeskalowanego pliku (niestandardowy): ", obrazek.size)
            print(colored("\nPowrót do opcji edytowania\n","red"))
            break
        else:
            print("Niewłaściwy klawisz! Spróbuj ponownie.\n")
            print(colored("Powrót do opcji edytowania\n","red"))
            break


def rotate(x):
    while True:
        print(colored("O ile stopni chcesz obrócić obraz?(1 - 90 stopni; 2 - 180 stopni; 3- 270 stopni)\n","yellow"))
        m=input()
        if m=="1":
            im = Image.open(x).rotate(90) #rotates image by 90 degrees
        elif m=="2":
            im = Image.open(x).rotate(180) #rotates image by 180 degrees
        elif m=="3":
            im = Image.open(x).rotate(270) #rotates image by 270 degrees
        else:
            print(colored("Podano błędną wartość! Spróbuj ponownie.\n","red")) #user will be informed that his input was incorrect
            print(colored("Powrót do opcji edytowania\n","yellow"))     #text that will be displayed if user input was invalid
            break
        im.show() #displays rotated image
        im.save(imageFile)
        break

def save_file(x):   #x - chosen file which user wants to save
    while True:
        im = Image.open(x)
        print ("Wpisz nazwę nowego pliku.")
        new_name = input()  #user has to name new file
        extension = '.jpg'  #extension is needed to allow Python to write a file as a picture file
        new_file = new_name + extension
        im.save(new_file)       #save() is a Pillow module function
        print ("Oto nazwa nowo utworzonego pliku:", new_file)
        print()
        print(colored("Powrót do opcji edytowania\n","red"))
        break

print(colored("Witaj w Pythoshopie!\nProgram ten umożliwia Ci zmianę kolorystyki, przeskalowanie lub obrót obrazu!\n","green"))
imageFile=input("Wpisz nazwę pliku (np. zabawny_pies.jpg):\n")
obrazek=Image.open(imageFile)
print("Oto dane dotyczące wczytanego (pierwotnego) pliku: ", obrazek.format, obrazek.size, obrazek.mode)
print()
menu()
