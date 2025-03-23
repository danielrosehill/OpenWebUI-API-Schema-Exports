# /api/v1/files/

## Table of contents:
- [get](#get)

- [post](#post)

- [json file](./_api_v1_files_.json)

---
<a name="get"></a>
## get

**tags:** ['files']

**summary:** List Files

**operationId:** list_files_api_v1_files__get

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'items': {'$ref': '#/components/schemas/FileModelResponse'}, 'type': 'array', 'title': 'Response List Files Api V1 Files  Get'}}}}}

**security:** [{'HTTPBearer': []}]

<a name="post"></a>
## post

**tags:** ['files']

**summary:** Upload File

**operationId:** upload_file_api_v1_files__post

**requestBody:** {'content': {'multipart/form-data': {'schema': {'$ref': '#/components/schemas/Body_upload_file_api_v1_files__post'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/FileModelResponse'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

