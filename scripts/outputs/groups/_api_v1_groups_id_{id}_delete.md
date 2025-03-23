# /api/v1/groups/id/{id}/delete

## Table of contents:
- [delete](#delete)

- [json file](./_api_v1_groups_id_{id}_delete.json)

---
<a name="delete"></a>
## delete

**tags:** ['groups']

**summary:** Delete Group By Id

**operationId:** delete_group_by_id_api_v1_groups_id__id__delete_delete

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'type': 'boolean', 'title': 'Response Delete Group By Id Api V1 Groups Id  Id  Delete Delete'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

