from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI()

@app.get("/")

async def index():
    return {"hadi": 2102060,
            "yasin":2102030,
            "shuvo":2102021}

class Blog(BaseModel):
    title: str
    body: str
    published : Optional[bool]


@app.get("/blog")
async def show(blog: Blog):
    return {"data":f"Blog is created with title as {blog.title}",} 


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)

