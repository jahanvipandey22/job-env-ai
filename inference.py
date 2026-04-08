from fastapi import FastAPI
from environment import JobEnv

app = FastAPI()

env = JobEnv()

@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state}

@app.post("/step")
def step(action: str):
    state, reward, done = env.step(action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }