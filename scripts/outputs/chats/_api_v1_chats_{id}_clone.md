# /api/v1/chats/{id}/clone

## Table of contents:
- [post](#post)

- [json file](./_api_v1_chats_{id}_clone.json)

---
<a name="post"></a>
## post

**tags:** ['chats']

**summary:** Clone Chat By Id

**operationId:** clone_chat_by_id_api_v1_chats__id__clone_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/CloneForm'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/ChatResponse'}, {'type': 'null'}], 'title': 'Response Clone Chat By Id Api V1 Chats  Id  Clone Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

