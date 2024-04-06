# fastapi-tutorial

## 起動

```sh
uvicorn main:app --reload
```

### Swagger UI

- http://127.0.0.1:8000/docs

### ReDoc

- http://127.0.0.1:8000/redoc

### OpenAPI

- http://127.0.0.1:8000/openapi.json

## セクション

- [最初のステップ](tutorials/firstSteps.py)
- [パスパラメータ](tutorials/pathParams.py)
- [クエリパラメータ](tutorials/queryParams.py)
- [リクエストボディ](tutorials/body.py)
- [クエリパラメータと文字列の検証](tutorials/queryParamsStrValidations.py)
- [パスパラメータと数値の検証](tutorials/pathParamsNumericValidations.py)
- [ボディ - 複数のパラメータ](tutorials/bodyMultipleParams.py)
- [ボディ - フィールド](tutorials/bodyFields.py)
- [ボディ - ネストされたモデル](tutorials/bodyNestedModels.py)
- [スキーマの追加・例](tutorials/schemaExtraExample.py)
- [追加データ型](tutorials/extraDataTypes.py)
- [クッキーのパラメータ](tutorials/cookieParams.py)
- [ヘッダーのパラメータ](tutorials/headerParams.py)
