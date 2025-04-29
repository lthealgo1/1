from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)
#update
print(3)
@app.get("/")
async def hello():
    return {'message': 'Hello'}
