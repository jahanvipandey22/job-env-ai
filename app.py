from fastapi import FastAPI, Body
import gradio as gr
from environment import JobEnv
from run import run_simulation

app = FastAPI()

env = JobEnv()

# ✅ REQUIRED API
@app.post("/openenv/reset")
def reset():
    return env.reset()

@app.post("/openenv/step")
def step(action: dict = Body(default={})):
    act = action.get("action", "learn_skill")
    state, reward, done = env.step(act)

    return {
        "state": state,
        "reward": reward,
        "done": done
    }

# ✅ Gradio UI
def run_env(role):
    return run_simulation(role)

iface = gr.Interface(
    fn=run_env,
    inputs=gr.Textbox(label="Enter Job Role"),
    outputs="text",
    title="🚀 Smart Job Application AI",
    description="Enter role → AI simulates job selection"
)

app = gr.mount_gradio_app(app, iface, path="/")