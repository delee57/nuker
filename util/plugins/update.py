# Hazard was proudly coded by Rdimo (https://github.com/Rdimo).
# Hazard Nuker under the GNU General Public Liscense v2 (1991).

import requests
import os
import shutil
import re
import ctypes

from tqdm import tqdm
from zipfile import ZipFile
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from colorama import Fore, Style

from util.plugins.common import *

def search_for_updates():
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    url = f"https://github.com/Rdimo/Hazard-Nuker/releases/latest"

    clear()
    setTitle("Hazard Nuker Checking For Updates. . .")
    for i in tqdm(range(100), 
                    desc="Searching for updates. . .", 
                    ascii=False, ncols=100):
                    sleep(0.003)
    r = requests.get(url, headers=header)
    clear()
    soup = str(BeautifulSoup(r.text, 'html.parser'))
    s1 = re.search('<title>', soup)
    s2 = re.search('·', soup)
    result_string = soup[s1.end():s2.start()]
    if THIS_VERSION not in result_string:
        setTitle("Hazard Nuker New Update Found!")
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + f'''
                ███╗   ██╗███████╗██╗    ██╗    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██╗
                ████╗  ██║██╔════╝██║    ██║    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
                ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██║
                ██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ╚═╝
                ██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██╗
                ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝
                              {Fore.LIGHTRED_EX}Looks like this Hazard Nuker {THIS_VERSION} is outdated '''.replace('█', f'{Fore.WHITE}█{Fore.RED}'), end="\n\n")
        choice = str(input(
            f'{Fore.GREEN}[{Fore.YELLOW}>>>{Fore.GREEN}] {Fore.RESET}You want to update to the latest version? (Y to update): {Fore.LIGHTRED_EX}'))

        if choice.upper() == 'Y':
            print(f"{Fore.WHITE}\nUpdating. . .{Fore.RESET}")
            setTitle(f'Hazard Nuker Updating...')
            try:
                new_version = requests.get("https://github.com/Rdimo/Hazard-Nuker/releases/download/v1.3.0/HazardNuker.zip")
                with open("HazardNuker.zip", 'wb')as zipfile:
                    zipfile.write(new_version.content)
                with ZipFile("HazardNuker.zip", 'r') as filezip:
                    filezip.extractall()
                os.remove("HazardNuker.zip")
                shutil.copyfile(os.getcwd()+'\\Hazard-Nuker-master\\Changelog.md', 'Changelog.md')
                shutil.copyfile(os.getcwd()+'\\Hazard-Nuker-master\\HazardNuker.exe', 'HazardNuker.exe')
                shutil.copyfile(os.getcwd()+'\\Hazard-Nuker-master\\README.md', 'README.md')
                shutil.rmtree('Hazard-Nuker-master')
                setTitle('Hazard Nuker Update Complete!')
                print(f"{Fore.GREEN}Update Successfully Finished!{Fore.RESET}")
                os.startfile("HazardNuker.exe")
                os._exit(0)
            except Exception as err:
                clear()
                print(f"{Fore.LIGHTRED_EX}{err}")
                ctypes.windll.user32.MessageBoxW(0, f"Oh no! An error occured while Updating Hazard Nuker-{THIS_VERSION}\n\nIf this keeps occuring try and download it manually here github.com/Rdimo/Hazard-Nuker\n\n\"{err}\"","ERROR", 0x0 | 0x10)
        else:
            input
            return