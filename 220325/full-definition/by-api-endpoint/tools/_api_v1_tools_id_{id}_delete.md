# /api/v1/tools/id/{id}/delete

## Table of contents:
- [delete](#delete)

<a name="delete" />
## delete

**tags:** ['tools']

**summary:** Delete Tools By Id

**operationId:** delete_tools_by_id_api_v1_tools_id__id__delete_delete

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'type': 'boolean', 'title': 'Response Delete Tools By Id Api V1 Tools Id  Id  Delete Delete'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

