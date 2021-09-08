import requests
r = requests.get("https://thispersondoesnotexist.com/image", headers={'User-Agent': 'My User Agent 1.0'}).content

with open("cool_person.jpeg", "wb") as f:
    f.write(r)