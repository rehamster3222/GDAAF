print(r"""
  /$$$$$$  /$$$$$$$   /$$$$$$         /$$$$$$       /$$  
 /$$__  $$| $$__  $$ /$$__  $$       /$$$_  $$    /$$$$  
| $$  \ $$| $$  \ $$| $$  \__/      | $$$$\ $$   |_  $$  
| $$$$$$$$| $$$$$$$/|  $$$$$$       | $$ $$ $$     | $$  
| $$__  $$| $$____/  \____  $$      | $$\ $$$$     | $$  
| $$  | $$| $$       /$$  \ $$      | $$ \ $$$     | $$  
| $$  | $$| $$      |  $$$$$$/      |  $$$$$$//$$ /$$$$$$
|__/  |__/|__/       \______/        \______/|__/|______/
""")                                               
                                                         
                                                         
import ansiconv
import glob
import os

lst = glob.glob("**/*.ans", recursive=True)
print(lst)
dir = input("введи полную дирректорию нужного файла которую выдало:  ")
if not lst:
    print("файлы не найдены:  ")
else:
    with open(dir, 'rb') as file:
        content = file.read()
        print("сделано:  ")
        c = content.decode('utf-8', errors='ignore')
        res = ansiconv.to_plain(c)
        print(res)
