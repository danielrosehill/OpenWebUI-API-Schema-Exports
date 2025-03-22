# /api/v1/chats/{id}/pin

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['chats']

**summary:** Pin Chat By Id

**operationId:** pin_chat_by_id_api_v1_chats__id__pin_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/ChatResponse'}, {'type': 'null'}], 'title': 'Response Pin Chat By Id Api V1 Chats  Id  Pin Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

