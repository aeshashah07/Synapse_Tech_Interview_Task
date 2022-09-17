from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"Data": "Test"}

@app.get("/all")
def home1():
    x = requests.get('https://dog.ceo/api/breeds/list/all')
    item = x.json()
    return {"Data": list(item['message'].keys())}

@app.get('/{breed}/list/')
def sub_breed(breed: str):
    x = requests.get(f'https://dog.ceo/api/breed/{breed}/list')
    item = x.json()
    return {"Data": item['message']}

@app.get('/{breed}')
def breed_images(breed: str):
    x = requests.get(f'https://dog.ceo/api/breed/{breed}/images/random')
    item = x.json()
    return {"Datat": item["message"]}