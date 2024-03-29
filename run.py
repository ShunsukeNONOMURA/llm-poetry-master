import gradio as gr

from pprint import pprint

# from app import *

from pathlib import Path
import os
import platform
import sys
import subprocess as sp
import shutil

from llama_cpp import Llama

DEFAULT_MAX_TOKENS = -1 # -1 = infinity
# current_model_path = "./models/ELYZA-japanese-Llama-2-7b-fast-instruct-q8_0.gguf"
current_model_path = "./models/ELYZA-japanese-Llama-2-13b-fast-instruct-q8_0.gguf"

llama = Llama(
    model_path=current_model_path,
    n_gpu_layers = -1,
    verbose = False,
)

def predict(message, history):
    messages = []
    for human_content, system_content in history:
        message_human = {
            "role":"user",
            "content": human_content+"\n",
        }
        message_system = {
            "role":"system",
            "content": system_content+"\n",
        }
        messages.append(message_human)
        messages.append(message_system)
    message_human = {
        "role":"user",
        "content":message+"\n",
    }
    messages.append(message_human)
    # Llama2回答
    streamer = llama.create_chat_completion(messages, stream=True)

    partial_message = ""
    for msg in streamer:
        message = msg['choices'][0]['delta']
        if 'content' in message:
            partial_message += message['content']
            yield partial_message

with gr.ChatInterface(predict).queue() as demo:
    # gr.ChatInterface(predict).queue()
    pass

if __name__ == "__main__":
    demo.launch(
        server_port = 27860,
        share=True
    )