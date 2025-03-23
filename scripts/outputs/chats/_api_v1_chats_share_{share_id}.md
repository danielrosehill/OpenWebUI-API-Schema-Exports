# /api/v1/chats/share/{share_id}

## Table of contents:
- [get](#get)

- [json file](./_api_v1_chats_share_{share_id}.json)

---
<a name="get"></a>
## get

**tags:** ['chats']

**summary:** Get Shared Chat By Id

**operationId:** get_shared_chat_by_id_api_v1_chats_share__share_id__get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'share_id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Share Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/ChatResponse'}, {'type': 'null'}], 'title': 'Response Get Shared Chat By Id Api V1 Chats Share  Share Id  Get'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

