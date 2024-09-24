from fastapi import FastAPI

app = FastAPI()

@app.get("/getcode")
async def root():
    return {"message": "test git pull naja go go"}

@app.get("/is_prime/{x}")
async def prime(x:int):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i ==0:
            return False
    return True


@app.get("/plus/{num1}/{num2}")
async def root(num1: int, num2: int):
    result = num1 + num2
    return {"result": result}