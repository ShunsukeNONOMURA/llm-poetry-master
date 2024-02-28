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
current_model_path = "./models/ELYZA-japanese-Llama-2-7b-fast-instruct-q8_0.gguf"

llm = Llama(
    model_path=current_model_path,
    n_gpu_layers = 40,
    verbose = True,
)


message_history = []
def clear_message_history():
    print('on clear')
    message_history = []

def chat(user_msg):
    message_history.append({
        "role": "user",
        "content": user_msg
    })
    assistant_msg = user_msg

    prompt = f"""
    [INST] {user_msg} [/INST]
    """
    # prompt = user_msg
    output = llm(
        prompt,
        temperature=0.1,
        max_tokens=DEFAULT_MAX_TOKENS,
        # stream=True,
    )
    # print(output['choices'][0]['text'])
    pprint(output['choices'])
    message_history.append({
        "role": "assistant",
        "content": output['choices'][0]['text'],
    })
    return [(message_history[i]["content"], message_history[i+1]["content"]) for i in range(0, len(message_history)-1, 2)]

with gr.Blocks() as demo:
    title = gr.Markdown("# nonoshun ui tool")
    gr.Markdown(f"model = {current_model_path}")
    title_llm = 'llm'
    with gr.Tab(title_llm):
        subtitle_hitomi = gr.Markdown(f"## {title_llm}")
        chatbot = gr.Chatbot()
        input = gr.Textbox(show_label=False, placeholder="メッセージを入力") ##.style(container=False)
        input.submit(fn=chat, inputs=input, outputs=chatbot) # メッセージ送信されたら、AIと会話してチャット欄に全会話内容を表示
        input.submit(fn=lambda: "", inputs=None, outputs=input) # （上記に加えて）入力欄をクリア
        
        # btn_clear = gr.Button()
        # btn_clear.click(fn=clear_message_history)
        # inp_hitomi = gr.Interface(
        #     fn=chat,
        #     inputs= gr.Textbox(),
        #     outputs = gr.Textbox(),
        #     allow_flagging='never'
        # )
        

if __name__ == "__main__":
    demo.launch(
        server_port = 27860
    )