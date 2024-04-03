from fastapi import FastAPI

app = FastAPI()

from tutorials import firstSteps, pathParams

app.include_router(firstSteps.router)
app.include_router(pathParams.router)
