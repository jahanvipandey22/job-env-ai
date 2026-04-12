
from fastapi import FastAPI, Body
import gradio as gr
from environment import JobEnv
from run import run_simulation

app = FastAPI()
env = JobEnv()

@app.post("/openenv/reset")
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

def run_env(role):
    return run_simulation(role)

iface = gr.Interface(
    fn=run_env,
    inputs=gr.Textbox(),
    outputs="text"
)

# 🔥 FIXED HERE
app = gr.mount_gradio_app(app, iface, path="/ui")