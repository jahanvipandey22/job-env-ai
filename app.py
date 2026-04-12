from fastapi import FastAPI, Body
from environment import JobEnv

app = FastAPI()
env = JobEnv()

@app.get("/")
def home():
    return {"message": "API running"}

@app.api_route("/openenv/reset", methods=["GET", "POST"])
def reset():
    return env.reset()

@app.api_route("/openenv/step", methods=["POST"])
def step(action: dict = Body(...)):
    act = action.get("action", "learn_skill")
    state, reward, done = env.step(act)

    return {
        "state": state,
        "reward": reward,
        "done": done
    }