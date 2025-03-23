# /api/v1/chats/search

## Table of contents:
- [get](#get)

- [json file](./_api_v1_chats_search.json)

---
<a name="get"></a>
## get

**tags:** ['chats']

**summary:** Search User Chats

**operationId:** search_user_chats_api_v1_chats_search_get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'text', 'in': 'query', 'required': True, 'schema': {'type': 'string', 'title': 'Text'}}, {'name': 'page', 'in': 'query', 'required': False, 'schema': {'anyOf': [{'type': 'integer'}, {'type': 'null'}], 'title': 'Page'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/ChatTitleIdResponse'}, 'title': 'Response Search User Chats Api V1 Chats Search Get'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

