# fastapiでラップしつつuvicorn経由でのリロードにする
poetry run uvicorn main:app --reload

# gradio 経由だと llmのメモリがうまく開放されないので使えない
# poetry run gradio run.py