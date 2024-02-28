
## 構築
poetry + poetry-plugin-dotenv 構成

## 参考
- poetry + poetry-plugin-dotenv 構成で llama-cpp-python を cuBLAS 用でビルドする方法
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

llama-cpp-pythonの入れ直し
```
poetry install
poetry run pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir
```

実行
```
poetry run python3 run.py
```
