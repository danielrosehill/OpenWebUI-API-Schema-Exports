# /api/v1/functions/create

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['functions']

**summary:** Create New Function

**operationId:** create_new_function_api_v1_functions_create_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/FunctionForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/FunctionResponse'}, {'type': 'null'}], 'title': 'Response Create New Function Api V1 Functions Create Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

