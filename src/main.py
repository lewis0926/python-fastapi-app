from fastapi import FastAPI

import redis

r = redis.Redis(host="redis", port=6379)
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World123"}


@app.get("/hits")
def read_root():
    r.set("foo", "bar")
    r.incr("hits")
    return {"Number of hits:": r.get("hits"), "foo": r.get("foo")}
