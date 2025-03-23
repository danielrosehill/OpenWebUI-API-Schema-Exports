# /api/v1/folders/

## Table of contents:
- [get](#get)

- [post](#post)

- [json file](./_api_v1_folders_.json)

---
<a name="get"></a>
## get

**tags:** ['folders']

**summary:** Get Folders

**operationId:** get_folders_api_v1_folders__get

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'items': {'$ref': '#/components/schemas/FolderModel'}, 'type': 'array', 'title': 'Response Get Folders Api V1 Folders  Get'}}}}}

**security:** [{'HTTPBearer': []}]

<a name="post"></a>
## post

**tags:** ['folders']

**summary:** Create Folder

**operationId:** create_folder_api_v1_folders__post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/FolderForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

