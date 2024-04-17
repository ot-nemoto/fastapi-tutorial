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
- [レスポンスモデル](tutorials/responseModel.py)
- [モデル - より詳しく](tutorials/extraModels.py)
- [レスポンスステータスコード](tutorials/responseStatusCode.py)
- [フォームデータ](tutorials/requestForms.py)
- [Request Files](tutorials/requestFiles.py)
- [リクエストフォームとファイル](tutorials/requestFormsAndFiles.py)
- [エラーハンドリング](tutorials/handlingErrors.py)
- [Path Operation の設定](tutorials/pathOperationConfiguration.py)
- [JSON 互換エンコーダ](tutorials/encoder.py)
- [ボディ - 更新](tutorials/bodyUpdates.py)
- [依存関係 - 最初のステップ](tutorials/dependencies.py)
  - [依存関係としてのクラス](tutorials/dependencies_/classes_as_dependencies.py)
  - [サブ依存関係](tutorials/dependencies_/classes_as_dependencies.py)
  - [path operation デコレータの依存関係](tutorials/dependencies_/dependencies_in_path_operation_decorators.py)
  - [Global Dependencies](tutorials/dependencies_/global_dependencies.py)
  - [yield を持つ依存関係](tutorials/dependencies_/dependencies_with_yield.py)
- [セキュリティ入門](tutorials/security.py)
  - [セキュリティ - 最初の一歩](tutorials/security_/first_steps.py)
  - [現在のユーザーの取得](tutorials/security_/get_current_user.py)
  - [Simple OAuth2 with Password and Bearer](tutorials/security_/simple_oauth2.py)
  - [パスワード（およびハッシュ化）による OAuth2、JWT トークンによる Bearer](tutorials/security_/oauth2_jwt.py)
