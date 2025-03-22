# /api/v1/files/{id}/content

## Table of contents:
- [get](#get)

<a name="get" />
## get

**tags:** ['files']

**summary:** Get File Content By Id

**operationId:** get_file_content_by_id_api_v1_files__id__content_get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

