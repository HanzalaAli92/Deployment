from fastapi import FastAPI

# CReate aFastAPI application instance
app = FastAPI()

# Define a GET endpoint at the route "/hello"
@app.get("/hello")
async def hello_world():
    # Return a simple string response
    return {"message": "Hello World"}
