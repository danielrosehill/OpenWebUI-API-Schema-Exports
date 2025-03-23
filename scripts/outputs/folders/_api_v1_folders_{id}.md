# /api/v1/folders/{id}

## Table of contents:
- [get](#get)

- [delete](#delete)

- [json file](./_api_v1_folders_{id}.json)

---
<a name="get"></a>
## get

**tags:** ['folders']

**summary:** Get Folder By Id

**operationId:** get_folder_by_id_api_v1_folders__id__get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/FolderModel'}, {'type': 'null'}], 'title': 'Response Get Folder By Id Api V1 Folders  Id  Get'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

<a name="delete"></a>
## delete

**tags:** ['folders']

**summary:** Delete Folder By Id

**operationId:** delete_folder_by_id_api_v1_folders__id__delete

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

