from llama_cpp import Llama

DEFAULT_MAX_TOKENS = -1 # -1 = infinity

current_model_path = "./models/ELYZA-japanese-Llama-2-7b-fast-instruct-q8_0.gguf"
llm = Llama(
    model_path=current_model_path,
    n_gpu_layers = 40,
    verbose = True,
)

# user_msg = 'こんにちは'
# user_msg = 'アメリカの良いところについて３つ挙げて、それぞれについて詳しく説明しなさい。'
user_msg = 'アメリカの大統領について教えて'

prompt = f"""
[INST] {user_msg} [/INST]
"""
print(f'input : {prompt}')

stream = llm(
    prompt,
    temperature=0.1,
    max_tokens=DEFAULT_MAX_TOKENS,
    stream=True,
)

# print(output)

result = ''
for output in stream:
    print('s')
    print(output)
    result += output['choices'][0]['text']
    print(result)
print (result)
# print(output['choices'][0]['text'])

exit(0)

