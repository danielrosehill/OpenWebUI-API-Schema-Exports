# /api/v1/folders/{id}/update/parent

## Table of contents:
- [post](#post)

- [json file](./_api_v1_folders_{id}_update_parent.json)

---
<a name="post"></a>
## post

**tags:** ['folders']

**summary:** Update Folder Parent Id By Id

**operationId:** update_folder_parent_id_by_id_api_v1_folders__id__update_parent_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/FolderParentIdForm'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

