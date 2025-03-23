# /api/v1/chats/list/user/{user_id}

## Table of contents:
- [get](#get)

- [json file](./_api_v1_chats_list_user_{user_id}.json)

---
<a name="get"></a>
## get

**tags:** ['chats']

**summary:** Get User Chat List By User Id

**operationId:** get_user_chat_list_by_user_id_api_v1_chats_list_user__user_id__get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'user_id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'User Id'}}, {'name': 'skip', 'in': 'query', 'required': False, 'schema': {'type': 'integer', 'default': 0, 'title': 'Skip'}}, {'name': 'limit', 'in': 'query', 'required': False, 'schema': {'type': 'integer', 'default': 50, 'title': 'Limit'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/ChatTitleIdResponse'}, 'title': 'Response Get User Chat List By User Id Api V1 Chats List User  User Id  Get'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

