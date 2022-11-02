import requests
import json

def PicOfTheDay():
    r = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={apikey}")
    print(r)
    load = json.loads(r.content)

    Save("picoftheday", load)

def RandomPic():
    amount = input("Enter amount of pictures: ")

    r = requests.get(f"https://api.nasa.gov/planetary/apod?count={amount}&api_key={apikey}")
    print(r)
    load = json.loads(r.content)

    for x in range(int(amount)):
        send = load[x]
        Save(f"randompic{str(x)}", send)


def Save(saveName, load):
    
    save = open(f"{saveName}.txt", "w")
    save.write(f"date: {load['date']}")
    save.write(f"\nexplanation: {load['explanation']}")
    save.close

    try:
        receive = requests.get(load["hdurl"])

        picture = open(f"{saveName}.png", 'wb')
        picture.write(receive.content)
        picture.close()

    except:
        picture = open(f"{saveName}_ot.txt", "w")
        picture.write(load["url"])
        picture.close


apikey = input("Enter API KEY: ")


RandomPic()