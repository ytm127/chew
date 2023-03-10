from random import *
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import httpx
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")


origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    files = get_file_urls()

    slug = get_slug()
    return templates.TemplateResponse("index.html", {"request": request, "slug": slug})

@app.get("/bucket/{slug}")
async def slug_content(slug):
    return bucket[slug]
        
@app.get("/about", response_class=HTMLResponse)
async def about():
    return {"message": "Chew is the quick and ephemeral storage you never knew you needed."}

@app.post("/upload/")
async def upload(request: Request):
    files = get_file_urls()
    slug = get_slug()
    print("inside upload function")
    return "okay now i need to actually take the File request, not this Request request, and upload it to Linode."
    # return templates.TemplateResponse("uploaded.html", {"request": request, "slug": slug})
