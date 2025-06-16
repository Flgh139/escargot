from fastapi import FastAPI
from escargot import Escargot

app = FastAPI()

config = {
    # 根據你的 API 金鑰與 DB 連線補上
    "azuregpt35-16k": {
        "api_key": "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",
        "model_id": "gpt-3.5-turbo",
        "api_base": "https://api.openai.com/v1"
    }
}

es = Escargot(config, model_name="azuregpt35-16k")

@app.post("/ask")
def ask(prompt: str):
    return es.run(prompt)
