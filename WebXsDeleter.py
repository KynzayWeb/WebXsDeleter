import os
os.system('title Wait For Updating...')
os.system('title Wait For Updating. 25%')
os.system('pip install requests')
os.system('title Wait For Updating. 50%')
os.system('pip install pystyle')
os.system('title Wait For Updating. 68%')
os.system('pip install dhooks')
os.system('title Wait For Updating. 100%')
import requests
from dhooks import *
from pystyle import *
os.system('title 𝐖𝐞𝐛𝐗𝐬𝐃𝐞𝐥𝐞𝐭𝐞𝐫 By Nity Web#0666')
os.system('cls')
os.system('mode 60, 16')

print(Colorate.Horizontal(Colors.blue_to_purple , """\n
        .  .   .    .   .    ,
        |  | _ |_  _| _ | _ -+-
        |/\|(/,[_)(_](/,|(/, | 
        
""" ,1 ))
print(Colors.blue + '       https://github.com/nity-web\n' + Colors.reset)
webhooks = input(Colors.purple + '   [' + Colors.blue + '+' + Colors.purple + ']' + Colors.gray + 'URL : ')

def delete():
    requests.delete(webhooks)
    check = requests.get(webhooks)
    if check.status_code == 404:
        print("\n" + Colors.purple + "[" + Colors.blue + "logs" + Colors.purple + "]" + Colors.green + "Webhooks deleted" + Colors.reset)
        os.system("Pause >nul")
    elif check.status_code == 200:
        print("\n" + Colors.purple + "[" + Colors.blue + "logs" + Colors.purple + "]" + Colors.red + " Webhooks not deleted" + Colors.reset)
        os.system("pause >nul")

test = requests.get(webhooks)
if test.status_code == 400:
    print("\n" + Colors.purple + "[" + Colors.blue + "logs" + Colors.purple + "]" + Colors.red + "Invalid webhooks" + Colors.reset)
    os.system("pause >nul")
elif test.status_code == 200:
    print("\n" + Colors.purple + "[" + Colors.blue + "logs" + Colors.purple + "]" + Colors.green + " Valid webhooks" + Colors.reset)
    delete()