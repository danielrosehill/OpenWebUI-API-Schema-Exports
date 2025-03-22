# /api/v1/functions/id/{id}/toggle

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['functions']

**summary:** Toggle Function By Id

**operationId:** toggle_function_by_id_api_v1_functions_id__id__toggle_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/FunctionModel'}, {'type': 'null'}], 'title': 'Response Toggle Function By Id Api V1 Functions Id  Id  Toggle Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

