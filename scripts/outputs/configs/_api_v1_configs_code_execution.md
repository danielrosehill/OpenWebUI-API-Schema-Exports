# /api/v1/configs/code_execution

## Table of contents:
- [get](#get)

- [post](#post)

- [json file](./_api_v1_configs_code_execution.json)

---
<a name="get"></a>
## get

**tags:** ['configs']

**summary:** Get Code Execution Config

**operationId:** get_code_execution_config_api_v1_configs_code_execution_get

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/CodeInterpreterConfigForm'}}}}}

**security:** [{'HTTPBearer': []}]

<a name="post"></a>
## post

**tags:** ['configs']

**summary:** Set Code Execution Config

**operationId:** set_code_execution_config_api_v1_configs_code_execution_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/CodeInterpreterConfigForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/CodeInterpreterConfigForm'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

