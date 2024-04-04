from fastapi import FastAPI

app = FastAPI()

from tutorials import firstSteps, pathParams, queryParams

app.include_router(firstSteps.router)
app.include_router(pathParams.router)
app.include_router(queryParams.router)
