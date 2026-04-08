from fastapi import FastAPI
from environment import JobEnv

app = FastAPI()

env = JobEnv()

# ✅ REQUIRED: RESET endpoint
@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state}

# ✅ REQUIRED: STEP endpoint
@app.post("/step")
def step(action: dict):
    act = action.get("action", "learn_skill")

    state, reward, done = env.step(act)

    return {
        "state": state,
        "reward": reward,
        "done": done
    }