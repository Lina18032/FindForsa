from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI PyMongo project!"}