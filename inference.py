from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/")
async def infer(request: Request):
    data = await request.json()
    return {"status": "ok"}