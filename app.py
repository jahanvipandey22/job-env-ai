from fastapi import FastAPI, Body
from environment import JobEnv
import uvicorn

app = FastAPI()
env = JobEnv()


@app.get("/")
def home():
    return {"message": "API running"}


@app.post("/openenv/reset")
def reset():
    state = env.reset()
    return {"state": state}


@app.post("/openenv/step")
def step(action: dict = Body(...)):
    act = action.get("action", "learn_skill")
    state, reward, done = env.step(act)

    return {
        "state": state,
        "reward": float(reward),
        "done": bool(done)
    }


# 🔥 VERY IMPORTANT (keeps server running)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
    import gradio as gr

def dummy():
    return "API running"

iface = gr.Interface(fn=dummy, inputs=[], outputs="text")

if __name__ == "__main__":
    iface.launch()