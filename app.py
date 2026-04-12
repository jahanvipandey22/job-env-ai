
from fastapi import FastAPI, Body
import gradio as gr
from environment import JobEnv
from run import run_simulation

app = FastAPI()
env = JobEnv()

# ✅ REQUIRED API ROUTES
@app.api_route("/openenv/reset", methods=["GET", "POST"])
def reset():
    return env.reset()

@app.api_route("/openenv/step", methods=["POST"])
def step(action: dict = Body(...)):
    act = action.get("action", "learn_skill")
    state, reward, done = env.step(act)
    return {"state": state, "reward": reward, "done": done}


# ✅ GRADIO UI (separate, safe)
def run_env(role):
    return run_simulation(role)

iface = gr.Interface(
    fn=run_env,
    inputs=gr.Textbox(label="Enter role"),
    outputs="text"
)

# ⚠️ IMPORTANT: mount AFTER routes
app = gr.mount_gradio_app(app, iface, path="/ui")


# ✅ HEALTH CHECK (VERY IMPORTANT FOR SCALER)
@app.get("/")
def home():
    return {"message": "API is running"}