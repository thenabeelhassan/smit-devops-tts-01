from fastapi import FastAPI
import json

app = FastAPI()

# Read = GET | Write = POST

# localhost:8008/
@app.get("/")
def home():
    return {"message": "API is running"}

# def function_name(parameters):
#     return value 

# def greet(name):
#     return "Hello " + name

def read_json():
    with open("server.json", "r") as file:
        json_data = json.load(file)
    return json_data

data = read_json()

@app.get("/data")
def get_data():
    return data

# def write_json(data):
#     with open("server.json", "w") as file:
#         json.dump(data, file, indent=4)

# data["server1"]["status"] = "stopped"
# write_json(data)

# print(read_json()["server2"]["ip"])
