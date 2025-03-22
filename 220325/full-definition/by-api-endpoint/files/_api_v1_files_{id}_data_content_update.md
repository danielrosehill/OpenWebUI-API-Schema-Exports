# /api/v1/files/{id}/data/content/update

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['files']

**summary:** Update File Data Content By Id

**operationId:** update_file_data_content_by_id_api_v1_files__id__data_content_update_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ContentForm'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

