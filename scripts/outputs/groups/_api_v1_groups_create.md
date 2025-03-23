# /api/v1/groups/create

## Table of contents:
- [post](#post)

- [json file](./_api_v1_groups_create.json)

---
<a name="post"></a>
## post

**tags:** ['groups']

**summary:** Create New Group

**operationId:** create_new_group_api_v1_groups_create_post

**requestBody:** {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/GroupForm'}}}, 'required': True}

**responses:** {'200': {'description': 'Successful Response', 'content': {'application/json': {'schema': {'anyOf': [{'$ref': '#/components/schemas/GroupResponse'}, {'type': 'null'}], 'title': 'Response Create New Group Api V1 Groups Create Post'}}}}, '422': {'description': 'Validation Error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}}

**security:** [{'HTTPBearer': []}]

