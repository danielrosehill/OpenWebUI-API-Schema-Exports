# /api/v1/chats/{id}/archive

## Table of contents:
- [post](#post)

- [json file](./_api_v1_chats_{id}_archive.json)

---
<a name="post"></a>
## post

**tags:** ['chats']

**summary:** Archive Chat By Id

**operationId:** archive_chat_by_id_api_v1_chats__id__archive_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/ChatResponse'}, {'type': 'null'}], 'title': 'Response Archive Chat By Id Api V1 Chats  Id  Archive Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

