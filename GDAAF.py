import os
import subprocess

print(r"""
  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$$        /$$$$$$       /$$  
 /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$| $$_____/       /$$$_  $$    /$$$$  
| $$  \__/| $$  \ $$| $$  \ $$| $$  \ $$| $$            | $$$$\ $$   |_  $$  
| $$ /$$$$| $$  | $$| $$$$$$$$| $$$$$$$$| $$$$$         | $$ $$ $$     | $$  
| $$|_  $$| $$  | $$| $$__  $$| $$__  $$| $$__/         | $$\ $$$$     | $$  
| $$  \ $$| $$  | $$| $$  | $$| $$  | $$| $$            | $$ \ $$$     | $$  
|  $$$$$$/| $$$$$$$/| $$  | $$| $$  | $$| $$            |  $$$$$$//$$ /$$$$$$
 \______/ |_______/ |__/  |__/|__/  |__/|__/             \______/|__/|______/
""")
dir = os.listdir()
print("файлы в папке:  ")
print (dir)
print("выбери нужную функцию")
vubor = int(input("1 (файл): распаковать, 2 (файл(бинарный)(пока в разработке может сохранять только main и список всех функций)): задекомпилировать с последующим выводом в файл), 3 (файл.gmd): задекомпилировать уровень в txt, 4 распаковать .geode файл:  "))
file = input("скажи точное название файла:  ")
if vubor == 1:
    dir = (f"unz_{file}")
    mkdir = os.system(f"mkdir {dir}")
    os.system(f"mv {file} {dir}")
    os.chdir(dir)
    os.system(f"unzip {file}")
    print("готово: ")
elif vubor == 2:
    dirrd = (f"de{file}")
    os.system(f"mkdir {dirrd}")
    os.system(f"mv {file} {dirrd}")
    os.chdir(dirrd)
    os.system(f"r2 -q -c 'aaa; afl' {file} > funcal.txt")
    os.system(f"r2 -q -c 'aaa; pD' {file} > alfncdism.txt")
    print("переиминуйте ваш txt: alfncdism.txt в файл с расширением .ans для просмотра используйте asprnt.py  ")
elif vubor == 3:
    print("в разработке сорр:(  ")
elif vubor ==4:
    dirr = (f"gunz_{file}")
    os.system(f"mkdir gunz_{file}")
    os.system(f"mv {file} {file}.zip")
    os.system(f"mv {file}.zip {dirr}")
    os.chdir(dirr)
    os.system(f"unzip {file}.zip")
else:
    print("пожайлуста введите правильный выбор  ")

