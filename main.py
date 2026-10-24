import gradio as gr

gr.close_all()

def greet(name):
    return f"Welcome, {name}! Have a great day."

demo = gr.Interface(
    fn=greet,
    inputs=[gr.Textbox(label="Enter Your Name")],
    outputs=[gr.Textbox(label="Greeting Message")],
    title="Personal Greeting App",
    description="Enter your name to get a personalized welcome message."
)

demo.launch()
