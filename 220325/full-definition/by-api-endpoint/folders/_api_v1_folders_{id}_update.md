# /api/v1/folders/{id}/update

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['folders']

**summary:** Update Folder Name By Id

**operationId:** update_folder_name_by_id_api_v1_folders__id__update_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/FolderForm'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

