from fastapi import FastAPI
import json
from pathlib import Path

# Create a FastAPI instance

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
        return

local_data_handler = DataHandler("exerciseB/fastapi/general_stats.json")
rse_data_handler = DataHandler("exerciseB/fastapi/rse_data.json")
@local_data.get("/")
async def root():
    return {"message": "Processed and analyzed data is available at /general_stats."}

@local_data.get("/general_stats")
async def process_data():
    local_data_handler.process_data()
    return {"data": local_data_handler.data}

@local_data.get("/rse_data")
async def get_rse_data():
    rse_data_handler.process_data()
    return {"data": rse_data_handler.data}
