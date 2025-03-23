# /api/v1/chats/folder/{folder_id}

## Table of contents:
- [get](#get)

- [json file](./_api_v1_chats_folder_{folder_id}.json)

---
<a name="get"></a>
## get

**tags:** ['chats']

**summary:** Get Chats By Folder Id

**operationId:** get_chats_by_folder_id_api_v1_chats_folder__folder_id__get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'folder_id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Folder Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/ChatResponse'}, 'title': 'Response Get Chats By Folder Id Api V1 Chats Folder  Folder Id  Get'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

