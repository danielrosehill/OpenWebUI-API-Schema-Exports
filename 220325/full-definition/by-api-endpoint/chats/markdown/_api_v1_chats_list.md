# /api/v1/chats/list

## Table of contents:
- [get](#get)

<a name="get" />
## get

**tags:** ['chats']

**summary:** Get Session User Chat List

**operationId:** get_session_user_chat_list_api_v1_chats_list_get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'page', 'in': 'query', 'required': False, 'schema': {'anyOf': [{'type': 'integer'}, {'type': 'null'}], 'title': 'Page'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/ChatTitleIdResponse'}, 'title': 'Response Get Session User Chat List Api V1 Chats List Get'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

