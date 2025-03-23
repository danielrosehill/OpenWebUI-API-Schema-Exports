# /api/v1/files/{id}

## Table of contents:
- [get](#get)

- [delete](#delete)

- [json file](./_api_v1_files_{id}.json)

---
<a name="get"></a>
## get

**tags:** ['files']

**summary:** Get File By Id

**operationId:** get_file_by_id_api_v1_files__id__get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/FileModel'}, {'type': 'null'}], 'title': 'Response Get File By Id Api V1 Files  Id  Get'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

<a name="delete"></a>
## delete

**tags:** ['files']

**summary:** Delete File By Id

**operationId:** delete_file_by_id_api_v1_files__id__delete

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

