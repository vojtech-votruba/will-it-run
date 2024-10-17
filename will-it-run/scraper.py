import requests
import platform
from difflib import SequenceMatcher

def search(name: str):
    name = name.lower()

    URL_games = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
    raw_data = requests.get(URL_games).json()["applist"]["apps"]
    
    # Basic linear search because I was to lazy to implement binary, lol
    app_id = ""
    max_alignment = 0

    for app in raw_data:
        alignment = SequenceMatcher(None, name, app["name"].lower()).ratio() 
        if alignment > max_alignment:
            max_alignment = alignment
            app_id = str(app["appid"])

    URL_requirements = "https://store.steampowered.com/api/appdetails?appids="
    res = requests.get(URL_requirements + app_id).json()

    if not res[app_id]["success"]:
        print("error")
        return None

    match platform.system():
        case "Windows":
            system = "pc"

        case "Linux":
            system = "linux"

        case "MacOS":
            system = "mac"

        case _:
            return KeyError


    requirements = res[app_id]["data"][f"{system}_requirements"]
    return requirements

if __name__ == '__main__':
    search("aa")
