# /api/v1/groups/id/{id}/update

## Table of contents:
- [post](#post)

<a name="post" />
## post

**tags:** ['groups']

**summary:** Update Group By Id

**operationId:** update_group_by_id_api_v1_groups_id__id__update_post

**security:** [{'HTTPBearer': []}]

**parameters:** [{'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'string', 'title': 'Id'}}]

**requestBody:** {'required': True, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/GroupUpdateForm'}}}}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/GroupResponse'}, {'type': 'null'}], 'title': 'Response Update Group By Id Api V1 Groups Id  Id  Update Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

