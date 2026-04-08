import gradio as gr
import subprocess

def run_env(role):
    result = subprocess.run(
        ["python", "run.py", role],
        capture_output=True,
        text=True
    )
    return result.stdout + result.stderr

gr.Interface(
    fn=run_env,
    inputs=gr.Textbox(label="Enter Job Role"),
    outputs="text",
    title="🚀 Smart Job Application AI",
    description="Enter role → AI simulates job selection"
).launch()