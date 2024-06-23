from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def main(name: str):
    return {"message": f"Hello, {name}"}

@app.get('/hello')
def hello():
    a = await main()
    return a
