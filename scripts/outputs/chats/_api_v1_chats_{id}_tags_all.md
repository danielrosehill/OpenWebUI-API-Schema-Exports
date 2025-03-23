# /api/v1/chats/{id}/tags/all

## Table of contents:
- [delete](#delete)

- [json file](./_api_v1_chats_{id}_tags_all.json)

---
<a name="delete"></a>
## delete

**tags:** ['chats']

**summary:** Delete All Tags By Id

**operationId:** delete_all_tags_by_id_api_v1_chats__id__tags_all_delete

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'type': 'boolean'}, {'type': 'null'}], 'title': 'Response Delete All Tags By Id Api V1 Chats  Id  Tags All Delete'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

