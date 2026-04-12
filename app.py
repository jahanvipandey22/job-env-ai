from fastapi import FastAPI, Body
from environment import JobEnv

app = FastAPI()
env = JobEnv()

@app.get("/")
def home():
    return {"message": "API running"}

# Allow both GET and POST (checker can be inconsistent)
@app.api_route("/openenv/reset", methods=["GET", "POST"])
def reset():
    return env.reset()

@app.post("/openenv/step")
def step(action: dict = Body(...)):
    act = action.get("action", "learn_skill")
    state, reward, done = env.step(act)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }