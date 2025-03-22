# /api/v1/chats/{id}/share

## Table of contents:
- [post](#post)
- [delete](#delete)

<a name="post" />
## post

**tags:** ['chats']

**summary:** Share Chat By Id

**operationId:** share_chat_by_id_api_v1_chats__id__share_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/ChatResponse'}, {'type': 'null'}], 'title': 'Response Share Chat By Id Api V1 Chats  Id  Share Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

<a name="delete" />
## delete

**tags:** ['chats']

**summary:** Delete Shared Chat By Id

**operationId:** delete_shared_chat_by_id_api_v1_chats__id__share_delete

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'type': 'boolean'}, {'type': 'null'}], 'title': 'Response Delete Shared Chat By Id Api V1 Chats  Id  Share Delete'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

