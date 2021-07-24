from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from src.SmartBookmark import evaluate, labels

app = FastAPI(
    title="Smart Bookmark",
    version="1.0",
    description="Classifies the sites into various different categories",
)


@app.get("/")
async def index():
    return {"message": "Smart Bookmark is online"}


@app.get("/list")
async def index():
    return [v for k, v in labels.items()]


class Input(BaseModel):
    data: str


@app.post("/classify")
async def get_item(input: Input):
    try:
        title, test_preds = evaluate(input.data)
        return {"title": title[0], "category": test_preds}
    except:
        return {"message": "Error"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
