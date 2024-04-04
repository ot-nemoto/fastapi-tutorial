from fastapi import FastAPI

app = FastAPI()

from tutorials import (
    firstSteps,
    pathParams,
    queryParams,
    body,
    queryParamsStrValidations,
)

app.include_router(firstSteps.router)
app.include_router(pathParams.router)
app.include_router(queryParams.router)
app.include_router(body.router)
app.include_router(queryParamsStrValidations.router)
