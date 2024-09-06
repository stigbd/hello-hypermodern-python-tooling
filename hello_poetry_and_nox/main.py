from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello world!"}


@app.get("/covered-by-test")
async def read_covered_by_test(covered: bool | None = None):
    if covered:
        return {"message": "This path is covered by a test!"}
    else:
        return {"message": "This path is not covered by a test!"}
