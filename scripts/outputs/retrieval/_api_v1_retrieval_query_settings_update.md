# /api/v1/retrieval/query/settings/update

## Table of contents:
- [post](#post)

- [json file](./_api_v1_retrieval_query_settings_update.json)

---
<a name="post"></a>
## post

**tags:** ['retrieval']

**summary:** Update Query Settings

**operationId:** update_query_settings_api_v1_retrieval_query_settings_update_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/QuerySettingsForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

