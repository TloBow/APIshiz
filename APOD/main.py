from random import Random
import requests
import json

def PicOfTheDay():
    r = requests.get("https://api.nasa.gov/planetary/apod?api_key=NIFH1JyVc1eMgvFxXShtJkGWgPAMFFjoCKJpcDmB")
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
    explanation.write("date: " + load['date'])
    explanation.write("\nexplanation: " + load['explanation'])
    explanation.close

def RandomPic():
    amount_str = input("Enter amount of pictures: ")
    amount_int = int(amount_str)

    r = requests.get("https://api.nasa.gov/planetary/apod?count=" + amount_str + "&api_key=NIFH1JyVc1eMgvFxXShtJkGWgPAMFFjoCKJpcDmB")
    print(r)
    load = json.loads(r.content)

    for x in range(amount_int):
        recpic = requests.get(load[x]['hdurl'])

        number = str(x)

        picture = open("randompic" + number + ".png", "wb")
        picture.write(recpic.content)
        picture.close()

        explanation = open("randompic" + number + ".txt", "w")
        explanation.write("date: " + load[x]['date'])
        explanation.write("\nexplanation: " + load[x]['explanation'])
        explanation.close()



PicOfTheDay()