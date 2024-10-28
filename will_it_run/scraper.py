import requests
import platform
from rapidfuzz import fuzz

def search(name: str):
    URL_games = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
    URL_requirements = "https://store.steampowered.com/api/appdetails?appids="
    raw_data = requests.get(URL_games).json()["applist"]["apps"]
    
    # Basic linear search because I was to lazy to implement binary or smt, lol
    app_id = ""
    max_alignment = 0.5

    for app in raw_data:
        app_name = app["name"]

        alignment = (2/8 * fuzz.token_sort_ratio(name, app_name) + 2/8 * fuzz.ratio(name, app_name)
                      + 4/8 * fuzz.partial_ratio(name, app_name))
        if alignment > max_alignment:
            try:
                res = requests.get(URL_requirements + str(app["appid"])).json()

                if res[str(app["appid"])]["data"]["type"] == "game":
                    max_alignment = alignment
                    app_id = str(app["appid"])
            
                else:
                    continue
            
            except:
                continue

    response = requests.get(URL_requirements + app_id).json()

    match platform.system():
        case "Windows":
            system = "pc"

        case "Linux":
            system = "linux"

        case "MacOS":
            system = "mac"

        case _:
            return KeyError

    requirements = response[app_id]["data"][f"{system}_requirements"]
    return app_id, response[app_id]["data"]["name"], requirements

if __name__ == '__main__':
    pass
