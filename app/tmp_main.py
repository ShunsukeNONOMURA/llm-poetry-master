# from logging import getLogger
from pathlib import Path
from fastapi import FastAPI
import gradio as gr
# from llama_cpp import Llama

# logger = getLogger("uvicorn.app")

DEFAULT_MAX_TOKENS = -1 # -1 = infinity
# current_model_path = "./models/ELYZA-japanese-Llama-2-7b-fast-instruct-q8_0.gguf"

LLM_MODEL_PATH_ROOT = './models'

llm_model_paths = []

# def predict(message, history):
#     messages = []
#     for human_content, system_content in history:
#         message_human = {
#             "role":"user",
#             "content": human_content+"\n",
#         }
#         message_system = {
#             "role":"system",
#             "content": system_content+"\n",
#         }
#         messages.append(message_human)
#         messages.append(message_system)
#     message_human = {
#         "role":"user",
#         "content":message+"\n",
#     }
#     messages.append(message_human)
#     # Llama2回答
#     streamer = llama.create_chat_completion(messages, stream=True)

#     partial_message = ""
#     for msg in streamer:
#         message = msg['choices'][0]['delta']
#         if 'content' in message:
#             partial_message += message['content']
#             yield partial_message

def create_interface():
    with gr.Blocks() as demo:
        title = gr.Markdown("# nonoshun ui tool")

        # gr.Dropdown(
        #     choices= llm_model_paths,
        #     # value = 1,
        # )

        # with gr.Tab("chat"):
        #     gr.ChatInterface(predict).queue()
    return demo


# demo = create_interface()
app = FastAPI()

@app.get("/health")
async def hello():
    return {"message": "ok"}


# app = gr.mount_gradio_app(app, demo, path="/")

