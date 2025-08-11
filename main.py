from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow Flutter to call your API (important for mobile/web apps)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this later to your app's domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Public API is running!"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

@app.post("/sum")
def sum_numbers(a: int, b: int):
    return {"result": a + b}
