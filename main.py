from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)
#update 
print(x)
@app.get("/")
async def hello():
    return {'message': 'Hello'}

#update 2 
print(2)
