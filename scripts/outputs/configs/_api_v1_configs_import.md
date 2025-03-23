# /api/v1/configs/import

## Table of contents:
- [post](#post)

- [json file](./_api_v1_configs_import.json)

---
<a name="post"></a>
## post

**tags:** ['configs']

**summary:** Import Config

**operationId:** import_config_api_v1_configs_import_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ImportConfigForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'type': 'object', 'title': 'Response Import Config Api V1 Configs Import Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

