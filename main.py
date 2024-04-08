from fastapi import FastAPI

app = FastAPI()

from tutorials import (
    firstSteps,
    pathParams,
    queryParams,
    body,
    queryParamsStrValidations,
    pathParamsNumericValidations,
    bodyMultipleParams,
    bodyFields,
    bodyNestedModels,
    schemaExtraExample,
    extraDataTypes,
    cookieParams,
    headerParams,
    responseModel,
    extraModels,
    responseStatusCode,
)

app.include_router(firstSteps.router)
app.include_router(pathParams.router)
app.include_router(queryParams.router)
app.include_router(body.router)
app.include_router(queryParamsStrValidations.router)
app.include_router(pathParamsNumericValidations.router)
app.include_router(bodyMultipleParams.router)
app.include_router(bodyFields.router)
app.include_router(bodyNestedModels.router)
app.include_router(schemaExtraExample.router)
app.include_router(extraDataTypes.router)
app.include_router(cookieParams.router)
app.include_router(headerParams.router)
app.include_router(responseModel.router)
app.include_router(extraModels.router)
app.include_router(responseStatusCode.router)
