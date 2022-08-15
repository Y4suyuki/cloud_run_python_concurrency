import time
from fastapi import FastAPI


app = FastAPI()

@app.get("/slow")
def slow():
    for i in range(15):
        print("🐍", end="", flush=True)
        time.sleep(0.1)
    print("🐌")
    return {"hello": "world"}
