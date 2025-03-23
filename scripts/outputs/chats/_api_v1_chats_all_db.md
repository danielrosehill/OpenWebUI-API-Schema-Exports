# /api/v1/chats/all/db

## Table of contents:
- [get](#get)

- [json file](./_api_v1_chats_all_db.json)

---
<a name="get"></a>
## get

**tags:** ['chats']

**summary:** Get All User Chats In Db

**operationId:** get_all_user_chats_in_db_api_v1_chats_all_db_get

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'items': {'$ref': '#/components/schemas/ChatResponse'}, 'type': 'array', 'title': 'Response Get All User Chats In Db Api V1 Chats All Db Get'}}}}}

**security:** [{'HTTPBearer': []}]

