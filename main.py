from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/about")
async def about():
    return {"message": "Chew is the quick and ephemeral storage you never knew you needed."}


