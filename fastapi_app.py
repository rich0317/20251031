from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return JSONResponse(content={"message": "Hello, FastAPI!"})


# 新增 /test1 節點
@app.get("/test1")
def test1():
     return JSONResponse(content={"message": "This is test1 endpoint."})


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
