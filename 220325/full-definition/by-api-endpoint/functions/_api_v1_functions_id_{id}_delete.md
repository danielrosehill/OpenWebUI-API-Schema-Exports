# /api/v1/functions/id/{id}/delete

## Table of contents:
- [delete](#delete)

<a name="delete" />
## delete

**tags:** ['functions']

**summary:** Delete Function By Id

**operationId:** delete_function_by_id_api_v1_functions_id__id__delete_delete

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'type': 'boolean', 'title': 'Response Delete Function By Id Api V1 Functions Id  Id  Delete Delete'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

