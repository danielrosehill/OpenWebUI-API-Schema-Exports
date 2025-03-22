# /api/v1/utils/code/format

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['utils']

**summary:** Format Code

**operationId:** format_code_api_v1_utils_code_format_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/CodeForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

