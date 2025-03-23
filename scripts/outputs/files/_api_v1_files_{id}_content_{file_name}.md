# /api/v1/files/{id}/content/{file_name}

## Table of contents:
- [get](#get)

- [json file](./_api_v1_files_{id}_content_{file_name}.json)

---
<a name="get"></a>
## get

**tags:** ['files']

**summary:** Get File Content By Id

**operationId:** get_file_content_by_id_api_v1_files__id__content__file_name__get

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

