# /api/v1/chats/new

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['chats']

**summary:** Create New Chat

**operationId:** create_new_chat_api_v1_chats_new_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ChatForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/ChatResponse'}, {'type': 'null'}], 'title': 'Response Create New Chat Api V1 Chats New Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

