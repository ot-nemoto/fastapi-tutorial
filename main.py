from fastapi import Depends, FastAPI, Request


async def verify_token(request: Request):
    return


async def verify_key(request: Request):
    return


app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])
"""
以下は、Global Dependencies検証の為、空のバリデーションチェックを定義
```
dependencies=[Depends(verify_token), Depends(verify_key)]
```
"""

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
    requestForms,
    requestFiles,
    requestFormsAndFiles,
    handlingErrors,
    pathOperationConfiguration,
    encoder,
    bodyUpdates,
    dependencies,
    security,
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
app.include_router(requestForms.router)
app.include_router(requestFiles.router)
app.include_router(requestFormsAndFiles.router)
app.include_router(handlingErrors.router)
app.include_router(pathOperationConfiguration.router)
app.include_router(encoder.router)
app.include_router(bodyUpdates.router)
app.include_router(dependencies.router)
app.include_router(security.router)
