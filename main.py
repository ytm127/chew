from random import *
from fastapi import FastAPI

app = FastAPI()


def get_slug():
    with open('5_letter_words.txt') as f:
        lines = f.readlines()
        n1 = randint(1, 5000)
        n2 = randint(1, 5000)
        n3 = randint(1, 5000)
        return f"{lines[n1][0:5]}-{lines[n2][0:5]}"

@app.get("/")
async def root():
    slug = get_slug()
    return {"message": f"Hello World, {slug}"}

@app.get("/about")
async def about():
    return {"message": "Chew is the quick and ephemeral storage you never knew you needed."}


