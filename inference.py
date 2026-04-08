from fastapi import FastAPI, Request
from environment import JobEnv

app = FastAPI()

env = JobEnv()

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/")
async def infer(request: Request):
    data = await request.json()

    action = data.get("action", "learn_skill")

    state, reward, done = env.step(action)

    return {
        "state": state,
        "reward": reward,
        "done": done
    }