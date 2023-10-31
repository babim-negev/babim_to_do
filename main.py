import uvicorn
from fastapi import FastAPI

from app.core.database_connect import engine, Base


app = FastAPI()

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    uvicorn.run("main:app", host='127.0.0.0', reload=True)

