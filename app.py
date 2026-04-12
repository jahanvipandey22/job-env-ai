import gradio as gr
from run import run_simulation   # 👈 import your function

def run_env(role):
    return run_simulation(role)  # 👈 direct call (NO subprocess)

iface = gr.Interface(
    fn=run_env,
    inputs=gr.Textbox(label="Enter Job Role"),
    outputs="text",
    title="🚀 Smart Job Application AI",
    description="Enter role → AI simulates job selection"
)

iface.launch(server_name="0.0.0.0", server_port=7860)