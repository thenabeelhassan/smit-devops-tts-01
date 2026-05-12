# Import libararies
from fastapi import FastAPI
import json

# Initialize FastAPI
app = FastAPI()

# Helper Functions

# Helper function to Read JSON file
def read_json_file():
    with open("server.json", "r") as file:
        data = json.load(file)
    return data

# Helper function to Write JSON file
def write_json_file(data):
    with open("server.json", "w") as file:
        json.dump(data, file, indent=4)


# API Logics

# Root API (/)
@app.get("/")
def root_path():
    return {
        "Status": "Server is running",
        "Health": "Healthy"
    }

# Data read API (/data)
@app.get("/data")
def data_read():
    return read_json_file()

# List of servers (/data/serverlist)
@app.get("/data/serverlist")
def server_data_read():
    data = read_json_file()
    return list(data.keys())

# Data read for any specific Object API (/data/{servername})
@app.get("/data/{servername}")
def server_data_read(servername: str):
    data = read_json_file()
    return data.get(servername, {"error": "Server not found"})


# Add new server (/server)
@app.post("/server")
def add_server(server_name: str, server_data: dict):
    data = read_json_file()

    if server_name in data:
        return {"error": "Server already exists."}
    
    data[server_name] = server_data
    write_json_file(data)

    return {"message": "Server addedd."}


# Update a server (/server/{server_name}/{status})
@app.put("/server/{server_name}/{status}")
def update_server_status(server_name: str, status: str):
    data = read_json_file()

    if server_name in data:
        data[server_name]["status"] = status
        write_json_file(data)
        return {"message": f"{server_name} status changed to {status}"}
    
    return {"error": "Server not found."}