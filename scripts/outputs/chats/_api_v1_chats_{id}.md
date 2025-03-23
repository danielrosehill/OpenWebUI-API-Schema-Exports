# /api/v1/chats/{id}

## Table of contents:
- [get](#get)

- [post](#post)

- [delete](#delete)

- [json file](./_api_v1_chats_{id}.json)

---
<a name="get"></a>
## get

**tags:** ['chats']

**summary:** Get Chat By Id

**operationId:** get_chat_by_id_api_v1_chats__id__get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/ChatResponse'}, {'type': 'null'}], 'title': 'Response Get Chat By Id Api V1 Chats  Id  Get'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

<a name="post"></a>
## post

**tags:** ['chats']

**summary:** Update Chat By Id

**operationId:** update_chat_by_id_api_v1_chats__id__post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ChatForm'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/ChatResponse'}, {'type': 'null'}], 'title': 'Response Update Chat By Id Api V1 Chats  Id  Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

<a name="delete"></a>
## delete

**tags:** ['chats']

**summary:** Delete Chat By Id

**operationId:** delete_chat_by_id_api_v1_chats__id__delete

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'type': 'boolean', 'title': 'Response Delete Chat By Id Api V1 Chats  Id  Delete'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

