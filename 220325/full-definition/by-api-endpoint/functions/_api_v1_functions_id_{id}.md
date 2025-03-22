# /api/v1/functions/id/{id}

## Table of contents:
- [get](#get)

<a name="get" />
## get

**tags:** ['functions']

**summary:** Get Function By Id

**operationId:** get_function_by_id_api_v1_functions_id__id__get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/FunctionModel'}, {'type': 'null'}], 'title': 'Response Get Function By Id Api V1 Functions Id  Id  Get'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

