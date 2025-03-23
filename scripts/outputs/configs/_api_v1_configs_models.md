# /api/v1/configs/models

## Table of contents:
- [get](#get)

- [post](#post)

- [json file](./_api_v1_configs_models.json)

---
<a name="get"></a>
## get

**tags:** ['configs']

**summary:** Get Models Config

**operationId:** get_models_config_api_v1_configs_models_get

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ModelsConfigForm'}}}}}

**security:** [{'HTTPBearer': []}]

<a name="post"></a>
## post

**tags:** ['configs']

**summary:** Set Models Config

**operationId:** set_models_config_api_v1_configs_models_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ModelsConfigForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ModelsConfigForm'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

