# /api/v1/functions/id/{id}/valves/update

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['functions']

**summary:** Update Function Valves By Id

**operationId:** update_function_valves_by_id_api_v1_functions_id__id__valves_update_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'type': 'object', 'title': 'Form Data'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'type': 'object'}, {'type': 'null'}], 'title': 'Response Update Function Valves By Id Api V1 Functions Id  Id  Valves Update Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

