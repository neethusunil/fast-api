from fastapi import FastAPI

#create an object
app = FastAPI() 

#create an endpoint
@app.get("/")
def home():
    return {"Data": "Testing"}
