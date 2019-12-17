import requests
import shutil
import simplejson as json

index = 0
apiCall = "https://api.scryfall.com/cards?page="

for i in range(1, 1500):
    print("Récupération de la page " + str(i) + "=========================================================================================")
    pageCall = apiCall + str(i)
    rCards = requests.get(pageCall)
    pageCards = rCards.text
    dataCards = json.loads(pageCards)
    for item in dataCards["data"]:
        if item["lang"] == "en":
            if item["legalities"]["modern"] == "legal":
                if "image_uris" in item:
                    print("Téléchargement de la carte \"" + str(item["name"]) + "\" d'index " + str(index))
                    imgUrl = item["image_uris"]["border_crop"]
                    fileName = "../assets/train/img" + str(index) + ".jpg"
                    img = requests.get(imgUrl, stream=True)
                    with open(fileName, "wb") as file:
                        shutil.copyfileobj(img.raw, file)
                    del img
                    index = index + 1
    del rCards
