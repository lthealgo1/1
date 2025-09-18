from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

print(0)
@app.get("/")
async def hello():
    return {'message': 'Hello'}


#hello
print(1)
