from fastapi import FastAPI
from mangum import Mangum
x=[]
app = FastAPI()
handler = Mangum(app)

print(3)
@app.get("/")
async def hello():
    return {'message': 'Hello'}

print(3000)
