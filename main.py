from random import *
from fastapi import FastAPI
import httpx

app = FastAPI()

####################### helpers ########################

def get_slug():
    """
    Returns a string/slug that is a concatenation of 2 5-letter words. 
    """
    with open('5_letter_words.txt') as f:
        lines = f.readlines()
        n1 = randint(1, 5000)
        n2 = randint(1, 5000)
        n3 = randint(1, 5000)
        return f"{lines[n1][0:5]}-{lines[n2][0:5]}"

def get_file_urls():
    # r = httpx.get("https://api.linode.com/v4/object-storage/buckets/us-east-1/chew-files/object-list")
    #url = "https://api.linode.com/v4/object-storage/buckets/us-east-1/chew-files/object-url"
    #r = httpx.post(url)
    
    return [
        "https://chew-files.us-east-1.linodeobjects.com/ww.txt",
        "https://chew-files.us-east-1.linodeobjects.com/invoice.pdf"
    ]

bucket = {
    "dorky-slobs": [
          "https://chew-files.us-east-1.linodeobjects.com/ww.txt",
          "https://chew-files.us-east-1.linodeobjects.com/invoice.pdf"
    ],
    "test-test": ["https://chew-files.us-east-1.linodeobjects.com/output001.txt"]
}

##################### routes #########################

@app.get("/")
async def root():
    files = get_file_urls()

    slug = get_slug()
    return {"message": f"Hello World, {slug}"}

@app.get("/bubbles/{slug}")
async def slug_content(slug):
    return bucket[slug]
        
@app.get("/about")
async def about():
    return {"message": "Chew is the quick and ephemeral storage you never knew you needed."}


