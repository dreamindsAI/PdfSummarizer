from fastapi import FastAPI
import uvicorn

# Create an instance of the FastAPI class
app = FastAPI()

# Define a simple route that responds to GET requests
@app.get("/")
def read_root():
    return {"Server is running.."}

if __name__ == "__main__":

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
