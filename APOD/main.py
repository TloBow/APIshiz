import requests
import json

def PicOfTheDay():
    r = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={apikey}")
    print(r)
    load = json.loads(r.content)

    try:
        receive = requests.get(load["hdurl"])

        picture = open('picoftheday.png', 'wb')
        picture.write(receive.content)
        picture.close()

    except:
        picture = open("picoftheday_os.txt", "w")
        picture.write(load["url"])
        picture.close

    explanation = open("picoftheday.txt", "w")
    explanation.write(f"date: {load['date']}")
    explanation.write(f"\nexplanation: {load['explanation']}")
    explanation.close

def RandomPic():
    amount = input("Enter amount of pictures: ")

    r = requests.get(f"https://api.nasa.gov/planetary/apod?count={amount}&api_key={apikey}")
    print(r)
    load = json.loads(r.content)

    for x in range(int(amount)):
        recpic = requests.get(load[x]['hdurl'])

        picture = open(f"randompic{str(x)}.png", "wb")
        picture.write(recpic.content)
        picture.close()

        explanation = open(f"randompic{str(x)}.txt", "w")
        explanation.write(f"date: {load[x]['date']}")
        explanation.write(f"\nexplanation: {load[x]['explanation']}")
        explanation.close()



apikey = input("Enter API KEY: ")


RandomPic()