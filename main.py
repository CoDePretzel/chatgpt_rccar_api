from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.mount("/", StaticFiles(directory="."), name="root")

class RCCar:
    def __init__(self):
        self.direction = "stopped"

    def move_forward(self):
        self.direction = "forward"

    def move_backward(self):
        self.direction = "backward"

    def turn_left(self):
        self.direction = "left"

    def turn_right(self):
        self.direction = "right"

car = RCCar()

class CarAction(BaseModel):
    action: str

@app.post("/car/move")
async def move_car(action: CarAction):
    if action.action == "forward":
        car.move_forward()
    elif action.action == "backward":
        car.move_backward()
    elif action.action == "left":
        car.turn_left()
    elif action.action == "right":
        car.turn_right()
    else:
        raise HTTPException(status_code=400, detail="Invalid action")

    return {"status": "success", "action": action.action}

# @app.get("/.well-known/ai-plugin.json", include_in_schema=False)
# async def serve_manifest():
#     try:
#         with open("./manifest.json") as f:
#             data = f.read()
#             # data = json.load(f)
#         # return data
#         return JSONResponse(content=json.loads(data))
#     except FileNotFoundError:
#         raise HTTPException(status_code=404, detail="File not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5003)

