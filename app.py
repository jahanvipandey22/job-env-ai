from fastapi import FastAPI, Body
from environment import JobEnv

app = FastAPI()
env = JobEnv()


@app.get("/")
def home():
    return {"message": "API running"}


# ✅ STRICT POST ONLY
@app.post("/openenv/reset")
def reset():
    state = env.reset()
    return {
        "state": state
    }


# ✅ SAFE + FLEXIBLE INPUT HANDLING
@app.post("/openenv/step")
def step(action: dict = Body(...)):
    act = action.get("action", "learn_skill")

    state, reward, done = env.step(act)

    return {
        "state": state,
        "reward": float(reward),
        "done": bool(done)
    }