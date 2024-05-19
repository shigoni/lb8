import requests
from PIL import Image, ImageDraw, ImageFont
import os
from io import BytesIO

photo = requests.get(
    "https://bronk.club/uploads/posts/2023-02/1676393947_bronk-club-p-otkritki-bez-teksta-krasivo-19.jpg"
)


def number_1():
    img = Image.open(BytesIO(photo.content))
    crop_photo = img.crop((700, 500, 3050, 2000))
    crop_photo.save("photo_crop.jpg")


def number_2():
    photo = {
        "Новый год": "https://img.redzhina.ru/img/5c/b9/5cb9945bbc86e1af4b763edae85db3d8.jpg",
        "День рождения": "https://gas-kvas.com/uploads/posts/2023-01/1674122055_gas-kvas-com-p-pozdravitelnaya-otkritka-s-dnem-rozhdeniya-16.jpg",
    }

    def photo_open(photo_url):
        response = requests.get(photo_url)
        img = Image.open(BytesIO(response.content))
        img.show()

    print("Праздники:", ", ".join(photo.keys()))

    photo_number = input("Введите название праздника, для получения открытки: ")
    if photo_number in photo:
        photo_open(photo[photo_number])
    else:
        print("\033[1m" + "Такого праздника нет!" + "\033[0m")


def number_3():
    name = input("Введите имя: ") + ", поздравляю!"

    img = Image.open(BytesIO(photo.content))
    crop_photo = img.crop((100, 100, 3450, 2400))

    draw = ImageDraw.Draw(crop_photo)
    font = ImageFont.truetype("arialbd.ttf", 200)
    draw.text((600, 1000), name, font=font, fill="red")

    crop_photo.save("happy.png")


while True:
    number = int(input("Введите номер задания: "))

    if number == 1:
        number_1()
    elif number == 2:
        number_2()
    elif number == 3:
        number_3()
    else:
        print("Такого задания нет")
