# /api/v1/knowledge/{id}/delete

## Table of contents:
- [delete](#delete)

- [json file](./_api_v1_knowledge_{id}_delete.json)

---
<a name="delete"></a>
## delete

**tags:** ['knowledge']

**summary:** Delete Knowledge By Id

**operationId:** delete_knowledge_by_id_api_v1_knowledge__id__delete_delete

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'type': 'boolean', 'title': 'Response Delete Knowledge By Id Api V1 Knowledge  Id  Delete Delete'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

