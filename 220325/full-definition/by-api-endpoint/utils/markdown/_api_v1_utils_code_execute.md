# /api/v1/utils/code/execute

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['utils']

**summary:** Execute Code

**operationId:** execute_code_api_v1_utils_code_execute_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/CodeForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

