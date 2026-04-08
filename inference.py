from fastapi import FastAPI
from environment import JobEnv

app = FastAPI()

env = JobEnv()

@app.post("/openenv/reset")
def reset():
    state = env.reset()
    return {"state": state}

@app.post("/openenv/step")
def step(action: dict):
    act = action.get("action", "learn_skill")

    state, reward, done = env.step(act)

    return {
        "state": state,
        "reward": reward,
        "done": done
    }