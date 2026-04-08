from fastapi import FastAPI
from pydantic import BaseModel
from environment import JobEnv

app = FastAPI()

env = JobEnv()

class StepRequest(BaseModel):
    action: str

@app.post("/reset")
async def reset():
    state = env.reset()
    return {"state": state}

@app.post("/step")
async def step(req: StepRequest):
    state, reward, done = env.step(req.action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }