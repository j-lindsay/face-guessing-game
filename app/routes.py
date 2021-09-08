from app import app
from flask import render_template, request, jsonify

import requests
import random

def get_fake_image_url():
    r = requests.get("https://thispersondoesnotexist.com/image", headers={'User-Agent': 'My User Agent 1.0'}).content
    prefix = str(random.randrange(1, 10000))
    filename = prefix + '.jpeg'

    with open("S:/face-guessing-game/app/static/" + filename, "wb") as f:
        f.write(r)

    return '../static/' + filename

def get_real_image_url():
    prefix = str(random.randrange(69800, 70000))
    filename = prefix + '.png'
    return filename


@app.route('/')
def index():
    fake_img_url = get_fake_image_url()
    real_img_url = "../static/images/" + get_real_image_url()

    data = [
        {
            "id": 1,
            "img_url": fake_img_url,
            "real": 1
        }, 
        {
            "id": 2,
            "img_url": real_img_url,
            "real": 2
        }
    ]
    random.shuffle(data)
    return render_template('index.html', data=data)

@app.route('/index')
def get_data():
    fake_img_url = get_fake_image_url()
    real_img_url = "../static/images/" + get_real_image_url()

    data = [
        {
            "id": 1,
            "img_url": fake_img_url,
            "real": 1
        }, 
        {
            "id": 2,
            "img_url": real_img_url,
            "real": 2
        }
    ]
    random.shuffle(data)
    return jsonify(data)