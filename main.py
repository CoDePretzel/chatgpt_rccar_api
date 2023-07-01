from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()

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

@app.get("/.well-known/ai-plugin.json", include_in_schema=False)
async def serve_manifest():
    try:
        with open("./manifest.json") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

