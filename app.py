import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    file = open("name.json", 'r')
    read_content = file.read()
    print(read_content)
    return file


if __name__== "__main__":
    uvicorn.run ("app:app",port=5000,reload=True)