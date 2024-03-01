# 詰まったところ履歴

## llama-cpp-python で cuBLAS = １ にならない
- CMAKE_ARGSの環境変数をcuBLASが有効になるように設定する
- poetry + poetry-plugin-dotenv 構成としてpoetryの中で環境変数を設定する
- 参考：poetry + poetry-plugin-dotenv 構成で llama-cpp-python を cuBLAS 用でビルドする方法
    - https://stackoverflow.com/questions/77534091/how-can-i-install-llama-cpp-python-with-cublas-using-poetry
    - https://github.com/volopivoshenko/poetry-plugin-dotenv/


.envを認識するプラグイン追加
```
poetry self add poetry-plugin-dotenv
```

.env作成
```
CMAKE_ARGS="-DLLAMA_CUBLAS=on"
```

.env有効化確認
```
$ ~/llm_poetry$ poetry run python3
Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> print(f"CMAKE_ARGS: {os.environ['CMAKE_ARGS']!r}")
CMAKE_ARGS: '-DLLAMA_CUBLAS=on'
```

llama-cpp-pythonを上書きで入れる
```
poetry install
poetry run pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir
```

## gradioだとリロード時にうまくgpuメモリが開放されない
- uvicorn経由だとリロード時にうまくGPUメモリ開放される模様。
- FastAPIでラップしてgradio利用する構成にする。
    - [LLM_RAG_Model_Deployment](https://github.com/aritrasen87/LLM_RAG_Model_Deployment/tree/main)