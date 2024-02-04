from fastapi import FastAPI
import json
from pathlib import Path

local_data = FastAPI()

class DataHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        with open(self.file_path, "r") as json_file:
            return json.load(json_file)

    def process_data(self):
        # Your data processing logic goes here
        # You can access self.data to get the loaded JSON data
        pass

data_handler = DataHandler("exerciseB/fastapi/general_stats.json")

@local_data.get("/")
async def root():
    return {"message": "Processed and analyzed data is available at /general_stats."}

@local_data.get("/general_stats")
async def process_data():
    data_handler.process_data()
    return {"data": data_handler.data}

""" @local_data.get("/get_data/{item_id}")
async def get_data_by_id(item_id: int):
    item = data_handler.get_data_by_id(item_id)
    if item:
        return {"data": item}
    else:
        raise HTTPException(status_code=404, detail="Item not found") """
