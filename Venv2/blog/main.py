from fastapi import FastAPI

app = FastAPI()

@app.post("/")
async def create(title, body):
    return {"title ":title,"body":body}