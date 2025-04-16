from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

# hi 
@app.get("/")
async def hello():
    return {'message': 'Hello'}

#update 
print(4)
