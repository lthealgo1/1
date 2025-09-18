from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

#update
@app.get("/")
async def hello():
    return {'message': 'Hello'}
