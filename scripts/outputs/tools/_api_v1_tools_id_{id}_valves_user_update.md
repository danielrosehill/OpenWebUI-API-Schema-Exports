# /api/v1/tools/id/{id}/valves/user/update

## Table of contents:
- [post](#post)

- [json file](./_api_v1_tools_id_{id}_valves_user_update.json)

---
<a name="post"></a>
## post

**tags:** ['tools']

**summary:** Update Tools User Valves By Id

**operationId:** update_tools_user_valves_by_id_api_v1_tools_id__id__valves_user_update_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'type': 'object', 'title': 'Form Data'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'type': 'object'}, {'type': 'null'}], 'title': 'Response Update Tools User Valves By Id Api V1 Tools Id  Id  Valves User Update Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

