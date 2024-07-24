from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from gemini import getCompletion
import uvicorn
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/{str}")
async def getData(string:str):
    response = await getCompletion(string)
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
