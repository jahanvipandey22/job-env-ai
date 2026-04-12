from fastapi import FastAPI, Body
from environment import JobEnv
import gradio as gr

app = FastAPI()
env = JobEnv()


@app.get("/")
def home():
    return {"message": "API running"}


# ✅ REQUIRED ENDPOINT
@app.post("/openenv/reset")
def reset():
    state = env.reset()
    return {"state": state}


# ✅ REQUIRED ENDPOINT
@app.post("/openenv/step")
def step(action: dict = Body(...)):
    act = action.get("action", "learn_skill")
    state, reward, done = env.step(act)

    return {
        "state": state,
        "reward": float(reward),
        "done": bool(done)
    }


# ✅ GRADIO (keeps space alive)
def dummy():
    return "API running"

iface = gr.Interface(fn=dummy, inputs=[], outputs="text")


# 🔥 SINGLE ENTRY POINT ONLY
if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860)